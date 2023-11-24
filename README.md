# BGCode

Plugin allows for the upload and conversion of bgcode files introduced in PrusaSlicer version 2.7.0+.

## Prerequisites

If installing on Windows you'll need some additional applications installed to complete the build process prior to installing the plugin. These are already included on OctoPi image, and possibly octoprint_deploy installations (need to verify). 

### Install the tools

Install Visual Studio Community 2019, or higher from [visualstudio.microsoft.com/vs/](https://visualstudio.microsoft.com/vs/).
Older versions are not supported as libbgcode requires support for C++17.
Select all workload options for C++ and make sure to launch Visual Studio after install (to ensure that the full setup completes).

Install CMake for Windows from [cmake.org](https://cmake.org/)
Download and run the exe accepting all defaults

Install git for Windows from [gitforwindows.org](https://gitforwindows.org/)
Download and run the exe accepting all defaults

## Setup

Install manually using this URL:

    https://github.com/jneilliii/OctoPrint-BGCode/archive/master.zip

## TODO

[X] ~~bundle libbgcode somehow~~

