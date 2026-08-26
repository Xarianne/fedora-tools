Name:           game-devices-udev
Version:        1.0
Release:        1%{?dist}
Summary:        Udev rules for game controllers
BuildArch:      noarch

License:        MIT
URL:            https://codeberg.org/fabiscafe/game-devices-udev
# Codeberg archives extract to "game-devices-udev" without the version number
Source0:        https://codeberg.org/fabiscafe/%{name}/archive/%{version}.tar.gz

Requires:       udev
Requires:       systemd
Requires:       filesystem

%description
A collection of udev rules for various game controllers to ensure they 
are recognized and configured correctly. This package also loads the 
uinput module at boot.

%prep
# Upstream tarball directory does not include version
%setup -q -n %{name}

%build
# Nothing to build

%install
# Install rules to /usr/lib (vendor) to avoid conflicts with /etc (admin)
install -d -m 0755 %{buildroot}%{_prefix}/lib/udev/rules.d
install -m 0644 *.rules %{buildroot}%{_prefix}/lib/udev/rules.d/

# Ensure uinput module loads on boot
install -d -m 0755 %{buildroot}%{_prefix}/lib/modules-load.d
echo "uinput" > %{buildroot}%{_prefix}/lib/modules-load.d/uinput.conf
chmod 0644 %{buildroot}%{_prefix}/lib/modules-load.d/uinput.conf

%post
/usr/bin/udevadm control --reload
/usr/bin/udevadm trigger
# Attempt to load uinput immediately, do not fail if unavailable
/usr/sbin/modprobe uinput || :

%postun
/usr/bin/udevadm control --reload
/usr/bin/udevadm trigger

%files
%license LICENSE
%doc README.md
%{_prefix}/lib/udev/rules.d/*.rules
%{_prefix}/lib/modules-load.d/uinput.conf

%changelog
%autochangelog
