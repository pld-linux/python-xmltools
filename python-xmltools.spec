%define short_name xmltools
%define python_sitepkgsdir %(echo `python -c "import sys; print (sys.prefix + '/lib/python' + sys.version[:3] + '/site-packages/')"`)

Summary:	Python XMLTools
Name:		python-%{short_name}
Version:	1.3.5
Release:	1
Source0:	ftp://ftp.logilab.org/pub/xmltools/%{short_name}-%{version}.tar.gz
License:	Unknown
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Разработка/Библиотеки
Group(uk):	Розробка/Б╕бл╕отеки
BuildRequires:	python >= 2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	python-PyXML
Requires:	python-4Suite
Url:		http://www.logilab.org/xmltools/index.html

%description
Python XmlTools is a set of high level tools to help using XML in
python. It relies heavily on PyXml and 4Suite to access XML resources.

%prep
%setup -q -n %{short_name}-%{version}

%build
CFLAGS="%{rpmcflags}" python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

gzip -9fn PKG-INFO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{python_sitepkgsdir}/logilab
