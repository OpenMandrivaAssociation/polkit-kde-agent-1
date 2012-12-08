Name:           polkit-kde-agent-1
Version:        0.99.0
Summary:        PolicyKit authentication agent for KDE
Release:        6
License:        GPL
Group:          Graphical desktop/KDE
URL:            https://projects.kde.org/projects/extragear/base/%{name}
Source0:        http://fr2.rpmfind.net/linux/KDE/stable/apps/KDE4.x/admin/%{name}-%{version}.tar.bz2
# upstream patches
# (bor) make sure dialogue is not hidden (GIT)
Patch100:	0001-Bring-the-auth-dialog-to-the-front-when-it-is-shown..patch
Patch101:	polkit-kde-agent-1-0.99.0-l10n-ru.patch
BuildRequires:  polkit-qt-1-devel >= 0.99.0
BuildRequires:  kdelibs4-devel
Provides:       polkit-agent
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
%setup -q -n %{name}-%{version}
%apply_patches

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%find_lang polkit-kde-authentication-agent-1


%changelog
* Mon Apr 16 2012 Mikhail Kompaniets <mkompan@mezon.ru> 0.99.0-5
- Updated Russian Translation

* Fri Apr 15 2011 Eugeni Dodonov <eugeni@mandriva.com> 0.99.0-3mdv2011.0
+ Revision: 653196
- Bump release

* Sat Feb 26 2011 Andrey Borzenkov <arvidjaar@mandriva.org> 0.99.0-2
+ Revision: 640111
- P100: fix "invisible" dialogue (GIT)

* Fri Dec 10 2010 Funda Wang <fwang@mandriva.org> 0.99.0-1mdv2011.0
+ Revision: 620236
- shouldusing kde4 cmake macro
- new version 0.99.0

* Sun Nov 21 2010 Andrey Borzenkov <arvidjaar@mandriva.org> 0.97.1-0.2mdv2011.0
+ Revision: 599348
- using GIT hash in version number was bad idea

* Sat Nov 20 2010 Andrey Borzenkov <arvidjaar@mandriva.org> 0.97.1-0.g99d1369a.1mdv2011.0
+ Revision: 599298
- update to GIT snapshot that builds and works under current KDE
- new name polkit-kde-agent-1

* Tue May 11 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.95.1-3mdv2010.1
+ Revision: 544536
- Add french translation

* Wed Apr 28 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.95.1-2mdv2010.1
+ Revision: 540132
- provides polkit-agent

* Wed Dec 23 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.95.1-1mdv2010.1
+ Revision: 481785
- Fix buildrequires
- Fix BuildRequire
- import polkit-kde-1

