Summary:	The Vorbis General Audio Compression Codec
Summary(pl):	Kodek kompresji audio - Vorbis
Name:		libvorbis
Version:	1.0rc3
Release:	1
License:	GPL
Group:		Development/Libraries
Source0:	http://www.vorbis.com/files/rc2/unix/%{name}-%{version}.tar.gz
Patch0:		%{name}-ac_fixes.patch
Patch1:		%{name}-make.patch
URL:		http://www.xiph.org/ogg/
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	libtool
BuildRequires:	libogg-devel
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

%package devel
Summary:	Development files for OGG Vorbis library
Summary(pl):	Pliki nag³ówkowe i dokumentacja developerska
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

%package static
Summary:	Static development library for OGG Vorbis
Summary(pl):	Biblioteka statyczna OGG Vorbis
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
The libvorbis-static package contains the static libraries of
libvorbis.

%description static -l pl
Biblioteka statyczna OGG Vorbis.

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
libtoolize --copy --force
aclocal
autoconf
automake -a -c -f
%configure \
	--enable-shared \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/*.{png,html} *.gz
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/vorbis
%{_aclocaldir}/*.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
