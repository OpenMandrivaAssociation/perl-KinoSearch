%define upstream_name    KinoSearch
%define upstream_version 0.165

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Surround highlight bits with tags
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module//%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Compress::Zlib)
BuildRequires: perl(ExtUtils::CBuilder)
BuildRequires: perl(ExtUtils::ParseXS)
BuildRequires: perl(Lingua::Stem::Snowball)
BuildRequires: perl(Lingua::StopWords)
BuildRequires: perl(Module::Build::Compat)
BuildRequires: perl-devel

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
KinoSearch is a loose port of the Java search engine library Apache Lucene,
written in Perl and C. The archetypal application is website search, but it
can be put to many different uses.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/man3/*
%perl_vendorlib/*
/usr/lib/debug/usr/lib/perl5/vendor_perl/5.10.1/x86_64-linux-thread-multi/auto/KinoSearch/KinoSearch.so.debug
/usr/src/debug/*