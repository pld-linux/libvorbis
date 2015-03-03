Summary:	The Vorbis General Audio Compression Codec
Summary(pl.UTF-8):	Kodek kompresji audio - Vorbis
Summary(pt_BR.UTF-8):	Biblioteca libvorbis
Summary(ru.UTF-8):	Кодек звуковой компрессии Vorbis
Summary(uk.UTF-8):	Кодек звукової компресії Vorbis
Name:		libvorbis
Version:	1.3.5
Release:	1
Epoch:		1
License:	BSD
Group:		Libraries
Source0:	http://downloads.xiph.org/releases/vorbis/%{name}-%{version}.tar.xz
# Source0-md5:	28cb28097c07a735d6af56e598e1c90f
Patch0:		%{name}-ac_fixes.patch
Patch1:		%{name}-make.patch
URL:		http://www.vorbis.com/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.6
BuildRequires:	gcc >= 5:3.0
BuildRequires:	libogg-devel >= 2:1.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	libogg >= 2:1.0
Obsoletes:	libvorbis0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ogg Vorbis is a fully open, non-proprietary, patent-and-royalty-free,
general-purpose compressed audio format for audio and music at fixed
and variable bitrates from 16 to 128 kbps/channel.

%description -l pl.UTF-8
Ogg Vorbis jest całkowicie otwartym, nie będącym niczyją własnością,
wolnym od patentów, ogólnego przeznaczenia kodekiem audio i muzyki o
stałej i zmiennej bitrate od 16 do 128 kbps/kanał.

%description -l ru.UTF-8
Ogg Vorbis - это полностью открытый, свободный от патентов и авторских
отчислений формат сжатия аудиоданных с фиксированным и изменяющимся
битрейтом от 16 до 128 килобит в секунду на канал.

%description -l uk.UTF-8
Ogg Vorbis - це повністю відкритий, вільний від патентів та авторських
відрахувань формат компресованого аудіо з фіксованим та змінним
бітрейтом від 16 до 128 кілобіт в секунду на канал.

%description -l pt_BR.UTF-8
Ogg Vorbis e' um formato de áudio aberto de propósito geral,
não-proprietário e isento de patentes e royalties, para áudio e musica
de alta qualidade (44.1-48.0kHz, 16+ bit, polifonico) com bitrate fixo
ou variável de 16 a 128 kbps/canal. Isso coloca Vorbis na mesma
categoria de MPEG-1 audio layer 3, MPEG-3 audio (AAC e TwinVQ) e PAQ.

%package devel
Summary:	Development files for Ogg Vorbis library
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja developerska
Summary(pt_BR.UTF-8):	Bibliotecas para desenvolvimento com o Vorbis
Summary(ru.UTF-8):	Библиотека Vorbis - Разработка
Summary(uk.UTF-8):	Бібліотека Vorbis - Розробка
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	libogg-devel >= 2:1.0
Obsoletes:	libvorbis0-devel

%description devel
The libvorbis-devel package contains the header files and
documentation needed to develop applications with libvorbis.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja developerska potrzebna do rozwijania
aplikacji korzystających z biblioteki libvorbis.

%description devel -l pt_BR.UTF-8
Bibliotecas e arquivos de inclusão para desenvolvimento com o codec
Vorbis.

%description devel -l ru.UTF-8
Пакет libvorbis-devel содержит файлы заголовков и документацию для
разработки программ с libvorbis.

%description devel -l uk.UTF-8
Пакет libvorbis-devel містить файли заголовків та документацію для
розробки програм з libvorbis.

%package static
Summary:	Static development library for Ogg Vorbis
Summary(es.UTF-8):	Bibliotecas estáticas
Summary(pl.UTF-8):	Biblioteka statyczna Ogg Vorbis
Summary(pt_BR.UTF-8):	Bibliotecas estáticas para desenvolvimento com o Vorbis
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
The libvorbis-static package contains the static libraries of
libvorbis.

%description static -l pl.UTF-8
Biblioteka statyczna Ogg Vorbis.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para desenvolvimento com o codec Vorbis.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

mv -f $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version} devel-docs

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES COPYING README
%attr(755,root,root) %{_libdir}/libvorbis.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libvorbis.so.0
%attr(755,root,root) %{_libdir}/libvorbisenc.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libvorbisenc.so.2
%attr(755,root,root) %{_libdir}/libvorbisfile.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libvorbisfile.so.3

%files devel
%defattr(644,root,root,755)
%doc devel-docs/*
%attr(755,root,root) %{_libdir}/libvorbis.so
%attr(755,root,root) %{_libdir}/libvorbisenc.so
%attr(755,root,root) %{_libdir}/libvorbisfile.so
%{_libdir}/libvorbis.la
%{_libdir}/libvorbisenc.la
%{_libdir}/libvorbisfile.la
%{_includedir}/vorbis
%{_aclocaldir}/vorbis.m4
%{_pkgconfigdir}/vorbis.pc
%{_pkgconfigdir}/vorbisenc.pc
%{_pkgconfigdir}/vorbisfile.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libvorbis.a
%{_libdir}/libvorbisenc.a
%{_libdir}/libvorbisfile.a
