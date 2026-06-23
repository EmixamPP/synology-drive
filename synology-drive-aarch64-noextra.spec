%global synology_version 4.0.3
%global synology_release 17892

Name:      synology-drive-noextra
Version:   %{synology_version}
Release:   %{synology_release}%{?dist}
Summary:   Unofficial RPM build of Synology Drive Client without extra dependencies
License:   Multiple, see https://www.synology.com/en-global/company/legal/terms_EULA
URL:       https://www.synology.com/

Source0: https://global.synologydownload.com/download/Utility/SynologyDriveClient/%{synology_version}-%{synology_release}/Ubuntu/Installer/synology-drive-client-%{synology_release}.x86_64.deb

AutoReqProv: no
Requires: glibc
Requires: glib2
Requires: gtk2
Requires: fex-emu
Requires: fex-emu-rootfs-fedora

Conflicts: synology-drive

%description
Synology Drive Client allows you to sync your computers with Synology NAS and back up the computer to the NAS.

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

# nautilus (installed in case the user wants to use Nautilus)
mkdir -p %{buildroot}%{_libdir}/nautilus/extensions-3.0/
install -Dm 644 usr/lib/nautilus/extensions-3.0/libnautilus-drive-extension.so -t %{buildroot}%{_libdir}/nautilus/extensions-3.0/
mkdir -p %{buildroot}%{_libdir}/nautilus/extensions-4/
install -Dm 644 usr/lib/nautilus/extensions-4/libnautilus-drive-extension-4.so -t %{buildroot}%{_libdir}/nautilus/extensions-4/

# desktop
mkdir -p %{buildroot}%{_datarootdir}/applications/
install -Dm 644 usr/share/applications/synology-drive.desktop -t %{buildroot}%{_datarootdir}/applications/
mkdir -p %{buildroot}%{_datarootdir}/icons/
cp -rp usr/share/icons/hicolor/ %{buildroot}%{_datarootdir}/icons/

# fex
mkdir -p %{buildroot}/usr/share/fex-emu/
cat << EOF > %{buildroot}/usr/share/fex-emu/Config.json
{"Config":{"ExtendedVolatileMetadata":"","NeedsSeccomp":"0","ServerSocketPath":"","MonoHacks":"1","StartupSleepProcName":"","StartupSleep":"0","HideHypervisorBit":"0","StallProcess":"0","X87ReducedPrecision":"0","VolatileMetadata":"1","KernelUnalignedAtomicBackpatching":"1","StrictInProcessSplitLocks":"0","HalfBarrierTSOEnabled":"1","MemcpySetTSOEnabled":"0","VectorTSOEnabled":"0","TSOEnabled":"1","SMCChecks":"1","EnableGpuvisProfiling":"0","ProfileStats":"0","TelemetryDirectory":"","OutputLog":"server","SilentLog":"1","DisableTelemetry":"0","ForceSVEWidth":"0","ThunkConfig":"","ThunkGuestLibs":"\/usr\/share\/fex-emu\/GuestThunks","ThunkHostLibs":"\/usr\/lib64\/fex-emu\/HostThunks","RootFS":"\/usr\/share\/fex-emu\/RootFS\/default.erofs","CPUFeatureRegisters":"","HideHybrid":"1","SmallTSCScale":"1","HostFeatures":"0","EnableCodeCacheValidation":"0","DisableL2Cache":"0","EnableCodeCachingWIP":"0","X86Disassemble":"0","DISABLE_VIXL_INDIRECT_RUNTIME_CALLS":"1","MaxInst":"5000","Disassemble":"0","Multiblock":"1","InjectLibSegFault":"0","DynamicL1Cache":"0","DynamicL1CacheIncreaseCountHeuristic":"250","DynamicL1CacheDecreaseCountHeuristic":"50","SingleStep":"0","GdbServer":"0","DumpIR":"no","PassManagerDumpIR":"0","DumpGPRs":"0","O0":"0","GlobalJITNaming":"0","LibraryJITNaming":"0","BlockJITNaming":"0","GDBSymbols":"0"},"ThunksDB":{"fex_thunk_test":0,"asound":0,"drm":0,"Vulkan":0,"WaylandClient":0,"GL":0}}
EOF

mkdir -p %{buildroot}/usr/lib/binfmt.d/
cat << EOF > %{buildroot}/usr/lib/binfmt.d/synology-drive.conf
:synology-drive:M:0:\x7fELF\x02\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x3e\x00:\xff\xff\xff\xff\xff\xfe\xfe\x00\x00\x00\x00\xff\xff\xff\xff\xff\xfe\xff\xff\xff:/usr/bin/FEX:POCF
EOF

%files
%license opt/Synology/SynologyDrive/LICENSE.txt
%doc usr/share/doc/synology-drive/changelog.gz

/opt/Synology/SynologyDrive/
%{_bindir}/synology-drive
%{_libdir}/nautilus/extensions-3.0/libnautilus-drive-extension.so
%{_libdir}/nautilus/extensions-4/libnautilus-drive-extension-4.so
%{_datarootdir}/applications/synology-drive.desktop
%{_datarootdir}/icons/hicolor/16x16/apps/synology-drive.png
%{_datarootdir}/icons/hicolor/24x24/apps/synology-drive.png
%{_datarootdir}/icons/hicolor/32x32/apps/synology-drive.png
%{_datarootdir}/icons/hicolor/48x48/apps/synology-drive.png
%{_datarootdir}/icons/hicolor/64x64/apps/synology-drive.png
%{_datarootdir}/icons/hicolor/128x128/apps/synology-drive.png
%{_datarootdir}/icons/hicolor/256x256/apps/synology-drive.png
%{_datarootdir}/icons/hicolor/512x512/apps/synology-drive.png
/usr/share/fex-emu/Config.json
/usr/lib/binfmt.d/synology-drive.conf

%changelog
* Sat Jun 06 2026 Michael Leithold <dMichael.Leithold@web.de> - 4.0.3-17892
- Version 4.0.3-17892 of Synology Drive Client
* Sat Apr 11 2026 Michael Leithold <Michael.Leithold@web.de> - 4.0.2-17889
- Version 4.0.2-17889 for Aarch64
* Fri Jan 23 2026 Maxime Dirksen <dev@emixam.be> - 4.0.2-17889
- Version 4.0.2-17889 of Synology Drive Client
