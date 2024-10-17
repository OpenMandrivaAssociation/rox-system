%define oname system
%define roxname System
%define roxdir %_prefix/lib/apps

Name:		rox-system
Version:	1.9.1
Release:	8
Summary:	System monitor for the ROX graphical desktop
Group:		Graphical desktop/Other
License:	GPL
URL:		https://rox.sourceforge.net/system.html
Source:		http://prdownloads.sourceforge.net/%{name}/%{oname}-%{version}.tar.bz2
Requires:	rox-lib >= 1.9.9
Requires:	python-ctypes
BuildArch:	noarch

%description
System displays information about your system - what processes are running
and the amount of memory they are using, as well as free and used disk space.
It can also be useful for quitting crashed applications.

%prep
%setup -q -n %{oname}-%{version}

%build
cd %{roxname}/Messages
./dist
rm -f *.old

%install
mkdir -p %{buildroot}%{roxdir}
cp -a %{roxname} %{buildroot}%{roxdir}
rm -rf %{buildroot}%{roxdir}/%{roxname}/CVS \
	%{buildroot}%{roxdir}/%{roxname}/Help/CVS \
    %{buildroot}%{roxdir}/%{roxname}/Messages/dist \
    %{buildroot}%{roxdir}/%{roxname}/Messages/*po

for gmo in %{buildroot}%{roxdir}/%{roxname}/Messages/*.gmo;do
echo "%lang($(basename $gmo|sed s/.gmo//)) $(echo $gmo|sed s!%{buildroot}!!)" >> %{name}.lang
done

%files -f %{name}.lang
%doc %{roxdir}/%{roxname}/Help
%dir %{roxdir}/%{roxname}
%dir %{roxdir}/%{roxname}/Messages
%{roxdir}/%{roxname}/.DirIcon
%{roxdir}/%{roxname}/*.py
%{roxdir}/%{roxname}/AppRun
%attr(644,root,root) %{roxdir}/%{roxname}/*.xml
%{roxdir}/%{roxname}/images

