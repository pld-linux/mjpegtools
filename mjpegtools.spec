Summary:	Tools for recording, editing, playing back and MPEG-encoding video under Linux
Summary(pl):	Narzêdzia do nagrywania, edycji, odtwarzania i kodowania do MPEG obrazu
Name:		mjpegtools
Version:	1.6.1
Release:	2
License:	GPL
Group:		Applications/Graphics
Source0:	http://dl.sourceforge.net/mjpeg/%{name}-%{version}.tar.gz
Patch0:		%{name}-moreshared.patch
Patch1:		%{name}-acam.patch
URL:		http://mjpeg.sourceforge.net/
BuildRequires:	SDL-devel
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	avifile-devel
BuildRequires:	gtk+-devel
BuildRequires:	libdv >= 0.9.5
BuildRequires:	libjpeg-devel
BuildRequires:	libmovtar-devel >= 0.0.2
BuildRequires:	libpng-devel
BuildRequires:	libtool
BuildRequires:	quicktime4linux-devel >= 1.4
Requires:	%{name}-libs = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoleted:	libmjpegtools0

%description
The MJPEG-tools are a basic set of utilities for recording, editing,
playing back and encoding (to MPEG) video under Linux. Recording can
be done with Zoran-based MJPEG-boards (LML33, Iomega Buz, Pinnacle
DC10(+), Marvel G200/G400), these can also playback video using the
hardware. With the rest of the tools, this video can be edited and
encoded into MPEG 1/2 or DivX video.

%description -l pl
MJPEG-tools to podstawowy zestaw narzêdzi do nagrywania, edycji,
odtwarzania i kodowania (do MPEG) obrazu pod Linuksem. Nagrywaæ mo¿na
przy u¿yciu kart MJPEG opartych na Zoranie (LML33, Iomega Buz,
Pinnacle DC10(+), Marvel G200/G400), na nich mo¿na tak¿e odtwarzaæ
obraz ze wsparciem sprzêtowym. Przy pomocy pozosta³ych narzêdzi obraz
mo¿na obrabiaæ i kodowaæ do formatu MPEG 1/2 lub DivX.

%package libs
Summary:	MJPEG-tools shared libraries
Summary(pl):	Biblioteki wspó³dzielone MJPEG-tools
Group:		Libraries

%description libs
MJPEG-tools shared libraries.

%description libs -l pl
Biblioteki wspó³dzielone MJPEG-tools.

%package devel
Summary:	Development headers for the mjpegtools
Summary(pl):	Pliki nag³ówkowe mjpegtools
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}
Obsoleted:	libmjpegtools0-devel

%description devel
This package contains C system header files needed to compile
applications that use part of the libraries of the mjpegtools package.

%description devel -l pl
Ten pakiet zawiera pliki nag³ówkowe C potrzebne do kompilowania
aplikacji u¿ywaj±cych czê¶ci bibliotek z pakietu mjpegtools.

%package static
Summary:	Static libraries for mjpegtools
Summary(pl):	Statyczne biblioteki mjpegtools
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libraries for mjpegtools.

%description static -l pl
Statyczne biblioteki mjpegtools.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-dv=/usr/X11R6/lib \
	--with-quicktime=/usr/include/quicktime \
%ifnarch i686 athlon
	--disable-cmov-extension
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lav*
%attr(755,root,root) %{_bindir}/yuv*
%attr(755,root,root) %{_bindir}/jpeg2yuv
%attr(755,root,root) %{_bindir}/divxdec
%attr(755,root,root) %{_bindir}/testrec
%attr(755,root,root) %{_bindir}/y4m*
%attr(755,root,root) %{_bindir}/ppm*
%attr(755,root,root) %{_bindir}/glav
%attr(755,root,root) %{_bindir}/ypipe
%attr(755,root,root) %{_bindir}/mp*
%attr(755,root,root) %{_bindir}/*.flt
%{_mandir}/man1/*

%files libs
%defattr(644,root,root,755)
%doc AUTHORS BUGS CHANGES HINTS PLANS README TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_mandir}/man5/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%dir %{_includedir}/mjpegtools
%{_includedir}/mjpegtools/*.h
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
