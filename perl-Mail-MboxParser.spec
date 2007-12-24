
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%include	/usr/lib/rpm/macros.perl
%define		pdir	Mail
%define		pnam	MboxParser
Summary:	Mail::MboxParser - read-only access to UNIX-mailboxes
Summary(pl.UTF-8):	Mail::MboxParser - dostęp w trybie odczytu do uniksowych skrzynek pocztowych
Name:		perl-Mail-MboxParser
Version:	0.55
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1b9fdb367db36ec94e7b5c6721f11221
BuildRequires:	perl-devel >= 1:5.8.0
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

%description -l pl.UTF-8
Ten moduł próbuje dać uproszczony dostęp do standardowych uniksowych
skrzynek pocztowych. Oferuje tylko podzbiór metod. Bardziej wymyśle
rzeczy nadal można robić wywołując dowolną metodę z MIME::Tools na
właściwych wartościach zwróconych przez ten moduł.

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
%{perl_vendorlib}/Mail/*.pm
%{perl_vendorlib}/Mail/MboxParser
%{_mandir}/man3/*
