# BGCode

Plugin allows for the upload and conversion of bgcode files introduced in PrusaSlicer version 2.7.0+. I cannot control what is in the file during the conversion process, this plugin is just using the tool provided by PrusaResearch to convert from one format to another. If there are issues related to the ascii format file that cause other plugins to not work then you should open an issue on the conflicting plugin's repository, the PrusaResearch repository for the tool [here](https://github.com/prusa3d/libbgcode/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc), or for PrusaSlicer [here](https://github.com/prusa3d/PrusaSlicer/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc). See below for currently known conflicting plugins and related errors. 

## Prerequisites

If installing on Windows or on octo4a you'll need some additional applications installed to complete the build process prior to installing the plugin. These are already included on OctoPi image, and possibly octoprint_deploy installations (need to verify). 

### Windows - Install the tools

Install Visual Studio Community 2019, or higher from [visualstudio.microsoft.com/vs/](https://visualstudio.microsoft.com/vs/).
Older versions are not supported as libbgcode requires support for C++17.
Select all workload options for C++ and make sure to launch Visual Studio after install (to ensure that the full setup completes).

Install CMake for Windows from [cmake.org](https://cmake.org/)
Download and run the exe accepting all defaults

Install git for Windows from [gitforwindows.org](https://gitforwindows.org/)
Download and run the exe accepting all defaults

### octo4a - Install the tools

After setting up OpenSSH server on settings tab, You can go to `http://<your-ip>:5002` and use root username and the password you selected on the settings tab. Run these commands to add the necessary system dependencies.

```
apk add git
apk add zlib-dev
```

## Setup

Install manually using this URL:

    https://github.com/jneilliii/OctoPrint-BGCode/archive/master.zip

## TODO

[X] ~~bundle libbgcode somehow~~

## Known Issues/Plugin Conflicts

- ~~SlicerEstimator: `UnicodeDecodeError: 'utf-8' codec can't decode byte 0x8a in position 1: invalid start byte`~~ resolved by setting hook order
- DisplayLayerProgress: `Layer indicator not found in file`

---

## Get Help

If you experience issues with this plugin or need assistance please use the issue tracker by clicking issues above.

## Additional Plugins

Check out my other plugins [here](https://plugins.octoprint.org/by_author/#jneilliii)

---

## Sponsors
- Andreas Lindermayr
- [@TheTuxKeeper](https://github.com/thetuxkeeper)
- [@tideline3d](https://github.com/tideline3d/)
- [SimplyPrint](https://simplyprint.io/)
- [Andrew Beeman](https://github.com/Kiendeleo)
- [Calanish](https://github.com/calanish)
- [Lachlan Bell](https://lachy.io/)
- [Johnny Bergdal](https://github.com/bergdahl)
- [Leigh Johnson](https://github.com/leigh-johnson)
- [Stephen Berry](https://github.com/berrystephenw)
- [Steve Dougherty](https://github.com/Thynix)
## Support My Efforts
I, jneilliii, programmed this plugin for fun and do my best effort to support those that have issues with it, please return the favor and leave me a tip or become a Patron if you find this plugin helpful and want me to continue future development.

[![Patreon](patreon-with-text-new.png)](https://www.patreon.com/jneilliii) [![paypal](paypal-with-text.png)](https://paypal.me/jneilliii)

<small>No paypal.me? Send funds via PayPal to jneilliii&#64;gmail&#46;com

You can use [this](https://www.paypal.com/cgi-bin/webscr?cmd=_xclick&business=jneilliii@gmail.com) link too. But the normal PayPal fee will be deducted.
</small>

