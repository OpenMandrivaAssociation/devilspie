Summary:	A window matching tool
Name:		devilspie
Version:	0.23
Release:	1
License:	GPLv2+
Group:		Graphical desktop/GNOME
Url:		http://www.burtonini.com/
Source0:	http://www.burtonini.com/computing/%{name}-%{version}.tar.xz
# Debian patchset
Patch0:		fix_manpage_lintian_warnings.patch
Patch1:		fix_memleak_in_my_wnck_get_viewport_start.patch
Patch2:		fix_using_deprecated_wnck_functions.patch
Patch3:		remove_unavailable_options_from_manpage.patch
BuildRequires:	intltool
BuildRequires:	pkgconfig(gdk-3.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libwnck-3.0)
BuildRequires:	pkgconfig(x11)

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

%files -f %{name}.lang
%doc AUTHORS ChangeLog README* TODO
%{_bindir}/*
%{_mandir}/*/*

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%configure2_5x
%make

%check
make check

%install
%makeinstall_std

%find_lang %{name}

