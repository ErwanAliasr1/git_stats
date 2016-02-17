%{?!_licensedir:%global license %%doc}
%{!?upstream_version: %global upstream_version %{version}}

Name:           git_stats
Summary:        A tool to report stats about a git repo
Version:        0.0.1.dev9
Release:        1%{?dist}
License:        ASL 2.0
#URL:            https://pypi.python.org/pypi/hardware

Source0:        %{name}-%{upstream_version}.tar.gz

BuildArch:      noarch
BuildRequires:  python-setuptools
BuildRequires:  python2-devel
BuildRequires:  python-pbr
BuildRequires:  git
Requires: numpy
Requires: python-pbr


%prep
%autosetup -S git -v -n git_stats-%{upstream_version}
rm -rf *.egg-info

find -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python2}|'

%build
%{__python2} setup.py build
rm -rf doc/build/html/.buildinfo

%install
%{__python2} setup.py install -O1 --skip-build --root=%{buildroot}


%description
Tooling to report basic information about a git repository hosted on github:
- Meaning time between commit
- Top <n> contributors

%package doc
Summary:    Documentation for git_stats
Group:      Documentation

%description doc
Documentation for git_stats


%files
%license LICENSE
%doc README.rst
%{python2_sitelib}/%{name}/*
%exclude %{python2_sitelib}/%{name}/test*
%exclude %{python2_sitelib}/%{name}-*
%{_bindir}/git_stats

%files doc
%license LICENSE

%changelog
* Tue Feb 17 2016 Erwan Velu <erwan@redhat.com> 0.1
- Initial package build

