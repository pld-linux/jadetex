Summary:	LaTeX macros for converting Jade TeX output into DVI/PS/PDF
Summary(pl):	Makra LaTeX do konwersji Jade Tex do DVI/PS/PDF
Name:		jadetex
Version:	3.12
Release:	5
License:	Copyright (C) 1995,1996,1997,1998,1999,2000,2001 Sebastian Rahtz <s.rahtz@elsevier.co.uk>
Group:		Applications/Publishing/SGML
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch1:		%{name}-latin2.patch
URL:		http://jadetex.sourceforge.net/
Requires:	tetex-pdftex
BuildRequires:	tetex-csplain
BuildRequires:	tetex-fonts-cmcyr
BuildRequires:	tetex-fonts-jknappen
BuildRequires:	tetex-format-latex
BuildRequires:	tetex-format-pdflatex
BuildRequires:	tetex-format-pdftex
BuildRequires:	tetex-format-plain
BuildRequires:	tetex-latex-ams
BuildRequires:	tetex-latex-carlisle
BuildRequires:	tetex-latex-cyrillic
BuildRequires:	tetex-latex-psnfss
BuildRequires:	tetex-metafont
BuildRequires:	tetex-pdftex
BuildRequires:	tetex-tex-babel
BuildRequires:	tetex-tex-ruhyphen
BuildRequires:	tetex-tex-ukrhyph
PreReq:		sh-utils
Requires:	sgml-common
%requires_eq	tetex
%requires_eq	tetex-latex
Autoreqprov:	no
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JadeTeX contains the additional LaTeX macros necessary for taking Jade
TeX output files and processing them as LaTeX files.

%description -l pl
JadeTeX zawiera dodatkowe makra LaTeX potrzebne do konwersji plików
otrzymanych z Jade TeX i przetworzenia ich jako plików LaTeX.

%prep
%setup -q 
%patch1 -p1

%build
%{__make} basic jadetex.fmt pdfjadetex.fmt

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/texmf/{web2c,tex/jadetex} \
	   $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

cp jadetex.1 pdfjadetex.1 ${RPM_BUILD_ROOT}%{_mandir}/man1

ln -s tex ${RPM_BUILD_ROOT}%{_bindir}/jadetex
ln -s pdftex ${RPM_BUILD_ROOT}%{_bindir}/pdfjadetex

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ -x %{_bindir}/texhash ] && /usr/bin/env - %{_bindir}/texhash 1>&2

%postun
[ -x %{_bindir}/texhash ] && /usr/bin/env - %{_bindir}/texhash 1>&2

%files
%defattr(644,root,root,755)
%doc ChangeLog ChangeLog-old doc/releasenotes.html
%attr(755,root,root) %{_bindir}/*
%{_datadir}/texmf/web2c/*
%{_datadir}/texmf/tex/jadetex
%{_mandir}/man1/*
