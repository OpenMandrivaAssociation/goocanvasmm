%define url_ver %(echo %version | cut -d. -f1,2)

%define api	2.0
%define major	6
%define libname %mklibname %{name} %{api} %{major}
%define devname %mklibname %{name} -d

Summary:	C++ wrappers for goocanvas
Name:		goocanvasmm
Version:	1.90.11
Release:	1
License:	LGPLv2+
Group:		System/Libraries
URL:		http://www.gtkmm.org
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	pkgconfig(glibmm-2.4)
BuildRequires:	pkgconfig(goocanvas-2.0)
BuildRequires:	pkgconfig(gtkmm-3.0)

%description
C++ wrappers for goocanvas.

%package -n %{libname}
Summary:	C++ wrappers for goocanvas
Group:		System/Libraries

%description -n	%{libname}
C++ wrappers for goocanvas.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{devname}
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

%files -n %{devname}
%doc %{_datadir}/devhelp/books/%{name}-%{api}
%doc %{_datadir}/doc/%{name}-%{api}
%{_includedir}/%{name}-%{api}
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}-%{api}.pc
%{_libdir}/%{name}-%{api}/include

