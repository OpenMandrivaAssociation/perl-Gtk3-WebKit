%define	modname	Gtk3-WebKit
%define	modver	0.06

%define perl_glib_require 1.240
%define gtk_require 2.22.1

Name:		perl-%{modname}
Version:	%{perl_convert_version %{modver}}
Release:	3

Summary:	Perl module for the webkit-3.x library
License:	LGPLv2+ or Artistic
Group:		Development/GNOME and GTK+
Url:		http://search.cpan.org/dist/Gtk3-WebKit/
Source0:	http://www.cpan.org/authors/id/P/PO/POTYL/%{modname}-%{modver}.tar.gz

BuildArch:	noarch

BuildRequires:	perl(ExtUtils::Depends) >= 0.300
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(ExtUtils::PkgConfig) >= 1.03
BuildRequires:	perl(Glib::Object::Introspection)
BuildRequires:	perl(Gtk3)
BuildRequires:	perl(Test::NeedsDisplay)
BuildRequires:	perl-devel
BuildRequires:	typelib(WebKit) = 3.0
Requires:	typelib(WebKit) = 3.0

%description
This module provides the Perl bindings for the Gtk port of WebKit.

WebKit is a web content engine, derived from KHTML and KJS from KDE, and used
primarily in Apple's Safari browser and Google's Chrome browser. It is made to
be embedded in other applications, such as mail readers, or web browsers.

It is able to display content such as HTML, SVG, XML, and others. It also
supports DOM, XMLHttpRequest, XSLT, CSS, Javascript/ECMAscript and more.

%prep
%setup -q -n %{modname}-%{modver}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="%{optflags}"

%install
%makeinstall_std

%check
%make test

%files
%doc COPYING Changes MYMETA.json META.yml MYMETA.yml README examples
%{perl_vendorlib}/Gtk3/WebKit*
%{_mandir}/*/*
