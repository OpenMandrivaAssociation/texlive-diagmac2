%global tl_name diagmac2
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.1
Release:	%{tl_revision}.1
Summary:	Diagram macros, using pict2e
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/diagmac2
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/diagmac2.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/diagmac2.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a development of the long-established diagmac package, using
pict2e so that the restrictions on line direction are removed.

