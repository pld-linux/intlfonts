Summary:	GNU international fonts
Summary(pl):	Mi�dzynarodowe fonty GNU
Name:		intlfonts
Version:	1.2.1
Release:	1
License:	GPL
Group:		Fonts
Source0:	ftp://ftp.gnu.org/gnu/intlfonts/%{name}-%{version}.tar.gz
# Source0-md5:	d77e9c4ec066a985687e5c67992677e4
Patch0:		%{name}-Chinese.patch
Patch1:		%{name}-dirs.patch
URL:		http://www.gnu.org/directory/GNU/intlfonts.html
BuildRequires:	XFree86-devel
BuildRequires:	t1utils
BuildRequires:	type1inst
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		ttffontsdir	%{_fontsdir}/TTF
%define		t1fontsdir	%{_fontsdir}/Type1
%define		t1afmdir	%{t1fontsdir}/afm

%description
This package contains some common used fonts.

%description -l pl
Ten pakiet zawiera troch� powszechnie u�ywanych font�w.

%package arabic
Summary:	International fonts for X -- Arabic
Summary(pl):	Mi�dzynarodowe fonty dla X - arabskie
Group:		Fonts
Requires:	%{name}
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/Misc

%description arabic
This package includes some Arabic fonts (digits and single and double
column).

%description arabic -l pl
Ten pakiet zawiera troch� arabskich font�w (cyfry i pojedyncze oraz
podw�jne kolumny).

%package asian
Summary:	International fonts for X -- Asian
Summary(pl):	Mi�dzynarodowe fonty dla X - azjatyckie
Group:		Fonts
Requires(post,postun):	fontpostinst

%description asian
This package includes some Vietnamese, Indian, Lao, and Thai fonts.

%description asian -l pl
Ten pakiet zawiera troch� font�w wietnamskich, indyjskich, laoskich i
tajskich.

%package chinese
Summary:	International fonts for X -- Chinese
Summary(pl):	Mi�dzynarodowe fonty dla X - chi�skie
Group:		Fonts
Requires(post,postun):	fontpostinst

%description chinese
This package includes some GB2312, GB8565-88, BIG5 (ETen), and SiSheng
Chinese fonts.

%description chinese -l pl
Ten pakiet zawiera troch� chi�skich font�w GB2312, GB8565-88, BIG5
(ETen) oraz SiSheng.

%package ethiopic
Summary:	International fonts for X -- Ethiopic
Summary(pl):	Mi�dzynarodowe fonty dla X - etiopskie
Group:		Fonts
Requires(post,postun):	fontpostinst

%description ethiopic
This package includes Unicode Ethiopic fonts.

%description ethiopic -l pl
Ten pakiet zawiera unikodowe fonty etiopskie.

%package european
Summary:	International fonts for X -- European
Summary(pl):	Mi�dzynarodowe fonty dla X - europejskie
Group:		Fonts
Requires(post,postun):	fontpostinst

%description european
This package includes some ISO 8859-1 (Latin-1), ISO 8859-2 (Latin-2),
ISO 8859-3 (Latin-3), ISO 8859-4 (Latin-4), ISO 8859-5 (Cyrillic),
ISO 8859-7 (Greek), ISO 8859-8 (Hebrew), ISO 8859-9 (Latin-5), and KOI
(Cyrillic) fonts.  Also one ISO 8859-1 big font is included.

%description european -l pl
Ten pakiet zawiera troch� font�w ISO 8859-1 (Latin-1), ISO 8859-2
(Latin-2), ISO 8859-3 (Latin-3), ISO 8859-4 (Latin-4), ISO 8859-5
(cyrilica), ISO 8859-7 (greckie), ISO 8859-8 (hebrajkie), ISO 8859-9
(Latin-5) oraz KOI (cyrylica). Jest te� do��czony jeden du�y font ISO
8859-1.

%package hebrew
Summary:	International fonts for X -- Hebrew
Summary(pl):	Mi�dzynarodowe fonty dla X - hebrajskie
Group:		Fonts
Requires:	%{name}
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/Misc

%description hebrew
This package includes some Hebrew fonts.

%description hebrew -l pl
Ten pakiet zawiera troch� font�w hebrajskich.

%package japanese
Summary:	International fonts for X -- Japanese
Summary(pl):	Mi�dzynarodowe fonty dla X - japo�skie
Group:		Fonts
Requires(post,postun):	fontpostinst

%description japanese
This package includes some JISX0208.1990, JISX0208.1978, JISX0212.1990
(HojoKanji), JISX0208.1983, and JISX0201 (Roman & Kana) Japanese
fonts.

%description japanese -l pl
Ten pakiet zawiera troch� japo�skich font�w JISX0208.1990,
JISX0208.1978, JISX0212.1990 (HojoKanji), JISX0208.1983 oraz JISX0201
(Roman i Kana).

%package phonetic
Summary:	International fonts for X -- Phonetic Alphabet
Summary(pl):	Mi�dzynarodowe fonty dla X - alfabet fonetyczny
Group:		Fonts
Requires:	%{name}
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/Misc

%description phonetic
This package includes some fonts of International Phonetic Alphabet.

%description phonetic -l pl
Ten pakiet zawiera troch� font�w dla mi�dzynarodowego alfabetu
fonetycznego.

%package TrueType
Summary:	International fonts for X -- TrueType
Summary(pl):	Mi�dzynarodowe fonty dla X - TrueType
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/TTF

%description TrueType
This package includes some TrueType fonts.

%description TrueType -l pl
Ten pakiet zawiera troch� font�w TrueType.

%package Type1
Summary:	International fonts for X -- Type1
Summary(pl):	Mi�dzynarodowe fonty dla X - Type1
Group:		Fonts
Requires(post,postun):	fontpostinst >= 0.1-6
Requires:	%{_fontsdir}/Type1

%description Type1
This package includes some Type1 fonts.

%description Type1 -l pl
Ten pakiet zawiera troch� font�w Type1.

%package emacs
Summary:	Fonts to allow multi-lingual PostScript printing from Emacs
Summary(pl):	Fonty pozwalaj�ce na drukowanie wieloj�zycznego PostScriptu z Emacsa
Group:		Applications/Editors/Emacs
Requires:	emacs-common

%description emacs
This package includes BDF fonts to print Amharic, Arabic, Cantonese,
Chinese, Czech, Danish, Esperanto, Estonian, Finnish, French, German,
Greek, Hebrew, Hindi, Italian, Japanese, Korean, Maltese, Nederlands,
Norwegian, Polish, Russian, Slovak, Spanish, Swedish, Thai, Tigrigna,
Turkish and Vietnamese text as bit-mapped PostScript.  To see these
languages in X, you can use the intlfonts-* packages (among others).

%description emacs -l pl
Ten pakiet zawiera fonty BDF pozwalaj�ce na drukowanie do bitmapowego
PostScriptu tekst�w w j�zykach: amharskim, arabskim, kanto�skim,
chi�skim, czeskim, du�skim, esperanto, esto�skim, fi�skim, francuskim,
niemieckim, greckim, hebrajskim, hindi, w�oskim, japo�skim,
korea�skim, malta�skim, holenderskim, norweskim, polskim, rosyjskim,
s�owackim, hiszpa�skim, szwedzkim, tajskim, tigrinia, tureckim i
wietnamskim. Aby zobaczy� te j�zyki pod X, mo�na u�y� pakiet�w
intlfonts-* (i innych).

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

install -d $RPM_BUILD_ROOT%{t1afmdir}
mv -f $RPM_BUILD_ROOT%{t1fontsdir}/*.afm $RPM_BUILD_ROOT%{t1afmdir}
rm -f $RPM_BUILD_ROOT%{t1fontsdir}/*.pfa

mv -f $RPM_BUILD_ROOT%{_fontsdir}/TrueType $RPM_BUILD_ROOT%{ttffontsdir}

cd $RPM_BUILD_ROOT%{t1fontsdir}
/usr/bin/type1inst
tail -n +2 fonts.scale > fonts.scale.intl
mv -f Fontmap Fontmap.intl
cd -

install -m 644 `find -name '*.bdf'` $RPM_BUILD_ROOT%{_datadir}/emacs/fonts/bdf/

%clean
rm -rf $RPM_BUILD_ROOT

%post arabic
fontpostinst misc %{_fontsdir}/Misc

%postun arabic
fontpostinst misc %{_fontsdir}/Misc

%post asian
fontpostinst misc %{_fontsdir}/Asian

%postun asian
fontpostinst misc %{_fontsdir}/Asian

%post chinese
fontpostinst misc %{_fontsdir}/Chinese

%postun chinese
fontpostinst misc %{_fontsdir}/Chinese

%post ethiopic
fontpostinst misc %{_fontsdir}/Ethiopic

%postun ethiopic
fontpostinst misc %{_fontsdir}/Ethiopic

%post european
fontpostinst misc %{_fontsdir}/European

%postun european
fontpostinst misc %{_fontsdir}/European

%post hebrew
fontpostinst misc %{_fontsdir}/Misc

%postun hebrew
fontpostinst misc %{_fontsdir}/Misc

%post japanese
fontpostinst misc %{_fontsdir}/Japanese

%postun japanese
fontpostinst misc %{_fontsdir}/Japanese

%post phonetic
fontpostinst misc %{_fontsdir}/Misc

%postun phonetic
fontpostinst misc %{_fontsdir}/Misc

%post TrueType
fontpostinst TTF

%postun TrueType
fontpostinst TTF

%post Type1
fontpostinst Type1

%postun Type1
fontpostinst Type1

%files
%defattr(644,root,root,755)
%dir %{_fontsdir}/Misc
%dir %{_fontsdir}/Misc/bmp*

%files arabic
%defattr(644,root,root,755)
%{_fontsdir}/Misc/arab*pcf.gz

%files asian
%defattr(644,root,root,755)
%{_fontsdir}/Asian

%files chinese
%defattr(644,root,root,755)
%{_fontsdir}/Chinese

%files ethiopic
%defattr(644,root,root,755)
%{_fontsdir}/Ethiopic

%files european
%defattr(644,root,root,755)
%{_fontsdir}/European

%files hebrew
%defattr(644,root,root,755)
%{_fontsdir}/Misc/heb*pcf.gz

%files japanese
%defattr(644,root,root,755)
%{_fontsdir}/Japanese

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
%defattr(644,root,root,755)
%{_datadir}/emacs/fonts/bdf/*
