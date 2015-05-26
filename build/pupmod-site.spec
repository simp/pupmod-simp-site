Summary: Site Puppet Module
Name: pupmod-site
Version: 2.0.0
Release: 3
License: Apache License 2.0
Group: Applications/System
Source: %{name}-%{version}-%{release}.tar.gz
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: puppet >= 3.3.0
Buildarch: noarch
Requires: simp-bootstrap >= 4.2.0
Obsoletes: pupmod-site-test

Prefix: /etc/puppet/environments/simp/modules

%description
This Puppet module provides a space from which to build site specific changes,
settings, and overrides.

This RPM simply sets up a blank environment from which to begin.

%prep

%build

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

mkdir -p %{buildroot}/%{prefix}/site

# Make your directories here.
mkdir -p -m 750 %{buildroot}/%{prefix}/site
mkdir -p -m 770 %{buildroot}/%{prefix}/site/files
mkdir -p -m 770 %{buildroot}/%{prefix}/site/lib
mkdir -p -m 750 %{buildroot}/%{prefix}/site/manifests
mkdir -p -m 750 %{buildroot}/%{prefix}/site/templates

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

mkdir -p %{buildroot}/%{prefix}/site

%files
%defattr(0640,root,puppet,0750)
%dir %{prefix}/site
%dir %{prefix}/site/files
%dir %{prefix}/site/lib
%dir %{prefix}/site/manifests
%dir %{prefix}/site/templates

%post

%postun
#!/bin/sh
# Post uninstall stuff

%changelog
* Mon May 25 2015 Trevor Vaughan <tvaughan@onyxpoint.com> - 2.0.0-3
- Updates for public release

* Fri Jan 16 2015 Trevor Vaughan <tvaughan@onyxpoint.com> - 2.0.0-2
- Changed puppet-server requirement to puppet

* Mon Dec 26 2011 Maintenance
2.0.0-1
- Updated the spec file to add in the 'lib' directory and set the directory
  permissions more cleanly.

* Tue Jan 11 2011 Maintenance
2.0.0-0
- Refactored for SIMP-2.0.0-alpha release

* Fri Jun 11 2010 Maintenance
1.0-0
- Stub to go along with the new simp version jump.

* Thu Feb 18 2010 Maintenance
0.1-11
- Updated the files list to explicitly name the user/group of the directories.
  For some reaons, %defattr didn't seem to carry down to them properly.

* Wed Dec 09 2009 Maintenance
0.1-10
- Forced permission and mode setting on the /etc/puppet/environments/simp/modules/site/files
  directory.
