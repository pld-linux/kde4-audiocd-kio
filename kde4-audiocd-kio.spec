%define		_state		stable
%define		orgname		audiocd-kio
%define		qtver		4.8.1

Summary:	Audiocd protocol for konqueror
Summary(pl.UTF-8):	Protokół audiocd dla konquerora
Name:		kde4-%{orgname}
Version:	4.14.3
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://download.kde.org/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	f298189165b4c864527090b50beb904d
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cdparanoia-III-devel
BuildRequires:	cmake >= 2.8.0
BuildRequires:	flac-devel >= 1.1.2
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	kde4-libkcddb-devel
BuildRequires:	kde4-libkcompactdisc-devel
BuildRequires:	libogg-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libvorbis-devel
BuildRequires:	phonon-devel >= 4.4.1
BuildRequires:	pkgconfig
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.600
Requires:	kde4-libkcddb >= %{version}
Requires:	kde4-konqueror >= %{version}
Provides:	kdemultimedia(audiocd) = %{version}-%{release}
Obsoletes:	kde4-kdemultimedia-audiocd < 4.8.99-1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package allows konqueror to play audiocd's without the need of an
external application. Just enter audiocd:/ in the location field.

%description -l pl.UTF-8
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
%{_datadir}/config.kcfg/audiocd_*_encoder.kcfg
%{_datadir}/kde4/services/audiocd.protocol
%{_datadir}/kde4/services/audiocd.desktop
%{_datadir}/apps/solid/actions/solid_audiocd.desktop
%{_datadir}/apps/konqsidebartng/virtual_folders/services/audiocd.desktop
%lang(en) %{_kdedocdir}/en/kioslave/audiocd
