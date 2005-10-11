#
# Conditional build:
%bcond_without	quicktime	# without Quicktime playback/recording support
# TODO
# - configure:   - MPEG Z/Alpha                  : false
Summary:	Tools for recording, editing, playing back and MPEG-encoding video under Linux
Summary(pl):	Narz�dzia do nagrywania, edycji, odtwarzania i kodowania do MPEG obrazu
Name:		mjpegtools
Version:	1.8.0
Release:	0.1
License:	GPL
Group:		Applications/Graphics
Source0:	http://dl.sourceforge.net/mjpeg/%{name}-%{version}.tar.gz
# Source0-md5:	6fd98362310480bdaf7171e9659f165f
Patch0:		%{name}-link.patch
URL:		http://mjpeg.sourceforge.net/
BuildRequires:	SDL-devel >= 1.1.3
BuildRequires:	XFree86-devel
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1:1.7
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	libdv-devel >= 0.9.5
BuildRequires:	libjpeg-devel
BuildRequires:	libmovtar-devel >= 0.0.2
BuildRequires:	libpng-devel
%{?with_quicktime:BuildRequires:	libquicktime-devel >= 0.9.4}
BuildRequires:	libtool >= 2:1.5
BuildRequires:	pkgconfig
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

%description -l pl
MJPEG-tools to podstawowy zestaw narz�dzi do nagrywania, edycji,
odtwarzania i kodowania (do MPEG) obrazu pod Linuksem. Nagrywa� mo�na
przy u�yciu kart MJPEG opartych na Zoranie (LML33, Iomega Buz,
Pinnacle DC10(+), Marvel G200/G400), na nich mo�na tak�e odtwarza�
obraz ze wsparciem sprz�towym. Przy pomocy pozosta�ych narz�dzi obraz
mo�na obrabia� i kodowa� do formatu MPEG 1/2 lub DivX.

%package libs
Summary:	MJPEG-tools shared libraries
Summary(pl):	Biblioteki wsp�dzielone MJPEG-tools
Group:		Libraries

%description libs
MJPEG-tools shared libraries.

%description libs -l pl
Biblioteki wsp�dzielone MJPEG-tools.

%package devel
Summary:	Development headers for the mjpegtools
Summary(pl):	Pliki nag��wkowe mjpegtools
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Obsoletes:	libmjpegtools0-devel

%description devel
This package contains C system header files needed to compile
applications that use part of the libraries of the mjpegtools package.

%description devel -l pl
Ten pakiet zawiera pliki nag��wkowe C potrzebne do kompilowania
aplikacji u�ywaj�cych cz�ci bibliotek z pakietu mjpegtools.

%package static
Summary:	Static libraries for mjpegtools
Summary(pl):	Statyczne biblioteki mjpegtools
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libraries for mjpegtools.

%description static -l pl
Statyczne biblioteki mjpegtools.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-dv=/usr \
	%{!?with_quicktime:--without-libquicktime} \
%ifnarch i686 athlon
	--disable-cmov-extension \
%endif
%ifarch ppc
	--disable-simd-accel
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_infodir}/dir*

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lav*
%attr(755,root,root) %{_bindir}/yuv*
%attr(755,root,root) %{_bindir}/jpeg2yuv
%attr(755,root,root) %{_bindir}/testrec
%attr(755,root,root) %{_bindir}/y4m*
%attr(755,root,root) %{_bindir}/pgm*
%attr(755,root,root) %{_bindir}/png2yuv
%attr(755,root,root) %{_bindir}/ppm*
%attr(755,root,root) %{_bindir}/glav
%attr(755,root,root) %{_bindir}/ypipe
%attr(755,root,root) %{_bindir}/mp*
%attr(755,root,root) %{_bindir}/*.flt
%attr(755,root,root) %{_bindir}/anytovcd.sh
%attr(755,root,root) %{_bindir}/mjpeg_simd_helper
%attr(755,root,root) %{_bindir}/pnmtoy4m
%attr(755,root,root) %{_bindir}/yuyvtoy4m
%{_mandir}/man1/*
%{_infodir}/mjpeg-howto*

%files libs
%defattr(644,root,root,755)
%doc AUTHORS BUGS CHANGES HINTS PLANS README TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_mandir}/man5/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/mjpegtools
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
