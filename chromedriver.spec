Summary:	WebDriver for Google Chrome
Summary(pl.UTF-8):	Interfejs WebDriver do przeglądarki Google Chrome
Name:		chromedriver
Version:	2.37
Release:	1
License:	Distributable
Group:		Applications
Source0:	https://chromedriver.storage.googleapis.com/%{version}/%{name}_linux64.zip
# Source0-md5:	f4fbbf50eaec2b9c9e21536e39b9999e
URL:		https://sites.google.com/a/chromium.org/chromedriver/
ExclusiveArch:	%{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WebDriver is an open source tool for automated testing of webapps
across many browsers. It provides capabilities for navigating to web
pages, user input, JavaScript execution, and more.

%description -l pl.UTF-8
WebDriver to otwarte narzędzie do automatycznego testowania aplikacji
WWW w różnych przeglądarkach. Ma możliwość nawigowania po stronach
WWW, wprowadzania danych użytkownika, wykonywania JavaScriptu itd.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

cp -p chromedriver $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/chromedriver
