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
Source5:        fedora-update-check.sh
Source6:        fedora-update-check.service
Source7:        fedora-update-check.timer

BuildArch:      noarch
BuildRequires:  systemd-rpm-macros

Requires:       dnf
Requires:       libnotify
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
# Copy sources into the build directory (like boot-windows.spec)
cp %{SOURCE0} %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} %{SOURCE7} .
find . -type f -name "*.sh" -exec sed -i 's/\r$//' {} +

%build
# nothing to build

%install
rm -rf %{buildroot}

install -D -m 0755 fedora-update.sh %{buildroot}%{_bindir}/fedora-update
install -D -m 0644 fedora-update.desktop %{buildroot}%{_datadir}/applications/fedora-update.desktop
install -D -m 0755 fedora-update-tray.py %{buildroot}%{_bindir}/fedora-update-tray
install -D -m 0644 fedora-update-tray.desktop %{buildroot}%{_datadir}/applications/fedora-update-tray.desktop
install -D -m 0644 fedora-update-tray.service %{buildroot}%{_userunitdir}/fedora-update-tray.service
install -D -m 0755 fedora-update-check.sh %{buildroot}%{_bindir}/fedora-update-check.sh
install -D -m 0644 fedora-update-check.service %{buildroot}%{_userunitdir}/fedora-update-check.service
install -D -m 0644 fedora-update-check.timer %{buildroot}%{_userunitdir}/fedora-update-check.timer

%files
%{_bindir}/fedora-update
%{_datadir}/applications/fedora-update.desktop
%{_bindir}/fedora-update-tray
%{_datadir}/applications/fedora-update-tray.desktop
%{_bindir}/fedora-update-check.sh
%{_userunitdir}/fedora-update-tray.service
%{_userunitdir}/fedora-update-check.service
%{_userunitdir}/fedora-update-check.timer

%changelog
%autochangelog
