Summary:	Development library for OGG Vorbis
Name:		libvorbis
Version:	1.0.0_cvs2000.10.29
Release:	1
License:	GPL
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Source0:	ftp://www.xiph.org/ogg/vorbis/download/vorbis_nightly_cvs.tgz
Patch0:		%{name}-make.patch
URL:		http://progen.dynodns.net/dengen/clean_theme.html
BuildRequires:	libogg-static
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description 
Ogg Vorbis is a fully Open, non-proprietary, patent-and-royalty-free,
general-purpose compressed audio format for high quality
(44.1-48.0kHz, 16+ bit, polyphonic) audio and music at fixed and
variable bitrates from 16 to 128 kbps/channel. This places Vorbis in
the same class as audio representations including MPEG-1 audio layer
3, MPEG-4 audio (AAC and TwinVQ), and PAC.

%package devel
Summary:	Development files for OGG Vorbis library
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki

%description devel
Ogg Vorbis is a fully Open, non-proprietary, patent-and-royalty-free,
general-purpose compressed audio format for high quality
(44.1-48.0kHz, 16+ bit, polyphonic) audio and music at fixed and
variable bitrates from 16 to 128 kbps/channel. This places Vorbis in
the same class as audio representations including MPEG-1 audio layer
3, MPEG-4 audio (AAC and TwinVQ), and PAC.

%package static
Summary:	Static development library for OGG Vorbis
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki

%description static
Ogg Vorbis is a fully Open, non-proprietary, patent-and-royalty-free,
general-purpose compressed audio format for high quality
(44.1-48.0kHz, 16+ bit, polyphonic) audio and music at fixed and
variable bitrates from 16 to 128 kbps/channel. This places Vorbis in
the same class as audio representations including MPEG-1 audio layer
3, MPEG-4 audio (AAC and TwinVQ), and PAC.

%prep
%setup -q -n vorbis
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_libdir}/lib*.la

%files devel
%defattr(644,root,root,755)
%doc doc/*.{png,html} *.gz
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/vorbis

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
