Summary:	GNU international fonts
Summary(pl):	Miêdzynarodowe fonty GNU
Name:		intlfonts
Version:	1.2
Release:	1
License:	GPL
Group:		X11/Fonts
Source0:	%{name}-%{version}.tar.gz
Patch0:		%{name}-Chinese.patch
Patch1:		%{name}-dirs.patch
BuildRequires:	XFree86-devel
BuildRequires:	t1utils
BuildRequires:	ttmkfdir
Requires(post,postun):	/usr/X11R6/bin/mkfontdir
Requires(post,postun):	fileutils
Requires(post,postun):	textutils
Requires(post,postun):	grep
Requires(post,postun):	sed
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		ttffontsdir	%{_fontsdir}/TTF
%define		t1fontsdir	%{_fontsdir}/Type1
%define		t1afmdir	%{t1fontsdir}/afm

%description
This package contains some common used fonts.

%package arabic
Summary:	International fonts for X -- Arabic.
Group:		X11/Fonts
Requires:	%{name}
Requires(post,postun):	/usr/X11R6/bin/mkfontdir

%description arabic
This package includes some Arabic fonts (digits and single and double
column).

%package asian
Summary:	International fonts for X -- Asian.
Group:		X11/Fonts
Requires(post,postun):	/usr/X11R6/bin/mkfontdir

%description asian
This package includes some Vietnamese, Indian, Lao, and Thai fonts.

%package chinese
Summary:	International fonts for X -- Chinese.
Group:		X11/Fonts
Requires(post,postun):	/usr/X11R6/bin/mkfontdir

%description chinese
This package includes some GB2312, GB8565-88, BIG5 (ETen), and SiSheng
Chinese fonts.

%package ethiopic
Summary:	International fonts for X -- Ethiopic.
Group:		X11/Fonts
Requires(post,postun):	/usr/X11R6/bin/mkfontdir

%description ethiopic
This package includes Unicode Ethiopic fonts.

%package european
Summary:	International fonts for X -- European.
Group:		X11/Fonts
Requires(post,postun):	/usr/X11R6/bin/mkfontdir

%description european
This package includes some ISO 8859-1 (Latin-1), ISO 8859-2 (Latin-2),
ISO 8859-3 (Latin-3), ISO 8859-4 (Latin-4), ISO 8859-5 (Cyrillic),
ISO 8859-7 (Greek), ISO 8859-8 (Hebrew), ISO 8859-9 (Latin-5), and KOI
(Cyrillic) fonts.  Also one ISO 8859-1 big font is included.

%package hebrew
Summary:	International fonts for X -- Hebrew.
Group:		X11/Fonts
Requires:	%{name}
Requires(post,postun):	/usr/X11R6/bin/mkfontdir

%description hebrew
This package includes some Hebrew fonts.

%package japanese
Summary:	International fonts for X -- Japanese.
Group:		X11/Fonts
Requires(post,postun):	/usr/X11R6/bin/mkfontdir

%description japanese
This package includes some JISX0208.1990, JISX0208.1978, JISX0212.1990
(HojoKanji), JISX0208.1983, and JISX0201 (Roman & Kana) Japanese fonts.

%package phonetic
Summary:	International fonts for X -- Phonetic Alphabet.
Group:		X11/Fonts
Requires:	%{name}
Requires(post,postun):	/usr/X11R6/bin/mkfontdir

%description phonetic
This package includes some fonts of International Phonetic Alphabet.

%package TrueType
Summary:	International fonts for X -- Truetype.
Group:		X11/Fonts
Requires(post,postun):	/usr/X11R6/bin/mkfontdir

%description TrueType

%package Type1
Summary:	International fonts for X -- Type1.
Group:		X11/Fonts
Requires(post,postun):	/usr/X11R6/bin/mkfontdir

%description Type1

%package emacs
Summary:	Fonts to allow multi-lingual PostScript printing from Emacs.
Group:		Applications/Editors/Emacs
Requires:	emacs-common

%description emacs
This package includes BDF fonts to print Amharic, Arabic, Cantonese,
Chinese, Czech, Danish, Esperanto, Estonian, Finnish, French, German,
Greek, Hebrew, Hindi, Italian, Japanese, Korean, Maltese, Nederlands,
Norwegian, Polish, Russian, Slovak, Spanish, Swedish, Thai, Tigrigna,
Turkish and Vietnamese text as bit-mapped PostScript.  To see these
languages in X, you can use the intlfonts-* packages (among others).

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
./configure \
	--with-fontdir=$RPM_BUILD_ROOT%{_fontsdir} \
	--enable-compress \
	--with-type1 \
	--with-truetype \
	--without-bdf

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/emacs/fonts/bdf

%{__make} install

install -d $RPM_BUILD_ROOT/%{t1afmdir}
mv -f $RPM_BUILD_ROOT/%{t1fontsdir}/*.afm $RPM_BUILD_ROOT/%{t1afmdir}/
rm -f $RPM_BUILD_ROOT/%{t1fontsdir}/*.pfa

mv -f $RPM_BUILD_ROOT%{_fontsdir}/TrueType $RPM_BUILD_ROOT%{ttffontsdir}

cd $RPM_BUILD_ROOT/%{ttffontsdir}
/usr/bin/ttmkfdir | tail +2 >fonts.scale.intl
cd -

cd $RPM_BUILD_ROOT/%{t1fontsdir}
/usr/bin/type1inst
tail +2 fonts.dir > fonts.dir.intl
tail +2 fonts.scale > fonts.scale.intl
mv -f Fontmap Fontmap.intl
cd -

install -m 644 `find -name '*.bdf'` $RPM_BUILD_ROOT%{_datadir}/emacs/fonts/bdf/

%clean
rm -rf $RPM_BUILD_ROOT

%post arabic
cd %{_fontsdir}/Misc
umask 022
/usr/X11R6/bin/mkfontdir

%postun arabic
cd %{_fontsdir}/Misc
umask 022
/usr/X11R6/bin/mkfontdir

%post asian
cd %{_fontsdir}/Asian
umask 022
/usr/X11R6/bin/mkfontdir

%postun asian
cd %{_fontsdir}/Asian
umask 022
/usr/X11R6/bin/mkfontdir

%post chinese
cd %{_fontsdir}/Chinese
umask 022
/usr/X11R6/bin/mkfontdir

%postun chinese
cd %{_fontsdir}/Chinese
umask 022
/usr/X11R6/bin/mkfontdir

%post ethiopic
cd %{_fontsdir}/Ethiopic
umask 022
/usr/X11R6/bin/mkfontdir

%postun ethiopic
cd %{_fontsdir}/Ethiopic
umask 022
/usr/X11R6/bin/mkfontdir

%post european
cd %{_fontsdir}/European
umask 022
/usr/X11R6/bin/mkfontdir

%postun european
cd %{_fontsdir}/European
umask 022
/usr/X11R6/bin/mkfontdir

%post hebrew
cd %{_fontsdir}/Misc
umask 022
/usr/X11R6/bin/mkfontdir

%postun hebrew
cd %{_fontsdir}/Misc
umask 022
/usr/X11R6/bin/mkfontdir

%post japanese
cd %{_fontsdir}/Japanese
umask 022
/usr/X11R6/bin/mkfontdir

%postun japanese
cd %{_fontsdir}/Japanese
umask 022
/usr/X11R6/bin/mkfontdir

%post phonetic
cd %{_fontsdir}/Misc
umask 022
/usr/X11R6/bin/mkfontdir

%postun phonetic
cd %{_fontsdir}/Misc
umask 022
/usr/X11R6/bin/mkfontdir

%post TrueType
cd %{ttffontsdir}
umask 022
rm -f fonts.scale.bak
cat fonts.scale.* | sort -u > fonts.scale.tmp
cat fonts.scale.tmp | wc -l | sed -e 's/ //g' > fonts.scale
cat fonts.scale.tmp >> fonts.scale
rm -f fonts.scale.tmp fonts.dir
ln -sf fonts.scale fonts.dir
if [ -x /usr/X11R6/bin/xftcache ]; then
	/usr/X11R6/bin/xftcache .
fi

%postun TrueType
cd %{ttffontsdir}
umask 022
rm -f fonts.scale.bak
cat fonts.scale.* 2>/dev/null | sort -u > fonts.scale.tmp
cat fonts.scale.tmp | wc -l | sed -e 's/ //g' > fonts.scale
cat fonts.scale.tmp >> fonts.scale
rm -f fonts.scale.tmp fonts.dir
ln -sf fonts.scale fonts.dir
if [ -x /usr/X11R6/bin/xftcache ]; then
	/usr/X11R6/bin/xftcache .
fi

%post Type1
cd %{t1fontsdir}
umask 022
rm -f fonts.scale.bak Fontmap.bak
cat fonts.scale.* | sort -u > fonts.scale.tmp
cat fonts.scale.tmp | wc -l | sed -e 's/ //g' > fonts.scale
cat fonts.scale.tmp >> fonts.scale
rm -f fonts.scale.tmp fonts.dir
ln -sf fonts.scale fonts.dir
cat Fontmap.* > Fontmap
cat fonts.alias.* > fonts.alias
if [ -x /usr/X11R6/bin/xftcache ]; then
	/usr/X11R6/bin/xftcache .
fi

%postun Type1
cd %{t1fontsdir}
umask 022
rm -f fonts.scale.bak Fontmap.bak
cat fonts.scale.* 2>/dev/null | sort -u > fonts.scale.tmp
cat fonts.scale.tmp | wc -l | sed -e 's/ //g' > fonts.scale
cat fonts.scale.tmp >> fonts.scale
rm -f fonts.scale.tmp fonts.dir
ln -sf fonts.scale fonts.dir
cat Fontmap.* > Fontmap 2>/dev/null
cat fonts.alias.* > fonts.alias 2>/dev/null
if [ -x /usr/X11R6/bin/xftcache ]; then
	/usr/X11R6/bin/xftcache .
fi

%files
%defattr(644,root,root,755)
%dir %{_fontsdir}/Misc
%dir %{_fontsdir}/Misc/bmp*

%files arabic
%defattr(644,root,root,755)
%{_fontsdir}/Misc/arab*pcf.gz

%files asian
%defattr(644,root,root,755)
%dir %{_fontsdir}/Asian
%{_fontsdir}/Asian/*

%files chinese
%defattr(644,root,root,755)
%dir %{_fontsdir}/Chinese
%{_fontsdir}/Chinese/*

%files ethiopic
%defattr(644,root,root,755)
%dir %{_fontsdir}/Ethiopic
%{_fontsdir}/Ethiopic/*

%files european
%defattr(644,root,root,755)
%dir %{_fontsdir}/European
%{_fontsdir}/European/*

%files hebrew
%defattr(644,root,root,755)
%{_fontsdir}/Misc/heb*pcf.gz

%files japanese
%defattr(644,root,root,755)
%dir %{_fontsdir}/Japanese
%{_fontsdir}/Japanese/*

%files phonetic
%defattr(644,root,root,755)
%{_fontsdir}/Misc/ipa*pcf.gz

%files TrueType
%defattr(644,root,root,755)
%{_fontsdir}/TTF/*

%files Type1
%defattr(644,root,root,755)
%{_fontsdir}/Type1/*.pfb
%{_fontsdir}/Type1/*.intl
%{_fontsdir}/Type1/afm/*

%files emacs
%{_datadir}/emacs/fonts/bdf/*
