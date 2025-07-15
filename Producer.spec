%define	fversion	%(echo %{version} | tr r - )
Summary:	Cross-platform library for OpenGL rendering
Summary(pl.UTF-8):	Wieloplatformowa biblioteka do renderingu OpenGL
Name:		Producer
Version:	0.8.5r3
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://www.andesengineering.com/Producer/Download/%{name}-%{fversion}.tar.gz
# Source0-md5:	889c99c47a3af7d8df03fb5584919cbe
Source1:	%{name}.pc
Patch0:		%{name}-soname.patch
Patch1:		%{name}-notix86.patch
URL:		http://www.andesengineering.com/Producer/index.html
BuildRequires:	OpenGL-devel
BuildRequires:	OpenThreads-devel
BuildRequires:	XFree86-devel
BuildRequires:	libstdc++-devel
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

%description -l pl.UTF-8
Open Producer (lub po prostu Producer) jest wieloplatformową
biblioteką C++ do zarządzania renderingiem OpenGL. Producer udostępnia
prostą, ale skalowalną możliwość dla aplikacji czasu rzeczywistego 3D
od chcących uruchamiać się w pojedynczym oknie aż do wielkich,
wieloekranowych systemów. Producer jest bardzo przenośny i
przetestowany na Linuksie, Windows, MacOS X, Solarisie i IRIXie.
Producer działa na wszystkich bazujących na Uniksie systemach
(włączając w to MacOS X) poprzez system okien X11 lub przez natywne
wywołania win32 na Windows. Producer był pisany z myślą o wydajności i
skalowalności uwzględniając systemy produkcyjne. Autorzy
oprogramowania chcący tworzyć aplikacje renderujące 3D, które mogą się
wyświetlać na ekranie lub przenieść na wielki system lub klaster
systemów wyświetlaczy poprzez prostą zmianę plików konfiguracyjnych,
mogą polegać na Open Producer, że obsłuży wszystko co jest potrzebne
dla nich.

%package devel
Summary:	Development files for Producer
Summary(pl.UTF-8):	Pliki programistyczne biblioteki Producer
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	OpenThreads-devel
Requires:	XFree86-devel
Requires:	libstdc++-devel

%description devel
Development files for Producent.

%description devel -l pl.UTF-8
Biblioteki programistyczne biblioteki Producer.

%prep
%setup -q -n %{name}
%patch -P0 -p1
%patch -P1 -p1

find -type d -name CVS |xargs rm -rf

%build
%{__make} \
	CXX="%{__cxx} %{rpmcflags} -fPIC -fpermissive"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INST_LOCATION=$RPM_BUILD_ROOT%{_prefix} \
	INST_LIBS=$RPM_BUILD_ROOT%{_libdir}

ln -sf `basename $RPM_BUILD_ROOT%{_libdir}/lib%{name}.so.*` $RPM_BUILD_ROOT%{_libdir}/lib%{name}.so

install -d $RPM_BUILD_ROOT%{_pkgconfigdir}
sed -e 's,^libdir=.*,libdir=%{_libdir},' %{SOURCE1} >$RPM_BUILD_ROOT%{_pkgconfigdir}/producer.pc

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc README.txt doc
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/%{name}
%{_pkgconfigdir}/*.pc
