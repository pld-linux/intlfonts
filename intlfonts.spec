Summary:	GNU international fonts
Summary(pl.UTF-8):	Międzynarodowe fonty GNU
Name:		intlfonts
Version:	1.4.2
Release:	1
License:	GPL v3+ with exception
Group:		Fonts
Source0:	https://ftp.gnu.org/gnu/intlfonts/%{name}-%{version}.tar.gz
# Source0-md5:	28b394febfa611a9d431ea87d37c946f
Patch0:		%{name}-dirs.patch
URL:		https://directory.fsf.org/wiki/GNU/intlfonts
BuildRequires:	xorg-app-bdftopcf
BuildRequires:	xorg-app-mkfontdir
BuildRequires:	t1utils
BuildRequires:	type1inst
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		ttffontsdir	%{_fontsdir}/TTF
%define		t1fontsdir	%{_fontsdir}/Type1
%define		t1afmdir	%{t1fontsdir}/afm

%description
This package contains some common used fonts.

%description -l pl.UTF-8
Ten pakiet zawiera trochę powszechnie używanych fontów.

%package arabic
Summary:	International fonts for X -- Arabic
Summary(pl.UTF-8):	Międzynarodowe fonty dla X - arabskie
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{name} = %{version}-%{release}
Requires:	%{_fontsdir}/Misc

%description arabic
This package includes some Arabic fonts (digits and single and double
column).

%description arabic -l pl.UTF-8
Ten pakiet zawiera trochę arabskich fontów (cyfry i pojedyncze oraz
podwójne kolumny).

%package asian
Summary:	International fonts for X -- Asian
Summary(pl.UTF-8):	Międzynarodowe fonty dla X - azjatyckie
Group:		Fonts
Requires(post,postun):	fontpostinst

%description asian
This package includes some Vietnamese, Indian, Lao, and Thai fonts.

%description asian -l pl.UTF-8
Ten pakiet zawiera trochę fontów wietnamskich, indyjskich, laoskich i
tajskich.

%package chinese
Summary:	International fonts for X -- Chinese
Summary(pl.UTF-8):	Międzynarodowe fonty dla X - chińskie
Group:		Fonts
Requires(post,postun):	fontpostinst

%description chinese
This package includes some GB2312, GB8565-88, BIG5 (ETen), and SiSheng
Chinese fonts.

%description chinese -l pl.UTF-8
Ten pakiet zawiera trochę chińskich fontów GB2312, GB8565-88, BIG5
(ETen) oraz SiSheng.

%package ethiopic
Summary:	International fonts for X -- Ethiopic
Summary(pl.UTF-8):	Międzynarodowe fonty dla X - etiopskie
Group:		Fonts
Requires(post,postun):	fontpostinst

%description ethiopic
This package includes Unicode Ethiopic fonts.

%description ethiopic -l pl.UTF-8
Ten pakiet zawiera unikodowe fonty etiopskie.

%package european
Summary:	International fonts for X -- European
Summary(pl.UTF-8):	Międzynarodowe fonty dla X - europejskie
Group:		Fonts
Requires(post,postun):	fontpostinst

%description european
This package includes some ISO 8859-1 (Latin-1), ISO 8859-2 (Latin-2),
ISO 8859-3 (Latin-3), ISO 8859-4 (Latin-4), ISO 8859-5 (Cyrillic),
ISO 8859-7 (Greek), ISO 8859-8 (Hebrew), ISO 8859-9 (Latin-5), and KOI
(Cyrillic) fonts.  Also one ISO 8859-1 big font is included.

%description european -l pl.UTF-8
Ten pakiet zawiera trochę fontów ISO 8859-1 (Latin-1), ISO 8859-2
(Latin-2), ISO 8859-3 (Latin-3), ISO 8859-4 (Latin-4), ISO 8859-5
(cyrilica), ISO 8859-7 (greckie), ISO 8859-8 (hebrajkie), ISO 8859-9
(Latin-5) oraz KOI (cyrylica). Jest też dołączony jeden duży font ISO
8859-1.

%package hebrew
Summary:	International fonts for X -- Hebrew
Summary(pl.UTF-8):	Międzynarodowe fonty dla X - hebrajskie
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{name} = %{version}-%{release}
Requires:	%{_fontsdir}/Misc

%description hebrew
This package includes some Hebrew fonts.

%description hebrew -l pl.UTF-8
Ten pakiet zawiera trochę fontów hebrajskich.

%package japanese
Summary:	International fonts for X -- Japanese
Summary(pl.UTF-8):	Międzynarodowe fonty dla X - japońskie
Group:		Fonts
Requires(post,postun):	fontpostinst

%description japanese
This package includes some JISX0208.1990, JISX0208.1978, JISX0212.1990
(HojoKanji), JISX0208.1983, and JISX0201 (Roman & Kana) Japanese
fonts.

%description japanese -l pl.UTF-8
Ten pakiet zawiera trochę japońskich fontów JISX0208.1990,
JISX0208.1978, JISX0212.1990 (HojoKanji), JISX0208.1983 oraz JISX0201
(Roman i Kana).

%package korean
Summary:	International fonts for X -- Korean
Summary(pl.UTF-8):	Międzynarodowe fonty dla X - koreańskie
Group:		Fonts
Requires(post,postun):	fontpostinst

%description korean
This package includes some KSC5601 Korean fonts.

%description korean -l pl.UTF-8
Ten pakiet zawiera trochę koreańskich fontów KSC5601.

%package phonetic
Summary:	International fonts for X -- Phonetic Alphabet
Summary(pl.UTF-8):	Międzynarodowe fonty dla X - alfabet fonetyczny
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{name} = %{version}-%{release}
Requires:	%{_fontsdir}/Misc

%description phonetic
This package includes some fonts of International Phonetic Alphabet.

%description phonetic -l pl.UTF-8
Ten pakiet zawiera trochę fontów dla międzynarodowego alfabetu
fonetycznego.

%package TrueType
Summary:	International fonts for X -- TrueType
Summary(pl.UTF-8):	Międzynarodowe fonty dla X - TrueType
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/TTF

%description TrueType
This package includes some TrueType fonts.

%description TrueType -l pl.UTF-8
Ten pakiet zawiera trochę fontów TrueType.

%package Type1
Summary:	International fonts for X -- Type1
Summary(pl.UTF-8):	Międzynarodowe fonty dla X - Type1
Group:		Fonts
Requires(post,postun):	fontpostinst >= 0.1-6
Requires:	%{_fontsdir}/Type1

%description Type1
This package includes some Type1 fonts.

%description Type1 -l pl.UTF-8
Ten pakiet zawiera trochę fontów Type1.

%package emacs
Summary:	Fonts to allow multi-lingual PostScript printing from Emacs
Summary(pl.UTF-8):	Fonty pozwalające na drukowanie wielojęzycznego PostScriptu z Emacsa
Group:		Applications/Editors/Emacs
Requires:	emacs-common

%description emacs
This package includes BDF fonts to print Amharic, Arabic, Cantonese,
Chinese, Czech, Danish, Esperanto, Estonian, Finnish, French, German,
Greek, Hebrew, Hindi, Italian, Japanese, Korean, Maltese, Nederlands,
Norwegian, Polish, Russian, Slovak, Spanish, Swedish, Thai, Tigrigna,
Turkish and Vietnamese text as bit-mapped PostScript.  To see these
languages in X, you can use the intlfonts-* packages (among others).

%description emacs -l pl.UTF-8
Ten pakiet zawiera fonty BDF pozwalające na drukowanie do bitmapowego
PostScriptu tekstów w językach: amharskim, arabskim, kantońskim,
chińskim, czeskim, duńskim, esperanto, estońskim, fińskim, francuskim,
niemieckim, greckim, hebrajskim, hindi, włoskim, japońskim,
koreańskim, maltańskim, holenderskim, norweskim, polskim, rosyjskim,
słowackim, hiszpańskim, szwedzkim, tajskim, tigrinia, tureckim i
wietnamskim. Aby zobaczyć te języki pod X, można użyć pakietów
intlfonts-* (i innych).

%prep
%setup -q
%patch0 -p1

%{__mv} Chinese.X/README{,.X}
%{__mv} European.BIG/README{,.BIG}
%{__mv} Japanese.BIG/README{,.BIG}
%{__mv} Japanese.X/README{,.X}
%{__mv} Misc/README{,.Misc}

%build
%configure \
	--enable-compress \
	--with-fontdir=%{_fontsdir} \
	--with-truetype \
	--with-type1 \
	--without-bdf

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/emacs/fonts/bdf

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{t1afmdir}
%{__mv} $RPM_BUILD_ROOT%{t1fontsdir}/*.afm $RPM_BUILD_ROOT%{t1afmdir}
%{__rm} $RPM_BUILD_ROOT%{t1fontsdir}/*.pfa

%{__mv} $RPM_BUILD_ROOT%{_fontsdir}/TrueType $RPM_BUILD_ROOT%{ttffontsdir}

cd $RPM_BUILD_ROOT%{t1fontsdir}
/usr/bin/type1inst
tail -n +2 fonts.scale > fonts.scale.intl
%{__mv} Fontmap Fontmap.intl
%{__rm} fonts.dir fonts.scale type1inst.log
cd -

touch $RPM_BUILD_ROOT%{_fontsdir}/{Misc,Asian,Chinese,Ethiopic,European,Japanese,Korean}/fonts.dir

cp -p `find -name '*.bdf'` $RPM_BUILD_ROOT%{_datadir}/emacs/fonts/bdf

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

%post korean
fontpostinst misc %{_fontsdir}/Korean

%postun korean
fontpostinst misc %{_fontsdir}/Korean

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
%doc ChangeLog NEWS README Misc/README.Misc
%dir %{_fontsdir}/Misc
%{_fontsdir}/Misc/bmp16-etl.pcf.gz
%ghost %{_fontsdir}/Misc/fonts.dir

%files arabic
%defattr(644,root,root,755)
%{_fontsdir}/Misc/arab*-*-etl.pcf.gz

%files asian
%defattr(644,root,root,755)
%doc Asian/README
%dir %{_fontsdir}/Asian
%{_fontsdir}/Asian/ind*-mule.pcf.gz
%{_fontsdir}/Asian/ind*-uni.pcf.gz
%{_fontsdir}/Asian/isci*-mule.pcf.gz
%{_fontsdir}/Asian/lao*-mule.pcf.gz
%{_fontsdir}/Asian/thai*.pcf.gz
%{_fontsdir}/Asian/tib*-mule.pcf.gz
%{_fontsdir}/Asian/visc*-etl.pcf.gz
%{_fontsdir}/Asian/xtis*.pcf.gz
%{_fontsdir}/Asian/fonts.alias
%ghost %{_fontsdir}/Asian/fonts.dir

%files chinese
%defattr(644,root,root,755)
%doc Chinese/README Chinese.X/README.X
%dir %{_fontsdir}/Chinese
%{_fontsdir}/Chinese/gb*.pcf.gz
%{_fontsdir}/Chinese/guob*.pcf.gz
%{_fontsdir}/Chinese/sish*-etl.pcf.gz
%{_fontsdir}/Chinese/taipei*.pcf.gz
%{_fontsdir}/Chinese/fonts.alias
%ghost %{_fontsdir}/Chinese/fonts.dir

%files ethiopic
%defattr(644,root,root,755)
%doc Ethiopic/README
%dir %{_fontsdir}/Ethiopic
%{_fontsdir}/Ethiopic/ethio*-uni.pcf.gz
%ghost %{_fontsdir}/Ethiopic/fonts.dir

%files european
%defattr(644,root,root,755)
%doc European/README European.BIG/README.BIG
%dir %{_fontsdir}/European
%{_fontsdir}/European/cyr*-etl.pcf.gz
%{_fontsdir}/European/grk*-etl.pcf.gz
%{_fontsdir}/European/koi*-etl.pcf.gz
%{_fontsdir}/European/lt1-*.pcf.gz
%{_fontsdir}/European/lt2-*-etl.pcf.gz
%{_fontsdir}/European/lt3-*-etl.pcf.gz
%{_fontsdir}/European/lt4-*-etl.pcf.gz
%{_fontsdir}/European/lt5-*-etl.pcf.gz
%{_fontsdir}/European/fonts.alias
%ghost %{_fontsdir}/European/fonts.dir

%files hebrew
%defattr(644,root,root,755)
%{_fontsdir}/Misc/heb*-etl.pcf.gz

%files japanese
%defattr(644,root,root,755)
%doc Japanese/README Japanese.BIG/README.BIG Japanese.X/README.X
%dir %{_fontsdir}/Japanese
%{_fontsdir}/Japanese/*x*rk.pcf.gz
%{_fontsdir}/Japanese/a18rk*.pcf.gz
%{_fontsdir}/Japanese/j*-*.pcf.gz
%{_fontsdir}/Japanese/jiskan*.pcf.gz
%{_fontsdir}/Japanese/jksp*.pcf.gz
%{_fontsdir}/Japanese/k14.pcf.gz
%{_fontsdir}/Japanese/fonts.alias
%ghost %{_fontsdir}/Japanese/fonts.dir

%files korean
%defattr(644,root,root,755)
%doc Korean.X/README
%dir %{_fontsdir}/Korean
%{_fontsdir}/Korean/hangl*.pcf.gz
%ghost %{_fontsdir}/Korean/fonts.dir

%files phonetic
%defattr(644,root,root,755)
%{_fontsdir}/Misc/ipa*-etl.pcf.gz

%files TrueType
%defattr(644,root,root,755)
%doc TrueType/README
%{_fontsdir}/TTF/lt1-*-omega-serif.ttf
%{_fontsdir}/TTF/lt2-*-omega-serif.ttf
%{_fontsdir}/TTF/lt3-*-omega-serif.ttf
%{_fontsdir}/TTF/lt4-*-omega-serif.ttf
%{_fontsdir}/TTF/lt5-*-omega-serif.ttf
%{_fontsdir}/TTF/viscii-omega-serif.ttf

%files Type1
%defattr(644,root,root,755)
%doc Type1/README
%{_fontsdir}/Type1/lt1-*-omega-serif.pfb
%{_fontsdir}/Type1/lt2-*-omega-serif.pfb
%{_fontsdir}/Type1/lt3-*-omega-serif.pfb
%{_fontsdir}/Type1/lt4-*-omega-serif.pfb
%{_fontsdir}/Type1/lt5-*-omega-serif.pfb
%{_fontsdir}/Type1/nf3*.pfb
%{_fontsdir}/Type1/tis620-*-omega-serif.pfb
%{_fontsdir}/Type1/viscii-*-omega-serif.pfb
%{_fontsdir}/Type1/Fontmap.intl
%{_fontsdir}/Type1/fonts.scale.intl
%{_fontsdir}/Type1/afm/lt1-*-omega-serif.afm
%{_fontsdir}/Type1/afm/lt2-*-omega-serif.afm
%{_fontsdir}/Type1/afm/lt3-*-omega-serif.afm
%{_fontsdir}/Type1/afm/lt4-*-omega-serif.afm
%{_fontsdir}/Type1/afm/lt5-*-omega-serif.afm
%{_fontsdir}/Type1/afm/nf3*.afm
%{_fontsdir}/Type1/afm/tis620-*-omega-serif.afm
%{_fontsdir}/Type1/afm/viscii-*-omega-serif.afm

%files emacs
%defattr(644,root,root,755)
%{_datadir}/emacs/fonts
