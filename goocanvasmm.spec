%define api 0.1
%define major 2
%define libname %mklibname %{name} %{api} %{major}
%define develname %mklibname %{name} -d

Summary:	C++ wrappers for goocanvas
Name:		goocanvasmm
Version:	0.6.0
Release:	%mkrel 1
License:	LGPLv2+
Group:		System/Libraries
URL:		http://www.gtkmm.org
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%name/0.6/%name-%version.tar.bz2
BuildRequires:	gtkmm2.4-devel
BuildRequires:	goocanvas-devel
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
%{_libdir}/lib*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/pkgconfig/*.pc
%{_includedir}/%{name}-%{api}
%{_libdir}/%{name}-%{api}/include
%{_libdir}/%{name}-%{api}/proc/m4/*.m4
