Name:           goose
Version:        1.47.0
Release:        %autorelease
Summary:        Goose AI agent desktop application

License:        Apache-2.0
URL:            https://goose-docs.ai/
Source0:        https://github.com/aaif-goose/goose/releases/download/v%{version}/Goose-%{version}-1.x86_64.rpm

BuildArch:      x86_64

BuildRequires:  rpm-build
BuildRequires:  cpio

# Runtime dependencies for the Electron-based desktop app
Requires:       nspr
Requires:       nss
Requires:       atk
Requires:       at-spi2-atk
Requires:       gtk3
Requires:       mesa-libgbm
Requires:       libxkbcommon
Requires:       alsa-lib
Requires:       libdrm
Requires:       vulkan-loader

%description
Goose is an open source AI agent that goes beyond code suggestions,
tackles bugs, and works with your favorite tools.

This package repackages the upstream prebuilt RPM for distribution via COPR.

%prep

%build

%install
mkdir -p %{buildroot}
cd %{buildroot}
rpm2cpio %{SOURCE0} | cpio -idmv

%files
%{_bindir}/Goose
%{_libdir}/Goose/
%{_datadir}/applications/Goose.desktop
%{_datadir}/pixmaps/Goose.png
%{_datadir}/doc/Goose/

%changelog
%autochangelog