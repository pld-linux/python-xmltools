%define short_name xmltools
%define python_sitepkgsdir %(echo `python -c "import sys; print (sys.prefix + '/lib/python' + sys.version[:3] + '/site-packages/')"`)

Summary:	Python XMLTools
Summary(pl):	Narzêdzia XML dla Pythona
Name:		python-%{short_name}
Version:	1.3.7
Release:	1
License:	Unknown
Group:		Development/Libraries
Source0:	ftp://ftp.logilab.org/pub/xmltools/%{short_name}-%{version}.tar.gz
# Source0-md5:	5764ccfb11e111fe8df62ba68fa8df8a
URL:		http://www.logilab.org/xmltools/index.html
BuildRequires:	python >= 2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	python-PyXML
Requires:	python-4Suite

%description
Python XmlTools is a set of high level tools to help using XML in
python. It relies heavily on PyXml and 4Suite to access XML resources.

%description -l pl
Python XmlTools to zestaw wysokopoziomowych narzêdzi pomagaj±cych przy
u¿ywaniu XML w Pythonie. Polegaj± na PyXml i 4Suite do dostêpu do
zasobów XML.

%prep
%setup -q -n %{short_name}-%{version}

%build
CFLAGS="%{rpmcflags}" python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc PKG-INFO
%{python_sitepkgsdir}/logilab
