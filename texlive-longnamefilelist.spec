Name:		texlive-longnamefilelist
Version:	27889
Release:	2
Summary:	Tidy \listfiles with long file names
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/longnamefilelist
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/longnamefilelist.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/longnamefilelist.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/longnamefilelist.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package equips LaTeX's \listfiles command with an optional
argument for the number of characters in the longest base
filename. This way you get a neatly aligned file list even when
it contains files whose base names have more than 8 characters.
The package can be combined with the myfilist package as
explained in the documentation.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/longnamefilelist/longnamefilelist.sty
%doc %{_texmfdistdir}/doc/latex/longnamefilelist/README
%doc %{_texmfdistdir}/doc/latex/longnamefilelist/SrcFILEs.txt
%doc %{_texmfdistdir}/doc/latex/longnamefilelist/longnamefilelist.pdf
#- source
%doc %{_texmfdistdir}/source/latex/longnamefilelist/longnamefilelist.tex
%doc %{_texmfdistdir}/source/latex/longnamefilelist/srcfiles.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
