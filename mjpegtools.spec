Name:		mjpegtools
Version:	1.6.0
Release:	1
Summary:	Tools for recording, editing, playing back and mpeg-encoding video under linux
License:	GPL
Group:		Libraries
Source0:	http://prdownloads.sourceforge.net/mjpeg/%{name}-%{version}.tar.gz
URL:		http://mjpeg.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The MJPEG-tools are a basic set of utilities for recording, editing,
playing back and encoding (to mpeg) video under linux. Recording can
be done with zoran-based MJPEG-boards (LML33, Iomega Buz, Pinnacle
DC10(+), Marvel G200/G400), these can also playback video using the
hardware. With the rest of the tools, this video can be edited and
encoded into mpeg1/2 or divx video.

%package devel
Summary:	Development headers and libraries for the mjpegtools
Group:		Development/Libraries

%description devel
This package contains static libraries and C system header files
needed to compile applications that use part of the libraries of the
mjpegtools package.

%package static
Summary:	Static libraries for mjpegtools
Group:		Development/Libraries

%description static
Static libraries for mjpegtools

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%post
/sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS CHANGES COPYING HINTS PLANS README TODO
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
%{_libdir}/*.so.*
%{_mandir}/man1/*
%{_mandir}/man5/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*-config
%{_includedir}/mjpegtools/*.h
%{_pkgconfigdir}/*.pc
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so
