Name:		highlight
Summary:	Universal source code to formatted text converter
Version:	3.6
Release:	%mkrel 1
Group:		Development/Other
License:	GPLv3
URL:		http://www.andre-simon.de/
Source0:	http://www.andre-simon.de/zip/%{name}-%{version}.tar.bz2
BuildRequires:	qt4-devel
BuildRequires:	lua-devel
BuildRequires:	boost-devel
BuildRequires:	desktop-file-utils
Buildroot:	%{_tmppath}/%{name}-%{version}-root

%description
A utility that converts sourcecode to HTML, XHTML, RTF, LaTeX, TeX,
XSL-FO, XML or ANSI escape sequences with syntax highlighting.
It supports several programming and markup languages.
Language descriptions are configurable and support regular expressions.
The utility offers indentation and reformatting capabilities.
It is easily possible to create new language definitions and colour themes.

%package gui
Summary:	GUI for the hihghlight source code formatter
Requires:	%{name} = %{version}-%{release}

%description gui
A Qt-based GUI for the highlight source code formatter source.

%prep
%setup -q

%build
%make
%__rm -rf src/gui-qt/moc*
%make gui


%install
%__rm -rf %{buildroot}
%makeinstall_std

%__mkdir_p %{buildroot}%{_datadir}/applications
%__mkdir_p %{buildroot}%{_datadir}/pixmaps

%make install-gui DESTDIR=%{buildroot}

%__rm -rf %{buildroot}%{_docdir}/%{name}/

desktop-file-install \
    --dir %{buildroot}%{_datadir}/applications \
   highlight.desktop

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc ChangeLog AUTHORS README* TODO examples/
%{_bindir}/highlight
%{_datadir}/highlight/
%{_mandir}/man1/highlight.1*
%config(noreplace) %{_sysconfdir}/highlight/

%files gui
%defattr(-,root,root,-)
%{_bindir}/highlight-gui
%{_datadir}/applications/highlight.desktop
%{_datadir}/pixmaps/highlight.xpm



%changelog
* Wed Dec 07 2011 Andrey Bondrov <abondrov@mandriva.org> 3.6-1mdv2011.0
+ Revision: 738601
- imported package highlight

