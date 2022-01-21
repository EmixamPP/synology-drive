# <p align=center>synology-drive</p>

Unofficial RPM package of Synology Drive Client <https://www.synology.com>.

Since the package provided by FlatHub is not 100% functional and the method of converting deb to rpm by Alien requires a lot of manipulation. I decided to recreate myself a clean and 100% functional RPM package for Synology Drive Client.

I have include the file explorer Nautilus as dependency in order to have access to the share menu and to have the file sync status indicator (like on Windows or Ubuntu).\
I also have include a gnome shell extension as dependency in order to see the tray icon (works natively with KDE).\
If you want a build without the gnome extension and/or Nautilus, feel free to open an issue.

## Installation
If you have previously installed Synology Drive Client with Alien or Flatpak (i.e. from another source than my repo), please ensure that they are uninstalled.

### Method 1, download from COPR repo (recommended to get updates)
Page link : [COPR package](https://copr.fedorainfracloud.org/coprs/emixampp/synology-drive/).

``` shell
sudo dnf copr enable emixampp/synology-drive
sudo dnf --refresh install synology-drive
```

### Method 2, download a rpm package that I built
1. Go to <https://github.com/EmixamPP/synology-drive/releases>
2. Download the version of your choice (I recommend the most recent one)
3. Unzip and execute `sudo dnf localinstall synology-drive-*.x86_64.rpm`

## Legal information
The build instructions of the RPM package are contained in the `synology-drive.spec` file. And, as you can see, this is just a wrapper of the installation instructions of the official `.deb` package.

As mentioned this is an unofficial build, therefore this RPM package is not verified by, affiliated with, or supported by Synology Inc.

I solemnly declare that no action has been performed on the source code of the software. Therefore, all its licenses are retained.

Synology Drive Client is registered under the Copyright Synology Inc. <https://www.synology.com/en-global/company/legal/terms_EULA>.
