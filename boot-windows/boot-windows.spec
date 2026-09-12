Name:           boot-windows
Version:        1.5
Release:        %autorelease
Summary:        Reboot into Windows via UEFI BootNext

License:        GPL-3.0-or-later
URL:            https://github.com/Xarianne/fedora-tools
Source0:        boot-windows.sh
Source1:        boot-windows.desktop
Source2:        boot-windows.rules

BuildArch:      noarch
Requires:       efibootmgr
Requires:       zenity
Requires:       systemd
Requires:       desktop-file-utils
Requires:       libnotify
Requires:       polkit

%description
Small helper to reboot into the Windows Boot Manager entry using UEFI BootNext.

%prep
%autosetup -c -T
# Copy sources to the current build directory
cp %{SOURCE0} %{SOURCE1} %{SOURCE2} .

%build
# No build steps needed for a shell script [cite: 5]

%install
# Install the script with executable permissions
install -D -p -m 0755 boot-windows.sh %{buildroot}%{_bindir}/boot-windows

# Install the desktop entry
install -D -p -m 0644 boot-windows.desktop %{buildroot}%{_datadir}/applications/boot-windows.desktop

# Install the Polkit rules for non-interactive use
install -D -p -m 0644 boot-windows.rules %{buildroot}%{_datadir}/polkit-1/rules.d/10-boot-windows.rules

%files
%{_bindir}/boot-windows
%{_datadir}/applications/boot-windows.desktop
%{_datadir}/polkit-1/rules.d/10-boot-windows.rules

%changelog
%autochangelog