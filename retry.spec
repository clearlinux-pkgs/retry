#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : retry
Version  : 0.9.2
Release  : 1
URL      : https://files.pythonhosted.org/packages/9d/72/75d0b85443fbc8d9f38d08d2b1b67cc184ce35280e4a3813cda2f445f3a4/retry-0.9.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/9d/72/75d0b85443fbc8d9f38d08d2b1b67cc184ce35280e4a3813cda2f445f3a4/retry-0.9.2.tar.gz
Summary  : Easy to use retry decorator.
Group    : Development/Tools
License  : Apache-2.0
Requires: retry-license = %{version}-%{release}
Requires: retry-python = %{version}-%{release}
Requires: retry-python3 = %{version}-%{release}
Requires: decorator
Requires: py
BuildRequires : buildreq-distutils3
BuildRequires : decorator
BuildRequires : pbr
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-mock
BuildRequires : tox
BuildRequires : virtualenv
BuildRequires : wheel

%description
=====

%package license
Summary: license components for the retry package.
Group: Default

%description license
license components for the retry package.


%package python
Summary: python components for the retry package.
Group: Default
Requires: retry-python3 = %{version}-%{release}

%description python
python components for the retry package.


%package python3
Summary: python3 components for the retry package.
Group: Default
Requires: python3-core

%description python3
python3 components for the retry package.


%prep
%setup -q -n retry-0.9.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1546112062
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 setup.py test
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/retry
cp LICENSE %{buildroot}/usr/share/package-licenses/retry/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/retry/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
