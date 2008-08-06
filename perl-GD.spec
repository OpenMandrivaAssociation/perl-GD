%define module GD
%define name	perl-%{module}
%define version 2.39
%define release %mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	A perl5 interface to Thomas Boutell's gd library
License:	Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/GD/%{module}-%{version}.tar.bz2
BuildRequires:	gd-devel
BuildRequires:	libpng-devel
BuildRequires:	zlib-devel
BuildRequires:	freetype-devel
BuildRequires:	libjpeg-devel
BuildRequires:	xpm-devel
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
GD.pm is a autoloadable interface module for libgd, a popular library
for creating and manipulating PNG files.  With this library you can
create PNG images on the fly or modify existing files.  Features
include:

a.  lines, polygons, rectangles and arcs, both filled and unfilled
b.  flood fills
c.  the use of arbitrary images as brushes and as tiled fill patterns
d.  line styling (dashed lines and the like)
e.  horizontal and vertical text rendering
f.  support for transparency and interlacing


%prep
%setup -q -n %{module}-%{version}

# Remove Local from path
find . -type f | xargs perl -p -i -e "s|/usr/local/|/usr/|g"

# lib64 fixes, don't add /usr/lib/X11 to linker search path
perl -pi -e "s|-L/usr/lib/X11||g;s|-L/usr/X11/lib||g;s|-L/usr/lib||g" Makefile.PL
perl -pi -e "s|(/usr/X11R6)/lib|\1/%{_lib}|g" Makefile.PL

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%{optflags}"

%check
%ifnarch ppc
%{__make} test
%endif

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog README README.QUICKDRAW README.unix demos
%{perl_vendorarch}/GD*
%{perl_vendorarch}/auto/GD*
%{perl_vendorarch}/qd.pl
%{_mandir}/man?/*
%{_bindir}/bdf2gdfont.pl

