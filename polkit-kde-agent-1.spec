%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)
#define git 20240222
%define gitbranch Plasma/6.0
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

Summary:	KDE Agent for PolicyKit
Name:		polkit-kde-agent-1
Version:	6.5.3
Release:	%{?git:0.%{git}.}1
License:	LGPL
Group:		System/Libraries
Url:		https://kde.org/
%if 0%{?git:1}
Source0:	https://invent.kde.org/plasma/polkit-kde-agent-1/-/archive/%{gitbranch}/polkit-kde-agent-1-%{gitbranchd}.tar.bz2#/polkit-kde-agent-1-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/plasma/%(echo %{version} |cut -d. -f1-3)/polkit-kde-agent-1-%{version}.tar.xz
%endif

BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(KF6WindowSystem)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(PolkitQt6-1)
Provides:	polkit-agent
# Renamed after 6.0 2025-05-03
%rename plasma6-polkit-kde-agent-1

BuildSystem:	cmake
BuildOption:	-DBUILD_QCH:BOOL=ON
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
KDE Agent for PolicyKit.

%files -f %{name}.lang
%{_sysconfdir}/xdg/autostart/polkit-kde-authentication-agent-1.desktop
%{_libdir}/libexec/polkit-kde-authentication-agent-1
%{_datadir}/applications/org.kde.polkit-kde-authentication-agent-1.desktop
%{_prefix}/lib/systemd/user/plasma-polkit-agent.service
%{_datadir}/knotifications6/polkit-kde-authentication-agent-1.notifyrc
