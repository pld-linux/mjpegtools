Summary:	Tools for recording, editing, playing back and MPEG-encoding video under Linux
Summary(pl):	Narzêdzia do nagrywania, edycji, odtwarzania i kodowania do MPEG obrazu
Name:		mjpegtools
Version:	1.6.0
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://prdownloads.sourceforge.net/mjpeg/%{name}-%{version}.tar.gz
URL:		http://mjpeg.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The MJPEG-tools are a basic set of utilities for recording, editing,
playing back and encoding (to MPEG) video under Linux. Recording can
be done with Zoran-based MJPEG-boards (LML33, Iomega Buz, Pinnacle
DC10(+), Marvel G200/G400), these can also playback video using the
hardware. With the rest of the tools, this video can be edited and
encoded into MPEG 1/2 or DivX video.

%description -l pl
MPEG-tools to podstawowy zestaw narzêdzi do nagrywania, edycji,
odtwarzania i kodowania (do MPEG) obrazu pod Linuksem. Nagrywaæ mo¿na
przy u¿yciu kart MJPEG opartych na Zoranie (LML33, Iomega Buz,
Pinnacle DC10(+), Marvel G200/G400), na nich mo¿na tak¿e odtwarzaæ
obraz ze wsparciem sprzêtowym. Przy pomocy pozosta³ych narzêdzi obraz
mo¿na obrabiaæ i kodowaæ do formatu MPEG 1/2 lub DivX.

%package devel
Summary:	Development headers for the mjpegtools
Summary(pl):	Pliki nag³ówkowe mjpegtools
Group:		Development/Libraries
Requires:	%{name} = %{version}

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

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS CHANGES HINTS PLANS README TODO
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
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_mandir}/man1/*
%{_mandir}/man5/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*-config
%dir %{_includedir}/mjpegtools
%{_includedir}/mjpegtools/*.h
%{_pkgconfigdir}/*.pc
%{_libdir}/lib*.la
%{_libdir}/lib*.so

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
