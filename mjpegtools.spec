#
# Conditional build:
%bcond_without	quicktime	# without Quicktime playback/recording support
#
Summary:	Tools for recording, editing, playing back and MPEG-encoding video under Linux
Summary(pl.UTF-8):	Narzędzia do nagrywania, edycji, odtwarzania i kodowania do MPEG obrazu
Name:		mjpegtools
Version:	2.0.0
Release:	2
License:	GPL v2+
Group:		Applications/Graphics
Source0:	http://downloads.sourceforge.net/mjpeg/%{name}-%{version}.tar.gz
# Source0-md5:	903e1e3b967eebcc5fe5626d7517dc46
Patch0:		%{name}-opt.patch
Patch1:		%{name}-pthread.patch
Patch2:		%{name}-config.h.patch
URL:		http://mjpeg.sourceforge.net/
BuildRequires:	SDL-devel >= 1.1.3
BuildRequires:	SDL_gfx-devel
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1:1.7
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	libdv-devel >= 0.9.5
BuildRequires:	libjpeg-devel >= 6b
BuildRequires:	libpng-devel
%{?with_quicktime:BuildRequires:	libquicktime-devel >= 0.9.7}
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libX11-devel
# only checked for, not used for anything
#BuildRequires:	xorg-lib-libXxf86dga-devel
Requires:	%{name}-libs = %{version}-%{release}
Obsoletes:	libmjpegtools0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The MJPEG-tools are a basic set of utilities for recording, editing,
playing back and encoding (to MPEG) video under Linux. Recording can
be done with Zoran-based MJPEG-boards (LML33, Iomega Buz, Pinnacle
DC10(+), Marvel G200/G400), these can also playback video using the
hardware. With the rest of the tools, this video can be edited and
encoded into MPEG 1/2 or DivX video.

%description -l pl.UTF-8
MJPEG-tools to podstawowy zestaw narzędzi do nagrywania, edycji,
odtwarzania i kodowania (do MPEG) obrazu pod Linuksem. Nagrywać można
przy użyciu kart MJPEG opartych na Zoranie (LML33, Iomega Buz,
Pinnacle DC10(+), Marvel G200/G400), na nich można także odtwarzać
obraz ze wsparciem sprzętowym. Przy pomocy pozostałych narzędzi obraz
można obrabiać i kodować do formatu MPEG 1/2 lub DivX.

%package libs
Summary:	MJPEG-tools shared libraries
Summary(pl.UTF-8):	Biblioteki współdzielone MJPEG-tools
Group:		Libraries
Requires:	libquicktime >= 0.9.7

%description libs
MJPEG-tools shared libraries.

%description libs -l pl.UTF-8
Biblioteki współdzielone MJPEG-tools.

%package devel
Summary:	Development headers for the mjpegtools
Summary(pl.UTF-8):	Pliki nagłówkowe mjpegtools
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Obsoletes:	libmjpegtools0-devel
# libmjpegutils has no additional deps
# liblavfile R: libquicktime-devel >= 0.9.7 libdv-devel
# liblavjpeg R: libjpeg-devel
# liblavplay R: SDL-devel xorg-lib-libX11-devel +liblavfile,liblavjpeg
# liblavrec R: +liblavfile,liblavjpeg
# libmpeg2encpp R: libstdc++-devel
# libmplex2 R: libstdc++-devel

%description devel
This package contains C system header files needed to compile
applications that use part of the libraries of the mjpegtools package.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe C potrzebne do kompilowania
aplikacji używających części bibliotek z pakietu mjpegtools.

%package static
Summary:	Static libraries for mjpegtools
Summary(pl.UTF-8):	Statyczne biblioteki mjpegtools
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libraries for mjpegtools.

%description static -l pl.UTF-8
Statyczne biblioteki mjpegtools.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	PTHREAD_LIBS="-lpthread" \
	%{!?with_quicktime:--without-libquicktime} \
%ifarch ppc
	--disable-simd-accel
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.glav README.lavpipe README.transist
%attr(755,root,root) %{_bindir}/anytovcd.sh
%attr(755,root,root) %{_bindir}/glav
%attr(755,root,root) %{_bindir}/jpeg2yuv
%attr(755,root,root) %{_bindir}/lav*
%attr(755,root,root) %{_bindir}/matteblend.flt
%attr(755,root,root) %{_bindir}/mjpeg_simd_helper
%attr(755,root,root) %{_bindir}/mp2enc
%attr(755,root,root) %{_bindir}/mpeg2enc
%attr(755,root,root) %{_bindir}/mpegtranscode
%attr(755,root,root) %{_bindir}/mplex
%attr(755,root,root) %{_bindir}/multiblend.flt
%attr(755,root,root) %{_bindir}/pgmtoy4m
%attr(755,root,root) %{_bindir}/png2yuv
%attr(755,root,root) %{_bindir}/pnmtoy4m
%attr(755,root,root) %{_bindir}/ppmtoy4m
%attr(755,root,root) %{_bindir}/qttoy4m
%attr(755,root,root) %{_bindir}/transist.flt
%attr(755,root,root) %{_bindir}/y4m*
%attr(755,root,root) %{_bindir}/ypipe
%attr(755,root,root) %{_bindir}/yuv*
%attr(755,root,root) %{_bindir}/yuyvtoy4m
%{_mandir}/man1/jpeg2yuv.1*
%{_mandir}/man1/lav*.1*
%{_mandir}/man1/mjpegtools.1*
%{_mandir}/man1/mp2enc.1*
%{_mandir}/man1/mpeg2enc.1*
%{_mandir}/man1/mplex.1*
%{_mandir}/man1/pgmtoy4m.1*
%{_mandir}/man1/png2yuv.1*
%{_mandir}/man1/pnmtoy4m.1*
%{_mandir}/man1/ppmtoy4m.1*
%{_mandir}/man1/y4m*.1*
%{_mandir}/man1/yuv*.1*
%{_infodir}/mjpeg-howto.info*

%files libs
%defattr(644,root,root,755)
%doc AUTHORS BUGS CHANGES HINTS PLANS README README.DV README.avilib TODO
%attr(755,root,root) %{_libdir}/liblavfile-2.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liblavfile-2.0.so.0
%attr(755,root,root) %{_libdir}/liblavjpeg-2.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liblavjpeg-2.0.so.0
%attr(755,root,root) %{_libdir}/liblavplay-2.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liblavplay-2.0.so.0
%attr(755,root,root) %{_libdir}/libmjpegutils-2.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmjpegutils-2.0.so.0
%attr(755,root,root) %{_libdir}/libmpeg2encpp-2.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmpeg2encpp-2.0.so.0
%attr(755,root,root) %{_libdir}/libmplex2-2.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmplex2-2.0.so.0
%{_mandir}/man5/yuv4mpeg.5*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblavfile.so
%attr(755,root,root) %{_libdir}/liblavjpeg.so
%attr(755,root,root) %{_libdir}/liblavplay.so
%attr(755,root,root) %{_libdir}/libmjpegutils.so
%attr(755,root,root) %{_libdir}/libmpeg2encpp.so
%attr(755,root,root) %{_libdir}/libmplex2.so
%{_libdir}/liblavfile.la
%{_libdir}/liblavjpeg.la
%{_libdir}/liblavplay.la
%{_libdir}/libmjpegutils.la
%{_libdir}/libmpeg2encpp.la
%{_libdir}/libmplex2.la
%{_includedir}/mjpegtools
%{_pkgconfigdir}/mjpegtools.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/liblavfile.a
%{_libdir}/liblavjpeg.a
%{_libdir}/liblavplay.a
%{_libdir}/libmjpegutils.a
%{_libdir}/libmpeg2encpp.a
%{_libdir}/libmplex2.a
