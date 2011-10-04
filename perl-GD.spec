%define upstream_name    GD
%define upstream_version 2.46

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 2

Summary:	A perl5 interface to Thomas Boutell's gd library
License:	Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/GD/%{upstream_name}-%{upstream_version}.tar.gz
Patch2:		skip-jpg-test.diff
BuildRequires:	gd-devel
BuildRequires:	libpng-devel
BuildRequires:	zlib-devel
BuildRequires:	freetype-devel
BuildRequires:	libjpeg-devel
BuildRequires:	xpm-devel
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

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
%setup -q -n %{upstream_name}-%{upstream_version}
%patch2 -p0

# Remove Local from path
find . -type f | xargs perl -p -i -e "s|/usr/local/|/usr/|g"

# lib64 fixes, don't add /usr/lib/X11 to linker search path
perl -pi \
    -e "s|-L/usr/lib/X11||g;" \
    -e "s|-L/usr/X11/lib||g;" \
    -e "s|-L/usr/lib||g" \
    Makefile.PL

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

