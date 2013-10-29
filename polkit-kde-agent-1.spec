Summary:	PolicyKit authentication agent for KDE
Name:		polkit-kde-agent-1
Version:	0.99.0
Release:	6
License:	GPLv2
Group:		Graphical desktop/KDE
Url:		https://projects.kde.org/projects/extragear/base/%{name}
Source0:	http://fr2.rpmfind.net/linux/KDE/stable/apps/KDE4.x/admin/%{name}-%{version}.tar.bz2
# upstream patches
# (bor) make sure dialogue is not hidden (GIT)
Patch100:	0001-Bring-the-auth-dialog-to-the-front-when-it-is-shown..patch
Patch101:	polkit-kde-agent-1-0.99.0-l10n-ru.patch
BuildRequires:	kdelibs4-devel
BuildRequires:	pkgconfig(polkit-qt-1)
Provides:	polkit-agent
Provides:	polkit-kde-1

%description
PolicyKit authentication agent for KDE

%files -f polkit-kde-authentication-agent-1.lang
%dir %{_kde_appsdir}/policykit1-kde
%{_kde_appsdir}/policykit1-kde/policykit1-kde.notifyrc
%{_kde_autostart}/polkit-kde-authentication-agent-1.desktop
%{_kde_libdir}/kde4/libexec/polkit-kde-authentication-agent-1

#-----------------------------------------------------------------------------

%prep
%setup -q
%apply_patches

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%find_lang polkit-kde-authentication-agent-1

