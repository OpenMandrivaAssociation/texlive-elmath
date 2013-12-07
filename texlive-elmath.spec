# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/elmath
# catalog-date 2007-05-25 16:15:27 +0200
# catalog-license lppl
# catalog-version v1.2
Name:		texlive-elmath
Version:	v1.2
Release:	6
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


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> v1.2-2
+ Revision: 751405
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> v1.2-1
+ Revision: 718320
- texlive-elmath
- texlive-elmath
- texlive-elmath
- texlive-elmath

