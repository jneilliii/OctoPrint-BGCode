# coding=utf-8
from __future__ import absolute_import

import os
import glob
import octoprint.plugin
import pybgcode
from octoprint.filemanager import DiskFileWrapper


class BgcodePlugin(octoprint.plugin.SettingsPlugin
                   ):
    def __init__(self):
        super().__init__()

    # -- bgcode upload extension tree hook

    def get_extension_tree(self, *args, **kwargs):
        return {'machinecode': {'gcode': ["bgcode", "bgc"]}}

    # ~~ bgcode upload preprocessor hook

    def bgcode_upload(self, path, file_object, links=None, printer_profile=None, allow_overwrite=True, *args, **kwargs):
        bgcode_extensions = [".bgcode", ".bgc"]
        name, extension = os.path.splitext(file_object.filename)
        if extension in bgcode_extensions:
            try:
                # quick cleanup if any gcode files left over from plugin conflicts
                # https://github.com/jneilliii/OctoPrint-BGCode/issues/15
                for f in glob.glob(os.path.join(self.get_plugin_data_folder(), "*.gcode")):
                    os.remove(f)
                temp_file_path = os.path.join(self.get_plugin_data_folder(), file_object.filename)
                self._logger.debug(f"saving file to extract from: {temp_file_path}")
                file_object.save(temp_file_path)
                gcode_file_path = os.path.join(self.get_plugin_data_folder(), f"{name}.gcode")
                self._logger.debug(f"converting {temp_file_path} to {gcode_file_path}")
                bgcode_file = pybgcode.open(temp_file_path, "rb")
                gcode_file = pybgcode.open(gcode_file_path, "w")
                pybgcode.from_binary_to_ascii(bgcode_file, gcode_file, verify_checksum=False)
                self._logger.debug("closing bgcode file objects used during conversion")
                pybgcode.close(gcode_file)
                pybgcode.close(bgcode_file)
                file_wrapper = DiskFileWrapper(path.replace(".bgcode", ".gcode"), gcode_file_path, move=True)
                self._logger.debug(f"created file wrapper object {file_wrapper}")
                self._logger.debug(f"removing temporary file {temp_file_path}")
                os.remove(temp_file_path)
                return file_wrapper
            except Exception as e:
                self._logger.debug(f"There was an error: {e}")
        return file_object

    # ~~ Routes hook

    def route_hook(self, server_routes, *args, **kwargs):
        from octoprint.server.util.tornado import LargeResponseHandler, path_validation_factory
        from octoprint.util import is_hidden_path
        return [
            (r"thumbnail/(.*)", LargeResponseHandler,
             {'path': self.get_plugin_data_folder(), 'as_attachment': False, 'path_validation': path_validation_factory(
                 lambda path: not is_hidden_path(path), status_code=404)})
        ]

    # ~~ Softwareupdate hook

    def get_update_information(self):
        return {
            "bgcode": {
                "displayName": "BGCode",
                "displayVersion": self._plugin_version,

                # version check: github repository
                "type": "github_release",
                "user": "jneilliii",
                "repo": "OctoPrint-BGCode",
                "current": self._plugin_version,

                # update method: pip
                "pip": "https://github.com/jneilliii/OctoPrint-BGCode/archive/{target_version}.zip",
            }
        }

    # ~~ Backup additional excludes hook

    def additional_excludes_hook(self, excludes, *args, **kwargs):
        if "uploads" in excludes:
            return ["."]
        return []


__plugin_name__ = "BGCode"
__plugin_pythoncompat__ = ">=3.8,<4"  # Only Python 3.8+


def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = BgcodePlugin()

    global __plugin_hooks__
    __plugin_hooks__ = {
        "octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information,
        "octoprint.filemanager.extension_tree": __plugin_implementation__.get_extension_tree,
        "octoprint.filemanager.preprocessor": (__plugin_implementation__.bgcode_upload, 1),
        "octoprint.server.http.routes": __plugin_implementation__.route_hook,
        "octoprint.plugin.backup.additional_excludes": __plugin_implementation__.additional_excludes_hook
    }
