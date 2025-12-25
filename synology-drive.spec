%global synology_version 4.0.1
%global synology_release 17885

Name:       synology-drive
Version:    %{synology_version}
Release:    %{synology_release}.6%{?dist}
Summary:    Unofficial RPM build of Synology Drive Client
License:    Multiple, see https://www.synology.com/en-global/company/legal/terms_EULA
URL:        https://www.synology.com/
Source0:    https://global.synologydownload.com/download/Utility/SynologyDriveClient/%{synology_version}-%{synology_release}/Ubuntu/Installer/synology-drive-client-%{synology_release}.x86_64.deb

AutoReqProv: no
Recommends: %{name}-gnome

BuildRequires: binutils
BuildRequires: xz
BuildRequires: tar

%description
Synology Drive Client allows you to sync your computers with Synology NAS and back up the computer to the NAS.

%package base
Summary:     Unofficial RPM build of Synology Drive Client
Conflicts:   synology-drive-noextra
Obsoletes:   synology-drive-noextra <= 4.0.1-17885
AutoReqProv: no
Requires:    glibc >= 2.19
Requires:    glib2 >= 2.16.0
Requires:    gtk2 >= 2.12.0

%description base
Synology Drive Client allows you to sync your computers with Synology NAS and back up the computer to the NAS.

%package nautilus
Summary:    Nautilus integrations for %{name}
AutoReqProv: no
Requires:   %{name}-base = %{version}-%{release}
Requires:   nautilus >= 43.0
Requires:   nautilus-extensions >= 43.0

%description nautilus
This package provides Nautilus integration for %{name}.

%package gnome
Summary:    GNOME integrations for %{name}
AutoReqProv: no
Requires:   %{name}-base
Requires:   %{name}-nautilus
Requires:   gnome-shell-extension-appindicator

%description gnome
This package provides GNOME integrations for %{name}.

%prep
ar x %{_sourcedir}/synology-drive-client-%{synology_release}.x86_64.deb data.tar.xz
tar xf data.tar.xz

# disable auto update
sed -i "s|https://utyupdate.synology.com||" opt/Synology/SynologyDrive/package/cloudstation/conf/update.conf
sed -i "s|/getUpdate||" opt/Synology/SynologyDrive/package/cloudstation/conf/update.conf

%install
export QA_RPATHS=$(( 0x0002|0x0020 )) # ignore rpath error since 3.1.0-12920

# software
mkdir -p %{buildroot}/opt/Synology/
cp -rp opt/Synology/SynologyDrive/ %{buildroot}/opt/Synology/

# executable
mkdir -p %{buildroot}%{_bindir}/
install -Dm 755 usr/bin/synology-drive -t %{buildroot}%{_bindir}/

# nautilus extension
mkdir -p %{buildroot}%{_libdir}/nautilus/extensions-4/
install -Dm 644 usr/lib/nautilus/extensions-4/libnautilus-drive-extension-4.so -t %{buildroot}%{_libdir}/nautilus/extensions-4/

# desktop
mkdir -p %{buildroot}%{_datarootdir}/applications/
install -Dm 644 usr/share/applications/synology-drive.desktop -t %{buildroot}%{_datarootdir}/applications/
mkdir -p %{buildroot}%{_datarootdir}/icons/
cp -rp usr/share/icons/hicolor/ %{buildroot}%{_datarootdir}/icons/

%files
%{nil}

%files base
%license opt/Synology/SynologyDrive/LICENSE.txt
%doc usr/share/doc/synology-drive/changelog.gz
/opt/Synology/SynologyDrive/
%{_bindir}/synology-drive
%{_datarootdir}/applications/synology-drive.desktop
%{_datarootdir}/icons/hicolor/16x16/apps/synology-drive.png
%{_datarootdir}/icons/hicolor/24x24/apps/synology-drive.png
%{_datarootdir}/icons/hicolor/32x32/apps/synology-drive.png
%{_datarootdir}/icons/hicolor/48x48/apps/synology-drive.png
%{_datarootdir}/icons/hicolor/64x64/apps/synology-drive.png
%{_datarootdir}/icons/hicolor/128x128/apps/synology-drive.png
%{_datarootdir}/icons/hicolor/256x256/apps/synology-drive.png
%{_datarootdir}/icons/hicolor/512x512/apps/synology-drive.png

%files nautilus
%{_libdir}/nautilus/extensions-4/libnautilus-drive-extension-4.so

%files gnome
%{nil}

%changelog
* Sat Nov 15 2025 Maxime Dirksen <dev@emixam.be> - 4.0.1-17885
- Version 4.0.1-17885 of Synology Drive Client
* Mon Oct 20 2025 Maxime Dirksen <dev@emixam.be> - 4.0.0-17877
- Version 4.0.0-17877 of Synology Drive Client
* Fri Mar 14 2025 Maxime Dirksen <dev@emixam.be> - 3.5.2-16111
- Version 3.5.2-16111 of Synology Drive Client
* Wed Feb 19 2025 Maxime Dirksen <dev@emixam.be> - 3.5.2-16110
- Version 3.5.2-16110 of Synology Drive Client
* Wed Nov 06 2024 Maxime Dirksen <dev@emixam.be> - 3.5.1-16102
- Version 3.5.1-16102 of Synology Drive Client
* Mon Aug 26 2024 Maxime Dirksen <dev@emixam.be> - 3.5.1-16101
- Version 3.5.1-16101 of Synology Drive Client
* Wed Apr 10 2024 Maxime Dirksen <dev@emixam.be> - 3.5.0-16084
- Version 3.5.0-16084 of Synology Drive Client
* Tue Oct 31 2023 Maxime Dirksen <dev@emixam.be> - 3.4.0-15724
- Version 3.4.0-15724 of Synology Drive Client
* Wed Oct 11 2023 Maxime Dirksen <dev@emixam.be> - 3.4.0-15721
- Version 3.4.0-15721 of Synology Drive Client
* Sat Mar 25 2023 Maxime Dirksen <dev@emixam.be> - 3.3.0-15082
- Version 3.3.0-15082 of Synology Drive Client
* Tue Dec 20 2022 Maxime Dirksen <dev@emixam.be> - 3.2.1-13271
- Version 3.2.1-13271 of Synology Drive Client
* Thu Nov 24 2022 Maxime Dirksen <dev@emixam.be> - 3.2.0-13258
- Version 3.2.0-13258 of Synology Drive Client
* Wed Oct 26 2022 Maxime Dirksen <dev@emixam.be> - 3.2.0-13238
- Version 3.2.0-13238 of Synology Drive Client
* Thu Apr 28 2022 Maxime Dirksen <dev@emixam.be> - 3.1.0-12923
- Version 3.1.0-12923 of Synology Drive Client
* Thu Apr 7 2022 Maxime Dirksen <dev@emixam.be> - 3.1.0-12920
- Version 3.1.0-12920 of Synology Drive Client
* Fri Jan 21 2022 Maxime Dirksen <dev@emixam.be> - 3.0.3-12689
- Version 3.0.3-12689 of Synology Drive Client
