# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/diagmac2
# catalog-date 2009-05-17 01:32:22 +0200
# catalog-license lppl
# catalog-version 2.1
Name:		texlive-diagmac2
Version:	2.1
Release:	1
Summary:	Diagram macros, using pict2e
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/diagmac2
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/diagmac2.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/diagmac2.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
This is a development of the long-established diagmac package,
using pict2e so that the restrictions on line direction are
removed.

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
%{_texmfdistdir}/tex/latex/diagmac2/diagmac2.sty
%doc %{_texmfdistdir}/doc/latex/diagmac2/README
%doc %{_texmfdistdir}/doc/latex/diagmac2/doc/diagmac2.pdf
%doc %{_texmfdistdir}/doc/latex/diagmac2/doc/diagmac2.tex
%doc %{_texmfdistdir}/doc/latex/diagmac2/doc/diagmactest.pdf
%doc %{_texmfdistdir}/doc/latex/diagmac2/doc/diagmactest.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
