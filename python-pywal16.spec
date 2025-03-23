Name:		python-pywal16
Version:	3.8.3
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/p/pywal16/pywal16-%{version}.tar.gz
Summary:	Generate and change color-schemes on the fly
URL:		https://pypi.org/project/pywal16/
License:	MIT
Group:		Terminal
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

Provides: wal
Provides: pywal

%description
Generate and change color-schemes on the fly

%prep
%autosetup -p1 -n pywal16-%{version}

%files
%{_bindir}/wal
%{py_sitedir}/*
/usr/man/*
