%define upstream_name KinoSearch
%define upstream_version 0.165

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Surround highlight bits with tags
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module//%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(Compress::Zlib)
BuildRequires:	perl(ExtUtils::CBuilder)
BuildRequires:	perl(ExtUtils::ParseXS)
BuildRequires:	perl(Lingua::Stem::Snowball)
BuildRequires:	perl(Lingua::StopWords)
BuildRequires:	perl(Module::Build::Compat)
BuildRequires:	perl-devel

%description
KinoSearch is a loose port of the Java search engine library Apache Lucene,
written in Perl and C. The archetypal application is website search, but it
can be put to many different uses.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sun Feb 12 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.165.0-5
+ Revision: 773604
- cleanout spec
- svn commit -m mass rebuild of perl extension against perl 5.14.2

  + Jérôme Quelin <jquelin@mandriva.org>
    - rebuild for perl 5.12
    - rebuild

* Fri Mar 12 2010 Jérôme Quelin <jquelin@mandriva.org> 0.165.0-2mdv2010.1
+ Revision: 518458
- ship debug files in -debug

* Mon Nov 30 2009 Jérôme Quelin <jquelin@mandriva.org> 0.165.0-1mdv2010.1
+ Revision: 471664
- no arch-dep files should be mentioned in %%files
- module is binary, not noarch
- import perl-KinoSearch


* Sun Nov 29 2009 cpan2dist 0.165-1mdv
- initial mdv release, generated with cpan2dist
