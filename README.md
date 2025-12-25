# <p align=center>synology-drive</p>

Unofficial RPM package of Synology Drive Client <https://www.synology.com>.

Since the package provided by FlatHub is not 100% functional and the method of converting deb to rpm by Alien requires a lot of manipulation. I decided to create myself a clean and 100% functional RPM package for Synology Drive Client.

In addition to the base package `synology-drive`, I provide two optional extra packages:
- `synology-drive-nautilus`: Adds integration with the Nautilus file manager, providing access to the context share menu and file synchronization status indicators (similar to Windows or the official Ubuntu package).
- `synology-drive-gnome`: Adds integration with the GNOME Shell top bar tray icon (works natively with KDE).

## Installation
If you have previously installed Synology Drive Client with Alien or Flatpak (i.e. from another source than my repo), please ensure that they are uninstalled.

If you like the project, do not hesitate to star the repository to support me, thank you!

### Method 1: install from COPR repo (recommended to get updates)
Page link : [COPR package](https://copr.fedorainfracloud.org/coprs/emixampp/synology-drive/).

1. `sudo dnf copr enable emixampp/synology-drive`
2. `sudo dnf --refresh install synology-drive`
3. For GNOME tray icon integration: `sudo dnf install synology-drive-gnome`
4. For Nautilus file integration: `sudo dnf install synology-drive-nautilus`

### Method 2: build the package locally (no update)
1. Install build tools : `sudo dnf install rpm-build rpmdevtools`
2. `git clone https://github.com/EmixamPP/synology-drive.git`
3. `cd synology-drive`
4. Optional, if you want to change the version:
   1. Consult the [release notes](https://www.synology.com/en-global/releaseNote/SynologyDriveClient) and choose the desired version (>= 3.2.1-13271)
   2. Edit the two first lines of `synology-drive.spec`.
5. `spectool -g -R synology-drisve.spec`
6. `rpmbuild -bb --noclean synology-drive.spec`
7. `sudo dnf install ~/rpmbuild/RPMS/x86_64/synology-drive-*.rpm`
8. If everything is ok, you can clean the build root : `rm -r ~/rpmbuild`

## Legal information
Consult the [LICENSE](https://github.com/EmixamPP/synology-drive/blob/main/LICENSE).

This project has been authorized by Synology Inc.
