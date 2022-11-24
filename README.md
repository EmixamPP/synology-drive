# <p align=center>synology-drive</p>

Unofficial RPM package of Synology Drive Client <https://www.synology.com>.

Since the package provided by FlatHub is not 100% functional and the method of converting deb to rpm by Alien requires a lot of manipulation. I decided to create myself a clean and 100% functional RPM package for Synology Drive Client.

I have include the file explorer Nautilus as dependency in order to have access to the share menu and to have the file sync status indicator (like on Windows or Ubuntu). :warning: No longer works with Nautilus > 43. I'm waiting for a fix from Synology. Subscribe to issue [#3](https://github.com/EmixamPP/synology-drive/issues/3) to know when the feature will be fixed.\
I also have include a GNOME shell extension as dependency in order to see the tray icon (works natively with KDE).\
I have build a second package for user's which didn't use GNOME. It does not contain the two dependencies mentioned above (they can be installed later if you want).



## Installation
If you have previously installed Synology Drive Client with Alien or Flatpak (i.e. from another source than my repo), please ensure that they are uninstalled.

### Method 1: install from COPR repo (recommended to get updates)
Page link : [COPR package](https://copr.fedorainfracloud.org/coprs/emixampp/synology-drive/).

1. `sudo dnf copr enable emixampp/synology-drive`
2. For GNOME: `sudo dnf --refresh install synology-drive`
3. For other desktop environments: `sudo dnf --refresh install synology-drive-noextra`

### Method 2: build the package locally (no update)
1. Install build tools : `sudo dnf install rpm-build rpmdevtools`
2. `git clone https://github.com/EmixamPP/synology-drive.git`
3. `cd synology-drive`
4. Optional, if you want to change the version:
   1. Consult the [release notes](https://www.synology.com/en-global/releaseNote/SynologyDriveClient) and choose the desired version (>= 3.0.0-12663)
   2. Edit the two first lines of `synology-drive.spec` or `synology-drive-noextra.spec`, depending on whether you are running GNOME or another desktop environement. 
5. For GNOME:
   1. `spectool -g -R synology-drive.spec`
   2. `rpmbuild -ba synology-drive.spec`
   3. `sudo dnf install ~/rpmbuild/RPMS/x86_64/synology-drive-*.x86_64.rpm`
6. For other desktop environments: 
   1. `spectool -g -R synology-drive-noextra.spec`
   2. `rpmbuild -ba synology-drive-noextra.spec`
   3. `sudo dnf install ~/rpmbuild/RPMS/x86_64/synology-drive-noextra-*.x86_64.rpm`
7. Clean build root : `rm -r ~/rpmbuild`

<!--- No more maintained
### Method 3: download a specific version from GitHub (no update)
1. Go to the [release page](https://github.com/EmixamPP/synology-drive/releases)
2. Download the RPM package of your choice depedning on: 
   1. The desired version (I recommend the most recent one)
   2. The prefix synology-drive for GNOME, or synology-drive-noextra for the other desktop environements
   3. The suffix corresponding to your Linux distribution (where X is a digit) (if your distro is not in the table, try a package for Fedora): 
      | Suffix     | Distro              |
      | ---        | ---                 |
      | elXXX      | Fedora eln          |
      | elX        | Centos-stream X     |
      | fcXX       | Fedora XX           |
      | mgaX       | Mageia X            |
      | suse.lpXXX | openSUSE Leap XX.X  |
      | suse.tw    | openSUSE Tumbleweed |
3. Execute `sudo dnf install synology-drive-*.x86_64.rpm`
-->

## Legal information
This is an unofficial build. Therefore, this RPM package is not verified by, affiliated with, or supported by Synology Inc.

Synology Drive Client is registered under the Copyright Synology Inc. <https://www.synology.com/en-global/company/legal/terms_EULA>.

This project has been authorized by Synology Inc.
