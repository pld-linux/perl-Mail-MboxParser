
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%include	/usr/lib/rpm/macros.perl
%define	pdir	Mail
%define	pnam	MboxParser
Summary:	Mail::MboxParser - read-only access to UNIX-mailboxes
Summary(pl):	Mail::MboxParser - dostêp w trybie odczytu do uniksowych skrzynek pocztowych
Name:		perl-Mail-MboxParser
Version:	0.44
Release:	1
# same as perl
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1eefc380bd0d3c2cfefa6ebcfcf4d0b6
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(MIME::QuotedPrint)
BuildRequires:	perl-MIME-tools >= 5.0
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module attempts to provide a simplified access to standard
UNIX-mailboxes. It offers only a subset of methods to get 'straight to
the point'. More sophisticated things can still be done by invoking
any method from MIME::Tools on the appropriate return values.

%description -l pl
Ten modu³ próbuje daæ uproszczony dostêp do standardowych uniksowych
skrzynek pocztowych. Oferuje tylko podzbiór metod. Bardziej wymy¶le
rzeczy nadal mo¿na robiæ wywo³uj±c dowoln± metodê z MIME::Tools na
w³a¶ciwych warto¶ciach zwróconych przez ten modu³.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}
cp -r eg $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog README
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}
%{perl_vendorlib}/%{pdir}/*.pm
%{perl_vendorlib}/%{pdir}/%{pnam}
%{_mandir}/man3/*
