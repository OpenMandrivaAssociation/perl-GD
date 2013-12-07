%define modname	GD
%define modver	2.49

Summary:	A perl5 interface to Thomas Boutell's gd library
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	2
License:	Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/GD/%{modname}-%{modver}.tar.gz
Patch2:		skip-jpg-test.diff
BuildRequires:	gd-devel
BuildRequires:	jpeg-devel
BuildRequires:	perl-devel
BuildRequires:	perl-JSON-PP
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(xpm)
BuildRequires:	pkgconfig(zlib)

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
%setup -qn %{modname}-%{modver}
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
%__perl Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%{optflags}"

#%check
#%ifnarch ppc
#%{__make} test
#%endif

%install
%makeinstall_std

%files
%doc ChangeLog README README.QUICKDRAW README.unix demos
%{perl_vendorarch}/GD*
%{perl_vendorarch}/auto/GD*
%{perl_vendorarch}/qd.pl
%{_bindir}/bdf2gdfont.pl
%{_mandir}/man1/*
%{_mandir}/man3/*

