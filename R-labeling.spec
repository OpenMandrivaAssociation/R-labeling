%global packname labeling
%global rlibdir %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.2
Release:          1
Summary:          Axis Labeling
Group:            Sciences/Mathematics
License:          MIT
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.2.tar.gz
BuildArch:        noarch
Requires:         R-core
BuildRequires:    R-devel Rmath-devel texlive-collection-latex

%description
Provides a range of axis labeling algorithms

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
