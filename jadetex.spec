Summary:	LaTeX macros for converting Jade TeX output into DVI/PS/PDF
Summary(pl.UTF-8):	Makra LaTeXa do konwersji Jade TeXa do DVI/PS/PDF
Name:		jadetex
Version:	3.13
Release:	9
License:	Copyright (C) 1995,1996,1997,1998,1999,2000,2001 Sebastian Rahtz <s.rahtz@elsevier.co.uk>
Group:		Applications/Publishing/SGML
Source0:	http://dl.sourceforge.net/jadetex/%{name}-%{version}.tar.gz
# Source0-md5:	634dfc172fbf66a6976e2c2c60e2d198
Patch0:		%{name}-latex.patch
Patch1:		%{name}-latin2.patch
URL:		http://jadetex.sourceforge.net/
BuildRequires:	texlive-fonts-jknappen
BuildRequires:	texlive-format-pdflatex
BuildRequires:	texlive-latex-ams
BuildRequires:	texlive-latex-extend
BuildRequires:	texlive-latex-marvosym
BuildRequires:	texlive-latex-psnfss
BuildRequires:	texlive-latex-wasysym
BuildRequires:	texlive-omega
BuildRequires:	texlive-xetex
Requires:	sgml-common
Requires:	sh-utils
AutoReqProv:	no
%requires_eq	texlive
%requires_eq	texlive-latex
Requires:	texlive-pdftex
Provides:	tetex-jadetex = %{version}-%{release}
Provides:	texlive-jadetex = %{version}-%{release}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JadeTeX contains the additional LaTeX macros necessary for taking Jade
TeX output files and processing them as LaTeX files.

%description -l pl.UTF-8
JadeTeX zawiera dodatkowe makra LaTeXa potrzebne do konwersji plików
otrzymanych z Jade TeXa i przetworzenia ich jako plików LaTeXa.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__make} basic jadetex.fmt pdfjadetex.fmt

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/texmf/{web2c,tex/jadetex} \
	   $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install jadetex.1 pdfjadetex.1 $RPM_BUILD_ROOT%{_mandir}/man1

ln -s pdfetex $RPM_BUILD_ROOT%{_bindir}/jadetex
ln -s pdfetex $RPM_BUILD_ROOT%{_bindir}/pdfjadetex

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x %{_bindir}/texhash ] || /usr/bin/env - %{_bindir}/texhash 1>&2

%postun
[ ! -x %{_bindir}/texhash ] || /usr/bin/env - %{_bindir}/texhash 1>&2

%files
%defattr(644,root,root,755)
%doc ChangeLog ChangeLog-old
%attr(755,root,root) %{_bindir}/*
%{_datadir}/texmf/web2c/*.fmt
%{_datadir}/texmf/tex/jadetex
%{_mandir}/man1/*
