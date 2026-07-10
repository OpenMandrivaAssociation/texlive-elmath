%global tl_name elmath
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2
Release:	%{tl_revision}.1
Summary:	Mathematics in Greek texts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/elmath
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/elmath.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/elmath.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/elmath.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package has been designed to facilitate the use of Greek letters in
mathematical mode. The package allows one to directly type in Greek
letters (in ISO 8859-7 encoding) in math mode.

