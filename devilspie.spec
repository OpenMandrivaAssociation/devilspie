Summary: A window matching tool
Name: devilspie
Version: 0.22
Release: 5
License: GPLv2+ and LGPLv2
Group: Graphical desktop/GNOME
URL: http://www.burtonini.com/
Source0: http://www.burtonini.com/computing/%{name}-%{version}.tar.gz
Patch0: devilspie-0.22-deprecated-gtk.patch
BuildRequires: libwnck-devel
BuildRequires: popt-devel
BuildRequires: glib2-devel >= 2.10
BuildRequires: intltool
BuildRequires: gnome-common
BuildRequires: pkgconfig(x11)

%description
A window-matching utility, inspired by Sawfish's "Matched Windows" option and
the lack of the functionality in Metacity. Metacity lacking window matching is
not a bad thing -- Metacity is a lean window manager, and window matching does
not have to be a window manager task.

Devil's Pie can be configured to detect windows as they are created, and match
the window to a set of rules. If the window matches the rules, it can perform a
series of actions on that window. For example, I make all windows created by
X-Chat appear on all workspaces, and the main Gkrellm1 window does not appear
in the pager or task list.

%prep
%setup -q
%apply_patches
autoreconf
cat > README.upgrade.urpmi <<EOF
Starting in 0.13-1mdk the configuration format has changed. Please read the
documentation about how to create the new rules.
EOF

%build
export LDFLAGS="-lX11"
%configure2_5x

%make

%check
make check

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog README* TODO
%{_bindir}/*
%{_mandir}/*/*




%changelog
* Sat Jul 30 2011 GÃ¶tz Waschk <waschk@mandriva.org> 0.22-4mdv2012.0
+ Revision: 692408
- update build dep
- fix build
- update license

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.22-3mdv2011.0
+ Revision: 244073
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sat Nov 24 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.22-1mdv2008.1
+ Revision: 111779
- new version

* Fri Nov 09 2007 JÃ©rÃ´me Soyer <saispo@mandriva.org> 0.21-1mdv2008.1
+ Revision: 107065
- New release


* Mon Jan 29 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.20.2-1mdv2007.0
+ Revision: 114832
- new version

* Fri Jan 12 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.20.1-1mdv2007.1
+ Revision: 108098
- new version
- reenable checks

* Fri Jan 12 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.20-1mdv2007.1
+ Revision: 108079
- new version
- disable checks as they are known to fail at the moment

* Fri Dec 01 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.19-1mdv2007.1
+ Revision: 89853
- new version

* Sat Oct 21 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.18-1mdv2007.0
+ Revision: 71574
- Import devilspie

* Sat Oct 21 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.18-1mdv2007.1
- New version 0.18

* Tue Apr 11 2006 Götz Waschk <waschk@mandriva.org> 0.17.1-1mdk
- New release 0.17.1
- depend on new glib
- use mkrel

* Mon Feb 06 2006 Jerome Soyer <saispo@mandriva.org> 0.16-1mdk
- New release 0.16

* Tue Oct 18 2005 GÃ¶tz Waschk <waschk@mandriva.org> 0.14-1mdk
- New release 0.14

* Thu Oct 13 2005 GÃ¶tz Waschk <waschk@mandriva.org> 0.13-3mdk
- rebuild for new libwnck

* Wed Sep 28 2005 Götz Waschk <waschk@mandriva.org> 0.13-2mdk
- add a note about the changed configuration format

* Wed Sep 28 2005 Götz Waschk <waschk@mandriva.org> 0.13-1mdk
- enable check
- update file list
- New release 0.13

* Sat Sep 17 2005 Götz Waschk <waschk@mandriva.org> 0.11-2mdk
- update docs, thanks to John Keller

* Sat Sep 17 2005 GÃ¶tz Waschk <waschk@mandriva.org> 0.11-1mdk
- New release 0.11

* Wed May 25 2005 Götz Waschk <waschk@mandriva.org> 0.10-3mdk
- fix buildrequires again

* Tue May 24 2005 Götz Waschk <waschk@mandriva.org> 0.10-2mdk
- fix buildrequires

* Sat May 21 2005 Frederic Crozat <fcrozat@mandrakesoft.com> 0.10-1mdk
- New release 0.10

* Tue Feb 08 2005 Jerome Soyer <saispo@mandrake.org> 0.8-1mdk
- New release 0.8

* Mon Sep 20 2004 Goetz Waschk <waschk@linux-mandrake.com> 0.7-1mdk
- New release 0.7

* Mon Aug 30 2004 Jerome Soyer <saispo@mandrake.org> 0.5.1-1mdk
- New release 0.5.1

* Thu Jun 10 2004 <fcrozat@mandrakesoft.com> 0.4-1mdk
- New release 0.4

