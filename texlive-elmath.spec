Name:		texlive-elmath
Version:	1.2
Release:	2
Summary:	Mathematics in Greek texts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/elmath
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/elmath.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/elmath.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/elmath.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package has been designed to facilitate the use of Greek
letters in mathematical mode. The package allows one to
directly type in Greek letters (in ISO 8859-7 encoding) in math
mode.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/elmath/elmath.sty
%doc %{_texmfdistdir}/doc/latex/elmath/elmath.pdf
#- source
%doc %{_texmfdistdir}/source/latex/elmath/elmath.dtx
%doc %{_texmfdistdir}/source/latex/elmath/elmath.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
