%define	short_name		xmltools

Summary:	Python XMLTools
Summary(pl.UTF-8):	Narzędzia XML dla Pythona
Name:		python-%{short_name}
Version:	1.4.0
Release:	2
License:	unknown
Group:		Development/Libraries
Source0:	ftp://ftp.logilab.org/pub/xmltools/%{short_name}-%{version}.tar.gz
# Source0-md5:	1ddfaf02cb2c20a199d57700a03b2154
URL:		http://www.logilab.org/xmltools/index.html
BuildRequires:	python >= 2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	python-PyXML
Requires:	python-4Suite

%description
Python XmlTools is a set of high level tools to help using XML in
python. It relies heavily on PyXml and 4Suite to access XML resources.

%description -l pl.UTF-8
Python XmlTools to zestaw wysokopoziomowych narzędzi pomagających przy
używaniu XML w Pythonie. Polegają na PyXml i 4Suite do dostępu do
zasobów XML.

%prep
%setup -q -n %{short_name}-%{version}

%build
CFLAGS="%{rpmcflags}" python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc PKG-INFO
%{py_sitescriptdir}/logilab
