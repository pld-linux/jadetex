Summary:	LaTeX macros for converting Jade TeX output into DVI/PS/PDF
Name:		jadetex
Version:	2.15
Release:	2
Copyright:	Copyright (C) 1995,1996,1997,1998 Sebastian Rahtz <s.rahtz@elsevier.co.uk>
Group:		Applications/Publishing/SGML
Group(pl):	Aplikacje/Publikowanie/SGML
Source0:	ftp://ftp.duke.edu/tex-archive/macros/%{name}.tar.bz2
Source1:	%{name}-latin2.dtx
Patch0:		%{name}-i18n.patch
Requires:	sgml-common, tetex >= 0.9, tetex-latex >= 0.9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	hugelatex
Autoreqprov:	no

%description
JadeTeX contains the additional LaTeX macros necessary for taking Jade
TeX output files and processing them as LaTeX files.

%prep
%setup -q -n jadetex
%patch0 -p1 

%build
tex jadetex.ins 
# 'echo' is temporary fix for some latex errors
# they are not important and can be ignored
echo | tex -ini "&hugelatex" -progname=jadetex jadetex.ini || :
echo | pdftex -ini "&pdflatex" -progname=pdfjadetex pdfjadetex.ini || :

# backup original files
install -d orig && mv -f *.fmt *.ltx orig

# now build latin2 jadetex
cp -f %{SOURCE1} ./jadetex.dtx
tex jadetex.ins
echo | tex -ini "&hugelatex" -progname=jadetex jadetex.ini || :
echo | pdftex -ini "&pdflatex" -progname=pdfjadetex pdfjadetex.ini || :

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/texmf/{web2c,tex/jadetex} \
	   $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

cp jadetex.1 pdfjadetex.1 ${RPM_BUILD_ROOT}%{_mandir}/man1 
# orig
mv orig/pdfjadetex.fmt orig/jadetex.fmt $RPM_BUILD_ROOT%{_datadir}/texmf/web2c
cp dsssl.def orig/jadetex.ltx $RPM_BUILD_ROOT%{_datadir}/texmf/tex/jadetex
# latin2
mv pdfjadetex.fmt $RPM_BUILD_ROOT%{_datadir}/texmf/web2c/pdfjadetexl2.fmt
mv jadetex.fmt    $RPM_BUILD_ROOT%{_datadir}/texmf/web2c/jadetexl2.fmt
cp jadetex.ltx    $RPM_BUILD_ROOT%{_datadir}/texmf/tex/jadetex/jadetexl2.ltx

#ln -s virtex ${RPM_BUILD_ROOT}%{_bindir}/jadetex
#ln -s pdfvirtex ${RPM_BUILD_ROOT}%{_bindir}/pdfjadetex
ln -s tex ${RPM_BUILD_ROOT}%{_bindir}/jadetex
ln -s pdftex ${RPM_BUILD_ROOT}%{_bindir}/pdfjadetex
ln -s tex ${RPM_BUILD_ROOT}%{_bindir}/jadetexl2
ln -s pdftex ${RPM_BUILD_ROOT}%{_bindir}/pdfjadetexl2

gzip -9nf ${RPM_BUILD_ROOT}%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ -x %{_bindir}/texhash ] && /usr/bin/env - %{_bindir}/texhash 1>&2

%postun
[ -x %{_bindir}/texhash ] && /usr/bin/env - %{_bindir}/texhash 1>&2

%files
%defattr(644,root,root,755)
#%doc ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_datadir}/texmf/web2c/*
%{_datadir}/texmf/tex/jadetex
%{_mandir}/man1/*
