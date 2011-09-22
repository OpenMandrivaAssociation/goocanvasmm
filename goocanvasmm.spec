%define api 1.0
%define major 5
%define libname %mklibname %{name} %{api} %{major}
%define develname %mklibname %{name} -d

Summary:	C++ wrappers for goocanvas
Name:		goocanvasmm
Version:	0.15.4
Release:	%mkrel 2
License:	LGPLv2+
Group:		System/Libraries
URL:		http://www.gtkmm.org
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%name/%name-%version.tar.bz2
BuildRequires:	gtkmm2.4-devel
BuildRequires:	goocanvas-devel >= 0.13
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

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
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libgoocanvasmm-%{api}.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/pkgconfig/%name-%api.pc
%{_includedir}/%{name}-%{api}
%{_libdir}/%{name}-%{api}/include
#%doc %_datadir/doc/%name-%api
#%_datadir/devhelp/books/%name-%api
