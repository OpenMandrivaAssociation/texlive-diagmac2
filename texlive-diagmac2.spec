Name:		texlive-diagmac2
Version:	15878
Release:	2
Summary:	Diagram macros, using pict2e
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/diagmac2
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/diagmac2.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/diagmac2.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a development of the long-established diagmac package,
using pict2e so that the restrictions on line direction are
removed.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/diagmac2/diagmac2.sty
%doc %{_texmfdistdir}/doc/latex/diagmac2/README
%doc %{_texmfdistdir}/doc/latex/diagmac2/doc/diagmac2.pdf
%doc %{_texmfdistdir}/doc/latex/diagmac2/doc/diagmac2.tex
%doc %{_texmfdistdir}/doc/latex/diagmac2/doc/diagmactest.pdf
%doc %{_texmfdistdir}/doc/latex/diagmac2/doc/diagmactest.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
