Summary:	LaTeX macros for converting Jade TeX output into DVI/PS/PDF
Summary(pl):	Makra LaTeXa do konwersji Jade TeXa do DVI/PS/PDF
Name:		jadetex
Version:	3.13
Release:	3
License:	Copyright (C) 1995,1996,1997,1998,1999,2000,2001 Sebastian Rahtz <s.rahtz@elsevier.co.uk>
Group:		Applications/Publishing/SGML
Source0:	http://dl.sourceforge.net/jadetex/%{name}-%{version}.tar.gz
# Source0-md5:	634dfc172fbf66a6976e2c2c60e2d198
Patch1:		%{name}-latin2.patch
Patch2:		%{name}-etex.patch
Patch3:		%{name}-texmfvar.patch
URL:		http://jadetex.sourceforge.net/
BuildRequires:	tetex-csplain >= 1:3.0
BuildRequires:	tetex-fonts-cmcyr >= 1:3.0
BuildRequires:	tetex-fonts-jknappen >= 1:3.0
BuildRequires:	tetex-format-latex >= 1:3.0
BuildRequires:	tetex-format-pdflatex >= 1:3.0
BuildRequires:	tetex-format-pdftex >= 1:3.0
BuildRequires:	tetex-format-plain >= 1:3.0
BuildRequires:	tetex-latex-ams >= 1:3.0
BuildRequires:	tetex-latex-carlisle >= 1:3.0
BuildRequires:	tetex-latex-cyrillic >= 1:3.0
BuildRequires:	tetex-latex-psnfss >= 1:3.0
BuildRequires:	tetex-latex-marvosym >= 1:3.0
BuildRequires:	tetex-metafont >= 1:3.0
BuildRequires:	tetex-pdftex >= 1:3.0
BuildRequires:	tetex-tex-babel >= 1:3.0
BuildRequires:	tetex-tex-ruhyphen >= 1:3.0
BuildRequires:	tetex-tex-ukrhyph >= 1:3.0
PreReq:		sh-utils
Requires:	sgml-common
%requires_eq	tetex
%requires_eq	tetex-latex
Requires:	tetex-pdftex >= 1:3.0
AutoReqProv:	no
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	texmf	/usr/share/texmf
%define texmfsysvar /var/lib/texmf

%description
JadeTeX contains the additional LaTeX macros necessary for taking Jade
TeX output files and processing them as LaTeX files.

%description -l pl
JadeTeX zawiera dodatkowe makra LaTeXa potrzebne do konwersji plików
otrzymanych z Jade TeXa i przetworzenia ich jako plików LaTeXa.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__make} basic jadetex.fmt pdfjadetex.fmt

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{texmf}/web2c,%{texmfsysvar}/tex/jadetex} \
	   $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install jadetex.1 pdfjadetex.1 $RPM_BUILD_ROOT%{_mandir}/man1

ln -s etex $RPM_BUILD_ROOT%{_bindir}/jadetex
ln -s pdfetex $RPM_BUILD_ROOT%{_bindir}/pdfjadetex

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ -x %{_bindir}/texhash ] && /usr/bin/env - %{_bindir}/texhash 1>&2

%postun
[ -x %{_bindir}/texhash ] && /usr/bin/env - %{_bindir}/texhash 1>&2

%files
%defattr(644,root,root,755)
%doc ChangeLog ChangeLog-old
%attr(755,root,root) %{_bindir}/*
%{texmfsysvar}/web2c/*.fmt
%{texmf}/tex/jadetex
%{_mandir}/man1/*
