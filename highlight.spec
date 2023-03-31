Summary:	Universal source code to formatted text converter
Name:		highlight
Version:	3.57
Release:	2
Group:		Development/Other
License:	GPLv3
Url:		http://www.andre-simon.de/
Source0:	http://www.andre-simon.de/zip/%{name}-%{version}.tar.bz2
Source100:	highlight.rpmlintrc

BuildRequires:	desktop-file-utils
BuildRequires:	boost-devel
BuildRequires:	cmake(ECM)
BuildRequires:	qt5-devel
BuildRequires:	pkgconfig(lua)

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
%make CXX=%{__cxx}
rm -rf src/gui-qt/moc*
%make gui QMAKE=%{_qt5_bindir}/qmake

%install
%makeinstall_std

mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/pixmaps

%make install-gui DESTDIR=%{buildroot} 

rm -rf %{buildroot}%{_docdir}/%{name}/

desktop-file-install \
	--dir %{buildroot}%{_datadir}/applications \
	highlight.desktop

%files
%doc AUTHORS README* 
%{_bindir}/highlight
%{_datadir}/highlight/
%{_mandir}/man1/highlight.1*
%{_mandir}/man5/filetypes.conf.5.*
%config(noreplace) %{_sysconfdir}/highlight/

%files gui
%{_bindir}/highlight-gui
%{_datadir}/applications/highlight.desktop
%{_datadir}/pixmaps/highlight.xpm
