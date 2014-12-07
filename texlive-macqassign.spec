# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/macqassign
# catalog-date 2009-03-01 13:29:14 +0100
# catalog-license lppl
# catalog-version 1
Name:		texlive-macqassign
Version:	1
Release:	9
Summary:	Typeset assignments for Macquarie University
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/macqassign
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/macqassign.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/macqassign.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive macqassign package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/macqassign/macqassign.cls
%doc %{_texmfdistdir}/doc/latex/macqassign/README
%doc %{_texmfdistdir}/doc/latex/macqassign/logo.ps
%doc %{_texmfdistdir}/doc/latex/macqassign/sample-assign.pdf
%doc %{_texmfdistdir}/doc/latex/macqassign/sample-assign.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1-2
+ Revision: 753673
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1-1
+ Revision: 718935
- texlive-macqassign
- texlive-macqassign
- texlive-macqassign
- texlive-macqassign

