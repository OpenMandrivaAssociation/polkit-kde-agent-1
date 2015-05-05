%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	KDE Agent for PolicyKit
Name:		polkit-kde-agent-1
Version:	5.3.0
Release:	1
License:	LGPL
Group:		System/Libraries
Url:		http://kde.org/
Source0:	ftp://ftp.kde.org/pub/kde/%{stable}/plasma/%{version}/%{name}-%{version}.tar.xz

BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(PolkitQt5-1)
BuildRequires:	qt5-devel
BuildRequires:	cmake
BuildRequires:	ninja

%description
KDE Agent for PolicyKit

%files -f polkit-kde-authentication-agent-1.lang
%{_sysconfdir}/xdg/autostart/polkit-kde-authentication-agent-1.desktop
%{_libdir}/libexec/polkit-kde-authentication-agent-1
%{_datadir}/knotifications5/policykit1-kde.notifyrc

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
ninja

%install
DESTDIR="%{buildroot}" ninja -C build install
%find_lang polkit-kde-authentication-agent-1
