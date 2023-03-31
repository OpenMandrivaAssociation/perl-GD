%define modname	GD
%define modver 2.76

Summary:	A perl5 interface to Thomas Boutell's gd library

Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	2
License:	Artistic
Group:		Development/Perl
Url:		http://metacpan.org/pod/GD
Source0:	http://www.cpan.org/modules/by-module/%{modname}/%{modname}-%{modver}.tar.gz
Patch0:		GD-2.56-utf8.patch
Patch1:		https://src.fedoraproject.org/rpms/perl-GD/raw/master/f/GD-2.70-cflags.patch
BuildRequires:	pkgconfig(gdlib)
BuildRequires:	pkgconfig(libjpeg)
BuildRequires:	perl-devel
BuildRequires:	perl-JSON-PP
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(xpm)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(libtiff-4)
BuildRequires:	pkgconfig(libwebp)
BuildRequires:	perl(ExtUtils::PkgConfig)

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
%autosetup -p0 -n %{modname}-%{modver}

# Remove Local from path
find . -type f | xargs perl -p -i -e "s|/usr/local/|/usr/|g"

# lib64 fixes, don't add /usr/lib/X11 to linker search path
sed -i  -e "s|-L/usr/lib/X11||g;s|-L/usr/X11/lib||g;s|-L/usr/X11R6/lib||g;s|-L/usr/lib|-L%{_libdir}|g" Makefile.PL

%build
echo %{_libdir} |perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%make_build

#%check
#%ifnarch ppc
#%{__make} test
#%endif

%install
%make_install

%files
%doc ChangeLog README README.QUICKDRAW demos
%{perl_vendorarch}/GD*
%{perl_vendorarch}/auto/GD*
%{_bindir}/bdf2gdfont.pl
%{_mandir}/man1/*
%{_mandir}/man3/*
