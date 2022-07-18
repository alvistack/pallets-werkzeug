%global debug_package %{nil}

Name: python-werkzeug
Epoch: 100
Version: 2.0.2
Release: 1%{?dist}
BuildArch: noarch
Summary: The comprehensive WSGI web application library
License: BSD-3-Clause
URL: https://github.com/pallets/werkzeug/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Werkzeug is a comprehensive WSGI web application library. It began as a
simple collection of various utilities for WSGI applications and has
become one of the most advanced WSGI utility libraries.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-werkzeug
Summary: The comprehensive WSGI web application library
Requires: python3
Provides: python3-werkzeug = %{epoch}:%{version}-%{release}
Provides: python3dist(werkzeug) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-werkzeug = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(werkzeug) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-werkzeug = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(werkzeug) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-werkzeug
Werkzeug is a comprehensive WSGI web application library. It began as a
simple collection of various utilities for WSGI applications and has
become one of the most advanced WSGI utility libraries.

%files -n python%{python3_version_nodots}-werkzeug
%license LICENSE.rst
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-werkzeug
Summary: The comprehensive WSGI web application library
Requires: python3
Provides: python3-werkzeug = %{epoch}:%{version}-%{release}
Provides: python3dist(werkzeug) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-werkzeug = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(werkzeug) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-werkzeug = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(werkzeug) = %{epoch}:%{version}-%{release}

%description -n python3-werkzeug
Werkzeug is a comprehensive WSGI web application library. It began as a
simple collection of various utilities for WSGI applications and has
become one of the most advanced WSGI utility libraries.

%files -n python3-werkzeug
%license LICENSE.rst
%{python3_sitelib}/*
%endif

%changelog
