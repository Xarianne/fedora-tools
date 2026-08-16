Name:           starship
Version:        1.26.0
Release:        %autorelease
Summary:        The minimal, blazing-fast, and infinitely customizable prompt

License:        ISC
URL:            https://starship.rs
Source0:        https://github.com/starship/starship/archive/refs/tags/v%{version}/starship-%{version}.tar.gz

BuildRequires:  cargo-rpm-macros

%description
Starship is a minimal, fast, and infinitely customizable prompt for any shell.

%prep
%autosetup -n starship-%{version}
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%files
%license LICENSE
%doc README.md
%{_bindir}/starship

%changelog
%autochangelog
