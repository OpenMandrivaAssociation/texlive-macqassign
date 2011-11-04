# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/macqassign
# catalog-date 2009-03-01 13:29:14 +0100
# catalog-license lppl
# catalog-version 1
Name:		texlive-macqassign
Version:	1
Release:	1
Summary:	Typeset assignments for Macquarie University
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/macqassign
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/macqassign.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/macqassign.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
TeXLive macqassign package.

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
%{_texmfdistdir}/tex/latex/macqassign/macqassign.cls
%doc %{_texmfdistdir}/doc/latex/macqassign/README
%doc %{_texmfdistdir}/doc/latex/macqassign/logo.ps
%doc %{_texmfdistdir}/doc/latex/macqassign/sample-assign.pdf
%doc %{_texmfdistdir}/doc/latex/macqassign/sample-assign.tex
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
