#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Math
%define	pnam	SchemaView-Plus
Summary:	SchemaView-Plus - drawing database schemas
Summary(pl):	SchemaView-Plus - rysowanie schematów baz danych
Name:		perl-SchemaView-Plus
Version:	0.16
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
# Source0-md5:	12bf54544099f03fb0ab3285732c5c45
BuildRequires:	perl-DBI >= 1.12
BuildRequires:	perl-Tk >= 800.014
BuildRequires:	perl(Tk::ProgressBar)
BuildRequires:	perl-Tk-FontDialog
BuildRequires:	perl-Tk-MListbox
BuildRequires:	perl-XML-Dumper >= 0.4
BuildRequires:	perl-XML-Parser
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-DBI >= 1.12
Requires:	perl-Tk >= 800.014
Requires:	perl-XML-Dumper >= 0.4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SchemaView Plus is a GUI for retrieve, drawing and printing database
schema. Schema can be retrieved using DBIx::SystemCatalog (currently
supported basically all current DBD drivers, some better support for
PostgreSQL and quite well support for Oracle). Program uses XML for
storing and retrieving data in text files. You can write any filters
to modify these XML files for add new functionality based on your
projects (e.g. dropping off some relationships etc.). You can specify
one filename on command line for autoloading it after GUI start up.
Schema can be printed to PostScript file.

%description -l pl
SchemaView Plus to GUI do odtwarzania, rysowania i drukowania
schematów baz danych. Schematy mog± byæ pozyskiwane przy u¿yciu
DBIx::SystemCatalog (aktualnie z podstawow± obs³ug± wszystkich
sterowników DBD, lepsz± obs³ug± dla PostgreSQL-a i nieco lepsz± dla
Oracle'a). Program u¿ywa XML-a do zapisywania i odczytywania danych
z plików tekstowych. Mo¿na pisaæ dowolne filtry do modyfikowania
tych plików XML do dodawania nowej funkcjonalno¶ci opartej na w³asnych
projektach (np. porzucanie czê¶ci relacji). Mo¿na podaæ jeden plik z
linii poleceñ w celu automatycznego wczytania go po starcie GUI.
Schemat mo¿na wydrukowaæ do pliku PostScript.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README eg/example.svp
%attr(755,root,root) %{_bindir}/svplus
%{perl_vendorlib}/DBIx/SystemCatalog*
%{perl_vendorlib}/Data/*.pm
%{perl_vendorlib}/Hints
%{perl_vendorlib}/Logo
%{perl_vendorlib}/Math/Project.pm
%{perl_vendorlib}/PostScript/Poster.pm
%{perl_vendorlib}/Print
%{perl_vendorlib}/Hints.pm
%{_mandir}/man[13]/*
