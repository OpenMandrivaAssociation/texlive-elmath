# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/elmath
# catalog-date 2007-05-25 16:15:27 +0200
# catalog-license lppl
# catalog-version v1.2
Name:		texlive-elmath
Version:	v1.2
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
This package has been designed to facilitate the use of Greek
letters in mathematical mode. The package allows one to
directly type in Greek letters (in ISO 8859-7 encoding) in math
mode.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/elmath/elmath.sty
%doc %{_texmfdistdir}/doc/latex/elmath/elmath.pdf
#- source
%doc %{_texmfdistdir}/source/latex/elmath/elmath.dtx
%doc %{_texmfdistdir}/source/latex/elmath/elmath.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
