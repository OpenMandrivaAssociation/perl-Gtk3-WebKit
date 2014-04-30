%define	modname	Gtk3-WebKit
%define	modver	0.05

%define perl_glib_require 1.240
%define gtk_require 2.22.1

Name:		perl-%{modname}
Version:	%{perl_convert_version %{modver}}
Release:	1

Summary:	Perl module for the webkit-3.x library
License:	LGPLv2+ or Artistic
Group:		Development/GNOME and GTK+
Url:		http://gtk2-perl.sf.net/
Source0:	http://prdownloads.sourceforge.net/gtk2-perl/%{modname}-%{modver}.tar.gz

BuildArch:	noarch

BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Glib::Object::Introspection)
BuildRequires:	perl(Gtk3)
BuildRequires:	perl(Test::NeedsDisplay)
BuildRequires:	perl-devel
BuildRequires:	perl-ExtUtils-Depends >= 0.300
BuildRequires:	perl-ExtUtils-PkgConfig >= 1.03
BuildRequires:	perl-Glib-Object-Introspection >= 0.002
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

%files
%doc COPYING Changes META.json META.yml MYMETA.yml README examples
%{perl_vendorlib}/Gtk3/WebKit*
%{_mandir}/*/*
