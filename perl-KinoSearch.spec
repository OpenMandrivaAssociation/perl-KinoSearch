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
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
KinoSearch is a loose port of the Java search engine library Apache Lucene,
written in Perl and C. The archetypal application is website search, but it
can be put to many different uses.

Features
    * *

      Extremely fast and scalable - can handle millions of documents

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

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
/usr/src/debug/KinoSearch-0.165/lib/KinoSearch.c
/usr/src/debug/KinoSearch-0.165/lib/KinoSearch.xs
/usr/src/debug/KinoSearch-0.165/lib/KinoSearch/Analysis/Stopalizer.pm
/usr/src/debug/KinoSearch-0.165/lib/KinoSearch/Analysis/Token.pm
/usr/src/debug/KinoSearch-0.165/lib/KinoSearch/Analysis/TokenBatch.pm
/usr/src/debug/KinoSearch-0.165/lib/KinoSearch/Document/Field.pm
/usr/src/debug/KinoSearch-0.165/lib/KinoSearch/Index/DelDocs.pm
/usr/src/debug/KinoSearch-0.165/lib/KinoSearch/Index/MultiTermDocs.pm
/usr/src/debug/KinoSearch-0.165/lib/KinoSearch/Index/PostingsWriter.pm
/usr/src/debug/KinoSearch-0.165/lib/KinoSearch/Index/SegTermDocs.pm
/usr/src/debug/KinoSearch-0.165/lib/KinoSearch/Index/SegTermEnum.pm
/usr/src/debug/KinoSearch-0.165/lib/KinoSearch/Index/SegWriter.pm
/usr/src/debug/KinoSearch-0.165/lib/KinoSearch/Index/TermBuffer.pm
/usr/src/debug/KinoSearch-0.165/lib/KinoSearch/Index/TermDocs.pm
/usr/src/debug/KinoSearch-0.165/lib/KinoSearch/Index/TermInfo.pm
/usr/src/debug/KinoSearch-0.165/lib/KinoSearch/Index/TermInfosWriter.pm
/usr/src/debug/KinoSearch-0.165/lib/KinoSearch/Search/BooleanScorer.pm
/usr/src/debug/KinoSearch-0.165/lib/KinoSearch/Search/HitCollector.pm
/usr/src/debug/KinoSearch-0.165/lib/KinoSearch/Search/HitQueue.pm
/usr/src/debug/KinoSearch-0.165/lib/KinoSearch/Search/PhraseScorer.pm
/usr/src/debug/KinoSearch-0.165/lib/KinoSearch/Search/Scorer.pm
/usr/src/debug/KinoSearch-0.165/lib/KinoSearch/Search/Similarity.pm
/usr/src/debug/KinoSearch-0.165/lib/KinoSearch/Search/TermScorer.pm
/usr/src/debug/KinoSearch-0.165/lib/KinoSearch/Store/InStream.pm
/usr/src/debug/KinoSearch-0.165/lib/KinoSearch/Store/OutStream.pm
/usr/src/debug/KinoSearch-0.165/lib/KinoSearch/Util/BitVector.pm
/usr/src/debug/KinoSearch-0.165/lib/KinoSearch/Util/ByteBuf.pm
/usr/src/debug/KinoSearch-0.165/lib/KinoSearch/Util/Carp.pm
/usr/src/debug/KinoSearch-0.165/lib/KinoSearch/Util/IntMap.pm
/usr/src/debug/KinoSearch-0.165/lib/KinoSearch/Util/MathUtils.pm
/usr/src/debug/KinoSearch-0.165/lib/KinoSearch/Util/MemManager.pm
/usr/src/debug/KinoSearch-0.165/lib/KinoSearch/Util/PriorityQueue.pm
/usr/src/debug/KinoSearch-0.165/lib/KinoSearch/Util/SortExternal.pm
/usr/src/debug/KinoSearch-0.165/lib/KinoSearch/Util/StringHelper.pm
/usr/src/debug/KinoSearch-0.165/lib/KinoSearch/Util/VerifyArgs.pm

