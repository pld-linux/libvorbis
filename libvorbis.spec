Summary:	The Vorbis General Audio Compression Codec
Summary(pl):	Kodek kompresji audio - Vorbis
Summary(pt_BR):	Biblioteca libvorbis versão 1.0
Summary(ru):	ëÏÄÅË Ú×ÕËÏ×ÏÊ ËÏÍÐÒÅÓÓÉÉ Vorbis
Summary(uk):	ëÏÄÅË Ú×ÕËÏ×Ï§ ËÏÍÐÒÅÓ¦§ Vorbis
Name:		libvorbis
Version:	1.0
Release:	3
Epoch:		1
License:	GPL
Group:		Development/Libraries
Source0:	http://www.xiph.org/ogg/vorbis/download/%{name}-%{version}.tar.gz
Patch0:		%{name}-ac_fixes.patch
Patch1:		%{name}-make.patch
URL:		http://www.xiph.org/ogg/
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	libtool
BuildRequires:	libogg-devel >= 2:1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libvorbis0

%description
Ogg Vorbis is a fully open, non-proprietary, patent-and-royalty-free,
general-purpose compressed audio format for audio and music at fixed
and variable bitrates from 16 to 128 kbps/channel.

%description -l pl
Ogg Vorbis jest ca³kowicie otwartym, nie bêd±cym niczyj± w³asno¶ci±,
wolnym od patentów, ogólnego przeznaczenia kodekiem audio i muzyki o
sta³ej i zmiennej bitrate od 16 do 128 kbps/kana³.

%description -l ru
Ogg Vorbis - ÜÔÏ ÐÏÌÎÏÓÔØÀ ÏÔËÒÙÔÙÊ, Ó×ÏÂÏÄÎÙÊ ÏÔ ÐÁÔÅÎÔÏ× É Á×ÔÏÒÓËÉÈ
ÏÔÞÉÓÌÅÎÉÊ ÆÏÒÍÁÔ ÓÖÁÔÉÑ ÁÕÄÉÏÄÁÎÎÙÈ Ó ÆÉËÓÉÒÏ×ÁÎÎÙÍ É ÉÚÍÅÎÑÀÝÉÍÓÑ
ÂÉÔÒÅÊÔÏÍ ÏÔ 16 ÄÏ 128 ËÉÌÏÂÉÔ × ÓÅËÕÎÄÕ ÎÁ ËÁÎÁÌ.

%description -l uk
Ogg Vorbis - ÃÅ ÐÏ×Î¦ÓÔÀ ×¦ÄËÒÉÔÉÊ, ×¦ÌØÎÉÊ ×¦Ä ÐÁÔÅÎÔ¦× ÔÁ Á×ÔÏÒÓØËÉÈ
×¦ÄÒÁÈÕ×ÁÎØ ÆÏÒÍÁÔ ËÏÍÐÒÅÓÏ×ÁÎÏÇÏ ÁÕÄ¦Ï Ú Æ¦ËÓÏ×ÁÎÉÍ ÔÁ ÚÍ¦ÎÎÉÍ
Â¦ÔÒÅÊÔÏÍ ×¦Ä 16 ÄÏ 128 Ë¦ÌÏÂ¦Ô × ÓÅËÕÎÄÕ ÎÁ ËÁÎÁÌ.

%description -l pt_BR
Ogg Vorbis e' um formato de áudio aberto de propósito geral,
não-proprietário e isento de patentes e royalties, para áudio e musica
de alta qualidade (44.1-48.0kHz, 16+ bit, polifonico) com bitrate fixo
ou variável de 16 a 128 kbps/canal. Isso coloca Vorbis na mesma
categoria de MPEG-1 audio layer 3, MPEG-3 audio (AAC e TwinVQ) e PAQ.

%package devel
Summary:	Development files for OGG Vorbis library
Summary(pl):	Pliki nag³ówkowe i dokumentacja developerska
Summary(pt_BR):	Bibliotecas para desenvolvimento com o vorbis
Summary(ru):	âÉÂÌÉÏÔÅËÁ Vorbis - òÁÚÒÁÂÏÔËÁ
Summary(uk):	â¦ÂÌ¦ÏÔÅËÁ Vorbis - òÏÚÒÏÂËÁ
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	libogg-devel
Obsoletes:	libvorbis0-devel

%description devel
The libvorbis-devel package contains the header files and
documentation needed to develop applications with libvorbis.

%description devel -l pl
Pliki nag³ówkowe i dokumentacja developerska potrzebna do rozwijania
aplikacji korzystaj±cych z biblioteki libvorbis.

%description devel -l pt_BR
Bibliotecas e arquivos de inclusão para desenvolvimento com o codec
Vorbis.

%description devel -l ru
ðÁËÅÔ libvorbis-devel ÓÏÄÅÒÖÉÔ ÆÁÊÌÙ ÚÁÇÏÌÏ×ËÏ× É ÄÏËÕÍÅÎÔÁÃÉÀ ÄÌÑ
ÒÁÚÒÁÂÏÔËÉ ÐÒÏÇÒÁÍÍ Ó libvorbis.

%description devel -l uk
ðÁËÅÔ libvorbis-devel Í¦ÓÔÉÔØ ÆÁÊÌÉ ÚÁÇÏÌÏ×Ë¦× ÔÁ ÄÏËÕÍÅÎÔÁÃ¦À ÄÌÑ
ÒÏÚÒÏÂËÉ ÐÒÏÇÒÁÍ Ú libvorbis.

%package static
Summary:	Static development library for OGG Vorbis
Summary(es):	Bibliotecas estáticas
Summary(pl):	Biblioteka statyczna OGG Vorbis
Summary(pt_BR):	Bibliotecas estáticas para desenvolvimento com o vorbis
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
The libvorbis-static package contains the static libraries of
libvorbis.

%description static -l pl
Biblioteka statyczna OGG Vorbis.

%description static -l pt_BR
Bibliotecas estáticas para desenvolvimento com o codec Vorbis.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

# temporary workaround for gcc 2.91-2.95.4 bug:
%ifarch i686
sed -e 's@-mno-ieee-fp@ @g' configure.in > configure.in.new
mv -f configure.in.new configure.in
%endif

%build
rm -f missing
%{__libtoolize}
aclocal
%{__autoconf}
%{__automake}
%configure \
	--enable-shared \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

rm -f doc/Makefile* doc/*/Makefile*

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc README doc/*
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/vorbis
%{_aclocaldir}/*.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
