Name:           polkit-kde-agent-1
Version:        0.99.0
Summary:        PolicyKit authentication agent for KDE
Release:        %mkrel 1
License:        GPL
Group:          Graphical desktop/KDE
URL:            https://projects.kde.org/projects/extragear/base/%{name}
Source0:        http://fr2.rpmfind.net/linux/KDE/stable/apps/KDE4.x/admin/%{name}-%{version}.tar.bz2
BuildRoot:      %_tmppath/%name-%version-%release-buildroot
BuildRequires:  polkit-qt-1-devel >= 0.99.0
BuildRequires:  kdelibs4-devel
Provides:       polkit-agent
Provides:	polkit-kde-1
Obsoletes:	polkit-kde-1

%description
PolicyKit authentication agent for KDE

%files -f polkit-kde-authentication-agent-1.lang
%defattr(-,root,root)
%dir %{_kde_appsdir}/policykit1-kde
%{_kde_appsdir}/policykit1-kde/policykit1-kde.notifyrc
%{_kde_autostart}/polkit-kde-authentication-agent-1.desktop
%{_kde_libdir}/kde4/libexec/polkit-kde-authentication-agent-1

#-----------------------------------------------------------------------------

%prep
%setup -q -n %name-%version

%build
%cmake_kde4
%make

%install
rm -rf %buildroot
%makeinstall_std -C build
%find_lang polkit-kde-authentication-agent-1

%clean
rm -rf %{buildroot}

