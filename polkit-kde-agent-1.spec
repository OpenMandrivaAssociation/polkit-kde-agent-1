%define         svn  1056463

Name:           polkit-kde-1
Version:        0.95.1
Summary:        Library that allows developer to access PolicyKit-1 API
Release:        %mkrel 3
License:        GPL
Group:          Graphical desktop/KDE
URL:            http://www.kde.org/
Source0:        %{name}-%{version}.tar.bz2
Patch0:         polkit-kde-1-0.95.1-add-fr-translations.patch
BuildRoot:      %_tmppath/%name-%version-%release-buildroot
BuildRequires:  polkit-qt-1-devel >= 0.95.1
BUildRequires:  kdelibs4-devel
Provides:       polkit-agent

%description
Polkit-kde-1 is a library that allows developer to access PolicyKit-1
API with a nice Qt-style API

%files -f polkit-kde-authentication-agent-1.lang
%defattr(-,root,root)
%{_kde_sysconfdir}/xdg/autostart/polkit-kde-authentication-agent-1.desktop
%{_kde_libdir}/kde4/libexec/polkit-kde-authentication-agent-1

#-----------------------------------------------------------------------------

%prep
%setup -q -n %name-%version
%patch0 -p0

%build

%cmake_qt4
%make


%install
rm -rf %buildroot
%makeinstall_std -C build
%find_lang polkit-kde-authentication-agent-1

%clean
rm -rf %{buildroot}

