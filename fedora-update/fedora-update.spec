Name:           fedora-update
Version:        1.5
Release:        %autorelease
Summary:        Interactive DNF update and cleanup helper

License:        GPL-3.0-or-later
URL:            https://github.com/Xarianne/fedora-tools
Source0:        fedora-update.sh
Source1:        fedora-update.desktop
Source2:        fedora-update-tray.py
Source3:        fedora-update-tray.desktop
Source4:        fedora-update-tray.service
Source5:        fedora-updates.png
Source6:        fedora-update-check.sh
Source7:        fedora-update-check.service
Source8:        fedora-update-check.timer

BuildArch:      noarch
BuildRequires:  systemd-rpm-macros

Requires:       dnf
Requires:       python3
Requires:       python3-pystray
Requires:       python3-pillow
Requires:       xdg-terminal-exec

%description
Interactive helper that checks for updates, runs dnf upgrade, autoremove
and cache cleanup, accessible from the desktop menu, plus an optional
tray helper that periodically checks for updates.

%prep
%autosetup -c -T
find . -type f -name "*.sh" -exec sed -i 's/\r$//' {} +

%build
# nothing to build

%install
rm -rf %{buildroot}

install -D -m 0755 %{SOURCE0} %{buildroot}%{_bindir}/fedora-update
install -D -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/applications/fedora-update.desktop
install -D -m 0755 %{SOURCE2} %{buildroot}%{_bindir}/fedora-update-tray
install -D -m 0644 %{SOURCE3} %{buildroot}%{_datadir}/applications/fedora-update-tray.desktop
install -D -m 0644 %{SOURCE4} %{buildroot}%{_userunitdir}/fedora-update-tray.service
install -D -m 0644 %{SOURCE5} %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/fedora-updates.png
install -D -m 0755 %{SOURCE6} %{buildroot}%{_bindir}/fedora-update-check.sh
install -D -m 0644 %{SOURCE7} %{buildroot}%{_userunitdir}/fedora-update-check.service
install -D -m 0644 %{SOURCE8} %{buildroot}%{_userunitdir}/fedora-update-check.timer

%files
%{_bindir}/fedora-update
%{_datadir}/applications/fedora-update.desktop
%{_bindir}/fedora-update-tray
%{_datadir}/applications/fedora-update-tray.desktop
%{_bindir}/fedora-update-check.sh
%{_userunitdir}/fedora-update-tray.service
%{_userunitdir}/fedora-update-check.service
%{_userunitdir}/fedora-update-check.timer
%{_datadir}/icons/hicolor/32x32/apps/fedora-updates.png

%changelog
%autochangelog
