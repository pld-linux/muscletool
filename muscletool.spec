#
# Conditional build:
%bcond_with	musclev2	# for MuscleCard v2
#
%if %{with musclev2}
%define	muscle_ver	2.0
%else
%define	muscle_ver	1.3.0
%endif
Summary:	muscleTool - command line tool for MuscleCard enabled smartcards
Summary(pl.UTF-8):	muscleTool - narzędzie linii poleceń do kart procesorowych MuscleCard
Name:		muscletool
Version:	2.1.1
Release:	1
License:	BSD
Group:		Applications
#Source0Download: https://alioth.debian.org/project/showfiles.php?group_id=30112
Source0:	https://alioth.debian.org/frs/download.php/3180/%{name}-%{version}.tar.bz2
# Source0-md5:	262040198294075274418688c73c2538
URL:		http://muscleapps.alioth.debian.org/
BuildRequires:	libmusclecard-devel >= %{muscle_ver}
BuildRequires:	pkgconfig
BuildRequires:	readline-devel
Requires:	libmusclecard >= %{muscle_ver}
Obsoletes:	muscleframework-tools < 1.1.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
muscleTool is a command line tool for MuscleCard enabled smartcards.
The main function is to format a smart card, but it offers some
additional MuscleCard functionality. There are key, PIN, object and
general related functions.

%description -l pl.UTF-8
muscleTool to działające z linii poleceń narzędzie do kart
procesorowych z oprogramowaniem MuscleCard. Główną funkcją jest
formatowanie kart procesorowych, ale dostępne są też inne funkcje
związane z oprogramowaniem MuscleCard, związane m.in. z kluczami,
PIN-ami, obiektami.

%prep
%setup -q

%build
%configure \
	--enable-readline \
	%{?with_musclev2:--enable-version2}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/muscleTool
%{_mandir}/man1/muscleTool.1*
