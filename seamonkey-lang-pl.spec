Summary:	Polish resources for SeaMonkey
Summary(pl):	Polskie pliki jêzykowe dla SeaMonkeya
Name:		seamonkey-lang-pl
Version:	1.0.3
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/contrib-localized/seamonkey-%{version}.pl-PL.langpack.xpi
# Source0-md5:	41a828a165b8cd5c20e1fdadf6258246
Source1:	http://www.mozilla-enigmail.org/downloads/lang/0.9x/enigmail-pl-PL-0.9x.xpi
# Source1-md5:	5061fb4a0b321644a1716aea831cf281
Source2:	gen-installed-chrome.sh
URL:		http://www.mozilla.org/projects/seamonkey/
BuildRequires:	unzip
BuildRequires:	util-linux
Requires(post,postun):	seamonkey >= %{version}
Requires(post,postun):	textutils
Requires:	seamonkey >= %{version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_chromedir	%{_datadir}/seamonkey/chrome

%description
Polish resources for SeaMonkey.

%description -l pl
Polskie pliki jêzykowe dla SeaMonkeya.

%prep
%setup -q -c
unzip -o %{SOURCE1}
install %{SOURCE2} .
./gen-installed-chrome.sh locale bin/chrome/{PL,pl-PL,pl-unix}.jar \
	> lang-pl-installed-chrome.txt
./gen-installed-chrome.sh locale chrome/enigmail-pl-PL.jar \
	>> lang-pl-installed-chrome.txt

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

install bin/chrome/{PL,pl-PL,pl-unix}.jar $RPM_BUILD_ROOT%{_chromedir}
install chrome/enigmail-pl-PL.jar $RPM_BUILD_ROOT%{_chromedir}
install lang-pl-installed-chrome.txt $RPM_BUILD_ROOT%{_chromedir}
cp -r bin/{searchplugins,defaults,components/myspell} $RPM_BUILD_ROOT%{_datadir}/seamonkey
rm $RPM_BUILD_ROOT%{_datadir}/seamonkey/searchplugins/google.*
rename PL pl-PL $RPM_BUILD_ROOT%{_datadir}/seamonkey/myspell/PL.{aff,dic}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/seamonkey-chrome+xpcom-generate

%postun
%{_sbindir}/seamonkey-chrome+xpcom-generate

%files
%defattr(644,root,root,755)
%{_chromedir}/PL.jar
%{_chromedir}/pl-PL.jar
%{_chromedir}/pl-unix.jar
%{_chromedir}/enigmail-pl-PL.jar
%{_chromedir}/lang-pl-installed-chrome.txt
%{_datadir}/seamonkey/searchplugins/*
%{_datadir}/seamonkey/defaults/messenger/PL
%{_datadir}/seamonkey/defaults/profile/PL
%{_datadir}/seamonkey/myspell/*
