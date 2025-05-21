%global debug_package %{nil}

Name:           zellij
Version:        0.42.2
Release:        1%{?dist}
Summary:        A terminal workspace with batteries included
Group:          Applications/System
License:        MIT
URL:            https://github.com/zellij-org/%{name}
BuildRequires:  cmake, openssl-devel, perl
Source:         https://github.com/zellij-org/%{name}/archive/refs/tags/v%{version}.tar.gz

%{?el7:BuildRequires: cargo, rust}

%description
Zellij is a workspace aimed at developers, ops-oriented people and anyone
who loves the terminal. Similar programs are sometimes called "Terminal Multiplexers".

%prep
%setup -q -n %{name}-%{version}

%build
cargo build --release

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/bin
cp target/release/%{name} %{buildroot}/usr/bin/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/usr/bin/%{name}

%changelog
* Wed May 21 2025 Jamie Curnow <jc@jc21.com> - 0.42.2-1
- https://github.com/zellij-org/zellij/releases/tag/v0.42.2
