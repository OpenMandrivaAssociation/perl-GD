%define upstream_name    GD
%define upstream_version 2.49

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

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
BuildRequires:	jpeg-devel
BuildRequires:	xpm-devel
BuildRequires:	perl-devel
BuildRequires:	perl-JSON-PP

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
%{_mandir}/man?/*
%{_bindir}/bdf2gdfont.pl



%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 2.460.0-4mdv2012.0
+ Revision: 765279
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 2.460.0-3
+ Revision: 763772
- rebuilt for perl-5.14.x

* Tue Oct 04 2011 Oden Eriksson <oeriksson@mandriva.com> 2.460.0-2
+ Revision: 702770
- rebuilt against libpng-1.5.x

* Tue May 17 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.460.0-1
+ Revision: 675527
- new version
- drop format errors patch

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 2.450.0-4
+ Revision: 667151
- mass rebuild

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 2.450.0-3mdv2011.0
+ Revision: 564439
- rebuild for perl 5.12.1

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 2.450.0-2mdv2011.0
+ Revision: 555866
- rebuild for perl 5.12

* Wed Jul 14 2010 Jérôme Quelin <jquelin@mandriva.org> 2.450.0-1mdv2011.0
+ Revision: 553128
- update to 2.45

* Sun Jan 10 2010 Oden Eriksson <oeriksson@mandriva.com> 2.440.0-4mdv2010.1
+ Revision: 488792
- rebuilt against libjpeg v8

* Mon Sep 07 2009 Thierry Vignaud <tv@mandriva.org> 2.440.0-3mdv2010.0
+ Revision: 432268
- skip jpeg test (seems to failed b/c compressed images differ)

  + Funda Wang <fwang@mandriva.org>
    - rebuild for new libjpeg v7

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuilt against libjpeg v7

* Sun Jul 12 2009 Jérôme Quelin <jquelin@mandriva.org> 2.440.0-1mdv2010.0
+ Revision: 394977
- update to 0.44
- removed patch perl-GD-2.41-fix-install, merged upstream
- using %%perl_convert_version

* Thu Jun 11 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.43-1mdv2010.0
+ Revision: 385237
- update to new version 2.43

* Sat Apr 11 2009 Funda Wang <fwang@mandriva.org> 2.41-2mdv2009.1
+ Revision: 366027
- fix str fmt

* Mon Aug 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.41-2mdv2009.0
+ Revision: 270740
- patch 1: fix missing file installation

* Sun Aug 10 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.41-1mdv2009.0
+ Revision: 270385
- update to new version 2.41

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 2.39-2mdv2009.0
+ Revision: 265365
- rebuild early 2009.0 package (before pixel changes)

* Tue Apr 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.39-1mdv2009.0
+ Revision: 196470
- update to new version 2.39

* Mon Jan 14 2008 Pixel <pixel@mandriva.com> 2.35-2mdv2008.1
+ Revision: 151277
- rebuild for perl-5.10.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Aug 25 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.35-1mdv2007.0
- New version 2.35

* Tue Jun 06 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.34-1mdv2007.0
- New release 2.34
- better source URL

* Thu May 18 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.32-2mdk
- fix buildrequires

* Thu Mar 09 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.32-1mdk
- New release 2.32
- spec cleanup
- correct optimisations
- %%mkrel

* Wed Mar 01 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 2.31-1mdk
- 2.31

* Thu Oct 20 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 2.30-1mdk
- 2.30

* Thu Aug 18 2005 Guillaume Rousse <guillomovitch@mandriva.org> 2.28-1mdk
- new version 
- fix sources url for rpmbuildupdate
- spec cleanup

* Sat Jul 16 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 2.25-1mdk
- 2.25
- Re-install qd.pl

* Thu Apr 28 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 2.23-1mdk
- 2.23
- add demos in doc

* Mon Mar 07 2005 Christiaan Welvaart <cjw@daneel.dyndns.org> 2.21-2mdk
- test 11 fails on ppc, disable tests for this arch

* Thu Feb 10 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 2.21-1mdk
- 2.21
- remove qd.pl, which isn't installed anymore

* Thu Nov 25 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 2.19-1mdk
- 2.19
- add tests

* Mon Nov 15 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 2.18-1mdk
- New version
- New script, bdf2gdfont.pl, to convert X BDF fonts to a format loadable by GD

* Tue Jul 27 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 2.16-1mdk
- 2.16.

* Fri Jul 23 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 2.15-1mdk
- 2.15.
- This release re-introduces GIF support. However it won't be enabled if
  libgd has been built without it.

* Thu Apr 15 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 2.12-1mdk
- 2.12.

* Thu Sep 04 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.07-3mdk
- fix buildrequires for 64bit ports

