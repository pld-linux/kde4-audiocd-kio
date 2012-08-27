%define		_state		stable
%define		orgname		audiocd-kio
%define		qtver		4.8.1

Summary:	K Desktop Environment - multimedia applications
Summary(pl.UTF-8):	K Desktop Environment - aplikacje multimedialne
Name:		kde4-kdemultimedia
Version:	4.9.0
Release:	0.1
License:	GPL v2+
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	7040f0f3335aa6d050a8f6e99148fe00
BuildRequires:	Qt3Support-devel >= %{qtver}
BuildRequires:	QtSvg-devel >= %{qtver}
BuildRequires:	QtTest-devel >= %{qtver}
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cdparanoia-III-devel
BuildRequires:	cmake >= 2.8.0
BuildRequires:	ffmpeg-devel >= 0.8
BuildRequires:	flac-devel >= 1.1.2
BuildRequires:	kde4-kdebase-workspace-devel >= %{version}
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	libmusicbrainz3-devel >= 1:3.0.0
BuildRequires:	libogg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtunepimp-devel
BuildRequires:	libvorbis-devel
BuildRequires:	phonon-devel >= 4.4.1
BuildRequires:	pkgconfig
BuildRequires:	pulseaudio-devel
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRequires:	xine-lib-devel >= 1:1.0
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%package audiocd
Summary:	Audiocd protocol for konqueror
Summary(pl.UTF-8):	Protokół audiocd dla konquerora
Group:		X11/Applications
Requires:	kde4-libkcddb = %{version}
Requires:	kde4-konqueror >= %{version}
Provides:	kdemultimedia(audiocd) = %{version}-%{release}

%description audiocd
This package allows konqueror to play audiocd's without the need of an
external application. Just enter audiocd:/ in the location field.

%description audiocd -l pl.UTF-8
Ten pakiet pozwala konquerorowi odtwarzanie płyt z muzyką bez potrzeby
używania zewnętrznej aplikacji. Po prostu wpisz audiocd:/ w pole
adresu.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

#%find_lang kio_audiocd	--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kcm_audiocd.so
%attr(755,root,root) %{_libdir}/kde4/kio_audiocd.so
%attr(755,root,root) %{_libdir}/kde4/libaudiocd_encoder*.so
%attr(755,root,root) %{_libdir}/libaudiocdplugins.so.4.*.*
%attr(755,root,root) %ghost %{_libdir}/libaudiocdplugins.so.?
%attr(755,root,root) %{_libdir}/libkcompactdisc.so.4.*.*
%attr(755,root,root) %ghost %{_libdir}/libkcompactdisc.so.?
%{_datadir}/apps/kconf_update/upgrade-metadata.sh
%{_datadir}/config.kcfg/audiocd_*_encoder.kcfg
%{_datadir}/apps/kconf_update/audiocd.upd
%{_datadir}/kde4/services/audiocd.protocol
%{_datadir}/kde4/services/audiocd.desktop
%{_datadir}/apps/solid/actions/solid_audiocd.desktop
%lang(en) %{_kdedocdir}/en/kioslave/audiocd