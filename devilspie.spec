Summary: A window matching tool
Name: devilspie
Version: 0.22
Release: %mkrel 4
License: GPLv2+ and LGPLv2
Group: Graphical desktop/GNOME
URL: http://www.burtonini.com/
Source0: http://www.burtonini.com/computing/%{name}-%{version}.tar.gz
Patch0: devilspie-0.22-deprecated-gtk.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libwnck-devel
BuildRequires: libpopt-devel
BuildRequires: glib2-devel >= 2.10
BuildRequires: intltool

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

%configure2_5x

%make
%check
make check

%install
rm -rf $RPM_BUILD_ROOT %name.lang

%makeinstall_std

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog README* TODO
%{_bindir}/*
%{_mandir}/*/*


