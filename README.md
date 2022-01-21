# <p align=center>synology-drive</p>

Unofficial RPM package of Synology Drive Client <https://www.synology.com>.

Since the package provided by FlatHub is not 100% functional and the method of converting deb to rpm by Alien requires a lot of manipulation. I decided to create myself a clean and 100% functional RPM package for Synology Drive Client.

I have include the file explorer Nautilus as dependency in order to have access to the share menu and to have the file sync status indicator (like on Windows or Ubuntu).\
I also have include a GNOME shell extension as dependency in order to see the tray icon (works natively with KDE).\
I have build a second package for user's which didn't use GNOME. It does not contain the two dependencies mentioned above (they can be installed later if you want).

## Installation
If you have previously installed Synology Drive Client with Alien or Flatpak (i.e. from another source than my repo), please ensure that they are uninstalled.

### Method 1: install from COPR repo (recommended to get updates)
Page link : [COPR package](https://copr.fedorainfracloud.org/coprs/emixampp/synology-drive/).

1. `sudo dnf copr enable emixampp/synology-drive`
2. For GNOME: `sudo dnf --refresh install synology-drive`
3. For other desktop environments: `sudo dnf --refresh install synology-drive-noextra`

### Method 2: download from GitHub
1. Go to <https://github.com/EmixamPP/synology-drive/releases>
2. Download the RPM package of your choice (I recommend the most recent one)
3. Execute `sudo dnf localinstall synology-drive-*.x86_64.rpm`

## Legal information
The build instructions of the RPM package are contained in the `synology-drive.spec` file. And, as you can see, this is just a wrapper of the installation instructions of the official `.deb` package.

As mentioned this is an unofficial build, therefore this RPM package is not verified by, affiliated with, or supported by Synology Inc.

I solemnly declare that no action has been performed on the source code of the software. Therefore, all its licences are retained.

Synology Drive Client is registered under the Copyright Synology Inc. <https://www.synology.com/en-global/company/legal/terms_EULA>.
