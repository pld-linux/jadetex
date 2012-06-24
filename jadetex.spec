Summary:	LaTeX macros for converting Jade TeX output into DVI/PS/PDF
Summary(pl):	Makra LaTeX do konwersji Jade Tex do DVI/PS/PDF
Name:		jadetex
Version:	3.5
Release:	3
License:	Copyright (C) 1995,1996,1997,1998,1999,2000,2001 Sebastian Rahtz <s.rahtz@elsevier.co.uk>
Group:		Applications/Publishing/SGML
Source0:	http://www.tug.org/applications/%{name}/%{name}.zip
#Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/%{name}/%{name}-%{version}.tar.gz
Patch1:		%{name}-latin2.patch
URL:		http://jadetex.sourceforge.net/
Requires:	sgml-common
%requires_eq	tetex
%requires_eq	tetex-latex
BuildRequires:	hugelatex
BuildRequires:	tetex-pdftex
BuildRequires:	tetex-format-plain
BuildRequires:	tetex-format-pdftex
BuildRequires:	tetex-format-pdflatex
BuildRequires:	tetex-latex-carlisle
BuildRequires:	tetex-tex-babel
BuildRequires:  tetex-latex-cyrillic
BuildRequires:	tetex-latex-ams
BuildRequires:	tetex-latex-psnfss
BuildRequires:	tetex-metafont
BuildRequires:	tetex-fonts-cmcyr
BuildRequires:	tetex-fonts-jknappen
BuildRequires:	unzip
Autoreqprov:	no
Prereq:		sh-utils
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JadeTeX contains the additional LaTeX macros necessary for taking Jade
TeX output files and processing them as LaTeX files.

%description -l pl
JadeTeX zawiera dodatkowe makra LaTeX potrzebne do konwersji plik�w
otrzymanych z Jade TeX i przetworzenia ich jako plik�w LaTeX.

%prep
%setup -q -c -T
unzip -qa %{SOURCE0}
%patch1 -p1

%build
make
#tex jadetex.ins
# 'echo' is temporary fix for some latex errors
# they are not important and can be ignored
#echo | tex -ini "&hugelatex" -progname=jadetex jadetex.ini || :
#echo | pdftex -ini "&pdflatex" -progname=pdfjadetex pdfjadetex.ini || :

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/texmf/{web2c,tex/jadetex} \
	   $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

cp jadetex.1 pdfjadetex.1 ${RPM_BUILD_ROOT}%{_mandir}/man1
# orig
mv pdfjadetex.fmt jadetex.fmt $RPM_BUILD_ROOT%{_datadir}/texmf/web2c
cp dsssl.def jadetex.ltx $RPM_BUILD_ROOT%{_datadir}/texmf/tex/jadetex

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
%doc ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_datadir}/texmf/web2c/*
%{_datadir}/texmf/tex/jadetex
%{_mandir}/man1/*
