%define	fversion	%(echo %{version} | tr r - )
Summary:	Cross-platform library for OpenGL rendering
Summary(pl):	Wieloplatformowa biblioteka do renderingu OpenGL
Name:		Producer
Version:	0.8.4r2
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://www.andesengineering.com/Producer/Download/%{name}-%{fversion}.tar.gz
# Source0-md5:	9e14c27a0e927a19bb3666fa73755652
Patch0:		%{name}-soname.patch
URL:		http://www.andesengineering.com/Producer/index.html
Provides:	OpenProducer = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Open Producer (or simply Producer) is a cross-platform, C++ library
for managing OpenGL rendering contexts in a windowing system
independent manner. Producer provides a simple, yet powerfully
scalable approach for real-time 3D applications wishing to run within
a single window to large, multidisplay systems. Producer is highly
portable and has been tested on Linux, Windows, Mac OSX, Solaris and
IRIX. Producer works on all Unix based OS's (including Mac OSX)
through the X11 Windowing system, and through the native win32 on
Windows. Producer is written with productivity, performance and
scalability in mind by adhering to industry standard and employing
advanced software engineering practices. Software developers wishing
to produce 3D rendering software that can display on a desktop, and
move to a large system or clustered system of displays by simply
changing a configuration file, can depend on Open Producer to handle
all the complexity for them.

%package devel
Summary:	Devel files for Producent
Summary(pl):	Pliki developerskie dla Producer
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Devel files for Producent.

%description devel -l pl
Biblioteki programistyczne dla Producent.

%prep
%setup -q -n %{name}
%patch0 -p0

find -type d -name CVS |xargs rm -rf

%build
%{__make} \
	CXX="%{__cxx} %{rpmcflags} -fPIC -fpermissive"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	 INST_LOCATION=$RPM_BUILD_ROOT%{_prefix}
ln -sf `basename $RPM_BUILD_ROOT%{_libdir}/lib%{name}.so.*` $RPM_BUILD_ROOT%{_libdir}/lib%{name}.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*

%files devel
%defattr(644,root,root,755)
%doc README.txt doc
%{_includedir}/%{name}
%attr(755,root,root) %{_libdir}/lib*.so
