%define	_lang	pl
%define	_reg	PL
%define _lare	%{_lang}-%{_reg}
Summary:	Polish resources for SeaMonkey
Summary(pl.UTF-8):	Polskie pliki językowe dla SeaMonkeya
Name:		seamonkey-lang-%{_lang}
Version:	1.1.7
Release:	1
License:	MPL 1.1 or GPL v2+ or LGPL v2.1+
Group:		X11/Applications/Networking
Source0:	http://releases.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/contrib-localized/seamonkey-%{version}.%{_lare}.langpack.xpi
# Source0-md5:	5dedd67377d38d5514c459203a8ccb05
Source1:	http://www.mozilla-enigmail.org/downloads/lang/0.9x/enigmail-%{_lare}-0.9x.xpi
# Source1-md5:	3ac349c7b6a1ebbd80f11c8911f5102d
Source2:	gen-installed-chrome.sh
URL:		http://www.mozilla.org/projects/seamonkey/
BuildRequires:	unzip
BuildRequires:	util-linux
Requires(post,postun):	seamonkey >= %{version}
Requires(post,postun):	textutils
Requires:	seamonkey >= %{version}
Obsoletes:	mozilla-lang-pl
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_chromedir	%{_datadir}/seamonkey/chrome

%description
Polish resources for SeaMonkey.

%description -l pl.UTF-8
Polskie pliki językowe dla SeaMonkeya.

%prep
%setup -q -c
%{__unzip} -o -qq %{SOURCE1}
install %{SOURCE2} .
./gen-installed-chrome.sh locale bin/chrome/{%{_reg},%{_lare},%{_lang}-unix}.jar \
	> lang-%{_lang}-installed-chrome.txt
./gen-installed-chrome.sh locale chrome/enigmail-%{_lare}.jar \
	>> lang-%{_lang}-installed-chrome.txt

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

install bin/chrome/{%{_reg},%{_lare},%{_lang}-unix}.jar $RPM_BUILD_ROOT%{_chromedir}
install chrome/enigmail-%{_lare}.jar $RPM_BUILD_ROOT%{_chromedir}
install lang-%{_lang}-installed-chrome.txt $RPM_BUILD_ROOT%{_chromedir}
cp -r bin/{searchplugins,defaults,dictionaries} $RPM_BUILD_ROOT%{_datadir}/seamonkey
rm $RPM_BUILD_ROOT%{_datadir}/seamonkey/searchplugins/google.*

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/seamonkey-chrome+xpcom-generate

%postun
%{_sbindir}/seamonkey-chrome+xpcom-generate

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_reg}.jar
%{_chromedir}/%{_lare}.jar
%{_chromedir}/%{_lang}-unix.jar
%{_chromedir}/enigmail-%{_lare}.jar
%{_chromedir}/lang-%{_lang}-installed-chrome.txt
%{_datadir}/seamonkey/searchplugins/*
# dir not provided
#%{_datadir}/seamonkey/defaults/isp/%{_reg}
%{_datadir}/seamonkey/defaults/messenger/%{_reg}
%{_datadir}/seamonkey/defaults/profile/%{_reg}
%{_datadir}/seamonkey/dictionaries/*
