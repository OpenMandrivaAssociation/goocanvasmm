%define api 1.0
%define major 5
%define libname %mklibname %{name} %{api} %{major}
%define develname %mklibname %{name} -d

Summary:	C++ wrappers for goocanvas
Name:		goocanvasmm
Version:	0.15.4
Release:	3
License:	LGPLv2+
Group:		System/Libraries
URL:		http://www.gtkmm.org
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%name/%name-%version.tar.bz2
BuildRequires:	pkgconfig(gdkmm-2.4)
BuildRequires:	goocanvas-devel >= 0.13

%description
C++ wrappers for goocanvas.

%package -n %{libname}
Summary:	C++ wrappers for goocanvas
Group:		System/Libraries

%description -n	%{libname}
C++ wrappers for goocanvas.

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{develname}
C++ wrappers for goocanvas.

This package contains all necessary files to compile or develop
programs/libraries that use %{name}.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libgoocanvasmm-%{api}.so.%{major}*

%files -n %{develname}
%{_libdir}/*.so
%{_libdir}/pkgconfig/%name-%api.pc
%{_includedir}/%{name}-%{api}
%{_libdir}/%{name}-%{api}/include


%changelog
* Thu Sep 22 2011 Götz Waschk <waschk@mandriva.org> 0.15.4-2mdv2012.0
+ Revision: 700890
- disable docs
- rebuild

* Mon Oct 18 2010 Götz Waschk <waschk@mandriva.org> 0.15.4-1mdv2011.0
+ Revision: 586629
- update to new version 0.15.4

* Wed May 05 2010 Götz Waschk <waschk@mandriva.org> 0.15.3-1mdv2010.1
+ Revision: 542311
- update to new version 0.15.3

* Fri Apr 16 2010 Götz Waschk <waschk@mandriva.org> 0.15.2-2mdv2010.1
+ Revision: 535466
- BS bump
- update to new version 0.15.2

* Mon Sep 14 2009 Götz Waschk <waschk@mandriva.org> 0.15.1-1mdv2010.0
+ Revision: 440190
- update file list
- new version
- new API version

* Tue Jul 07 2009 Götz Waschk <waschk@mandriva.org> 0.15.0-1mdv2010.0
+ Revision: 393138
- update to new version 0.15.0

* Fri Apr 24 2009 Götz Waschk <waschk@mandriva.org> 0.14.0-1mdv2010.0
+ Revision: 368989
- new version
- new major

* Mon Dec 01 2008 Götz Waschk <waschk@mandriva.org> 0.13.0-1mdv2009.1
+ Revision: 308754
- new version
- new major
- drop patch
- update goocanvas dep

* Tue Nov 18 2008 Götz Waschk <waschk@mandriva.org> 0.12.0-2mdv2009.1
+ Revision: 304291
- fix build

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuilt against new libxcb

* Tue Oct 21 2008 Götz Waschk <waschk@mandriva.org> 0.12.0-1mdv2009.1
+ Revision: 295970
- new version
- new major
- update file list
- fix source URL

* Sat Sep 13 2008 Funda Wang <fwang@mandriva.org> 0.11.0-1mdv2009.0
+ Revision: 284483
- New version 0.11.0

* Sun Jul 27 2008 Götz Waschk <waschk@mandriva.org> 0.9.0-1mdv2009.0
+ Revision: 250615
- new version

* Wed Jun 25 2008 Funda Wang <fwang@mandriva.org> 0.6.0-1mdv2009.0
+ Revision: 229063
- import goocanvasmm


