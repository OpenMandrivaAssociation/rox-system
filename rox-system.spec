%define oname system
%define roxname System
%define version 1.9.1
%define name rox-system
%define roxdir %_prefix/lib/apps

Name:		%name
Version:	%version
Release:	%mkrel 5
Summary:	System monitor for the ROX graphical desktop
Group:		Graphical desktop/Other
License:	GPL
URL:		http://rox.sourceforge.net/system.html
Source:		http://prdownloads.sourceforge.net/%{name}/%{oname}-%version.tar.bz2
Requires:	rox-lib >= 1.9.9
Requires:	python-ctypes
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildArch:	noarch

%description
System displays information about your system - what processes are running
and the amount of memory they are using, as well as free and used disk space.
It can also be useful for quitting crashed applications.

%prep
%setup -q -n %oname-%version

%build
cd %roxname/Messages
./dist
rm -f *.old

%install
rm -rf $RPM_BUILD_ROOT %name.lang
mkdir -p $RPM_BUILD_ROOT%roxdir
cp -a %roxname $RPM_BUILD_ROOT%roxdir
rm -rf %buildroot%roxdir/%roxname/CVS %buildroot%roxdir/%roxname/Help/CVS %buildroot%roxdir/%roxname/Messages/dist %buildroot%roxdir/%roxname/Messages/*po

for gmo in %buildroot%roxdir/%roxname/Messages/*.gmo;do
echo "%lang($(basename $gmo|sed s/.gmo//)) $(echo $gmo|sed s!%buildroot!!)" >> %name.lang
done

%clean
rm -rf $RPM_BUILD_ROOT


%files -f %name.lang
%defattr (-,root,root)
%doc %roxdir/%roxname/Help
%dir %roxdir/%roxname
%dir %roxdir/%roxname/Messages
%roxdir/%roxname/.DirIcon
%roxdir/%roxname/*.py
%roxdir/%roxname/App*
%attr(644,root,root) %roxdir/%roxname/*.xml
%roxdir/%roxname/images

