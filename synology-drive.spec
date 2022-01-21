%global   debug_package %{nil}

%define synology_version 3.0.3
%define synology_release 12689

Name:     synology-drive
Version:  %{synology_version}
Release:  %{synology_release}%{?dist}
Summary:  Unofficial RPM build of Synology Drive Client
License:  custom

Source0:  https://global.download.synology.com/download/Utility/SynologyDriveClient/%{synology_version}-%{synology_release}/Ubuntu/Installer/x86_64/synology-drive-client-%{synology_release}.x86_64.deb

AutoReqProv: no
Requires: glibc
Requires: glib2
Requires: gtk2

# For Nautilus integration
Requires: nautilus
Requires: nautilus-extensions

# For tray icon on Gnome
Requires: gnome-shell-extension-appindicator

%description
Synology Drive Client allows you to sync your computers with Synology NAS and back up the computer to the NAS.

%prep
ar x %{_sourcedir}/synology-drive-client-%{synology_release}.x86_64.deb data.tar.xz
tar xf data.tar.xz

%install
# software
mkdir -p %{buildroot}/opt/Synology/
cp -r opt/Synology/SynologyDrive/ %{buildroot}/opt/Synology/

# executable
mkdir -p %{buildroot}%{_bindir}/
install -Dm 755 usr/bin/synology-drive -t %{buildroot}%{_bindir}/

# nautilus
mkdir -p %{buildroot}%{_libdir}/nautilus/extensions-3.0/
install -Dm 644 usr/lib/nautilus/extensions-3.0/libnautilus-drive-extension.so -t %{buildroot}%{_libdir}/nautilus/extensions-3.0/

# desktop
mkdir -p %{buildroot}%{_datarootdir}/applications/
install -Dm 644 usr/share/applications/synology-drive.desktop -t %{buildroot}%{_datarootdir}/applications/
mkdir -p %{buildroot}%{_datarootdir}/icons/
cp -r usr/share/icons/hicolor/ %{buildroot}%{_datarootdir}/icons/

%files
%license opt/Synology/SynologyDrive/LICENSE.txt
%doc usr/share/doc/synology-drive/changelog.gz

/opt/Synology/SynologyDrive/
%{_bindir}/synology-drive
%{_libdir}/nautilus/extensions-3.0/libnautilus-drive-extension.so
%{_datarootdir}/applications/synology-drive.desktop
%{_datarootdir}/icons/hicolor/16x16/apps/synology-drive.png
%{_datarootdir}/icons/hicolor/24x24/apps/synology-drive.png
%{_datarootdir}/icons/hicolor/32x32/apps/synology-drive.png
%{_datarootdir}/icons/hicolor/48x48/apps/synology-drive.png
%{_datarootdir}/icons/hicolor/64x64/apps/synology-drive.png
%{_datarootdir}/icons/hicolor/128x128/apps/synology-drive.png
%{_datarootdir}/icons/hicolor/256x256/apps/synology-drive.png
%{_datarootdir}/icons/hicolor/512x512/apps/synology-drive.png

%changelog
* Fri Jan 21 2022 Maxime dirksen <emixampp@fedoraproject.org> - 3.0.3-12689
- Version 3.0.3-12689 of Synology Drive Client
