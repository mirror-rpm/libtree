%global debug_package %{nil}

Name:           libtree
Version:        1.0
Release:        3%{?dist}
Summary:        Implementation of AVL (Adelson-Velskii and Landis) balanced trees

License:        MIT
URL:            https://piumarta.com/software/tree/
Source0:        %{url}/tree-%{version}.tar.gz

%define common_desc tree.h Implementation of AVL (Adelson-Velskii and Landis) \
balanced trees in the spirit of the BSD queue and list implementations.

%description
%{common_desc}

%package  devel
Summary:  %{summary}
Provides: libtree-static = %{version}-%{release}

%description devel
%{common_desc}

%prep
%autosetup -n tree-%{version}

%build

%install
mkdir -p %{buildroot}%{_includedir}
install -p -m 644 tree.h %{buildroot}%{_includedir}

%files devel
%{_includedir}/tree.h

%changelog
* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Mar 20 2021 Timothée Floure <fnux@fedoraproject.org> - 1.0-1
- Let there be package.
