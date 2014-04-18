%define		pkgname	xlsxwriter
Summary:	A Python module for creating Excel XLSX files
Name:		python-%{pkgname}
Version:	0.5.3
Release:	1
License:	BSD
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/X/XlsxWriter/XlsxWriter-%{version}.tar.gz
# Source0-md5:	490074368f784c4a06295a5dca2c0d7d
URL:		https://github.com/jmcnamara/XlsxWriter
BuildRequires:	python-devel
Requires:	python-libs >= 1:2.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XlsxWriter is a Python module for writing files in the Excel 2007+
XLSX file format.

XlsxWriter can be used to write text, numbers, formulas and hyperlinks
to multiple worksheets and it supports features such as formatting and
many more, including:
- 100% compatible Excel XLSX files.
- Full formatting.
- Merged cells.
- Defined names.
- Charts.
- Autofilters.
- Data validation and drop down lists.
- Conditional formatting.
- Worksheet PNG/JPEG images.
- Rich multi-format strings.
- Cell comments.
- Memory optimisation mode for writing large files.

%prep
%setup -q -n XlsxWriter-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/readme.html README.rst LICENSE.txt
%dir %{py_sitescriptdir}/%{pkgname}
%{py_sitescriptdir}/%{pkgname}/*.py[co]
%{py_sitescriptdir}/XlsxWriter-%{version}-py*.egg-info
