Summary:	LaTeX macros for converting Jade TeX output into DVI/PS/PDF
Summary(pl):	Makra LaTeX do konwersji Jade Tex do DVI/PS/PDF
Name:		jadetex
Version:	3.5
Release:	2
Copyright:	Copyright (C) 1995,1996,1997,1998,1999,2000,2001 Sebastian Rahtz <s.rahtz@elsevier.co.uk>
Group:		Applications/Publishing/SGML
Group(de):	Applikationen/Publizieren/SGML
Group(pl):	Aplikacje/Publikowanie/SGML
URL:		http://www.tug.org/applications/jadetex/
Source0:	http://www.tug.org/applications/%{name}/%{name}.zip
Patch1:		%{name}-latin2.patch
Requires:	sgml-common
%requires_eq	tetex
%requires_eq	tetex-latex
BuildRequires:	hugelatex
BuildRequires:	tetex-pdftex
BuildRequires:	unzip
Autoreqprov:	no
Prereq:		sh-utils
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JadeTeX contains the additional LaTeX macros necessary for taking Jade
TeX output files and processing them as LaTeX files.

%description -l pl
JadeTeX zawiera dodatkowe makra LaTeX potrzebne do konwersji plików
otrzymanych z Jade TeX i przetworzenia ich jako plików LaTeX.

%prep
%setup -q -c -T 
unzip -qa %{SOURCE0}
%patch1 -p1 

%build
tex jadetex.ins 
# 'echo' is temporary fix for some latex errors
# they are not important and can be ignored
echo | tex -ini "&hugelatex" -progname=jadetex jadetex.ini || :
echo | pdftex -ini "&pdflatex" -progname=pdfjadetex pdfjadetex.ini || :

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

gzip -9nf ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ -x %{_bindir}/texhash ] && /usr/bin/env - %{_bindir}/texhash 1>&2

%postun
[ -x %{_bindir}/texhash ] && /usr/bin/env - %{_bindir}/texhash 1>&2

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_datadir}/texmf/web2c/*
%{_datadir}/texmf/tex/jadetex
%{_mandir}/man1/*
