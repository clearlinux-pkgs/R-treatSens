#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-treatSens
Version  : 2.1.3
Release  : 2
URL      : https://cran.r-project.org/src/contrib/treatSens_2.1.3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/treatSens_2.1.3.tar.gz
Summary  : Sensitivity Analysis for Causal Inference
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-treatSens-lib
Requires: R-BH
Requires: R-Rcpp
Requires: R-RcppEigen
Requires: R-dbarts
Requires: R-lme4
Requires: R-mvtnorm
BuildRequires : R-BH
BuildRequires : R-Rcpp
BuildRequires : R-RcppEigen
BuildRequires : R-dbarts
BuildRequires : R-lme4
BuildRequires : R-mvtnorm
BuildRequires : clr-R-helpers

%description
parametric models with either binary or continuous treatment.

%package lib
Summary: lib components for the R-treatSens package.
Group: Libraries

%description lib
lib components for the R-treatSens package.


%prep
%setup -q -c -n treatSens

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1521208137

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1521208137
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library treatSens
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library treatSens
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library treatSens
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library treatSens|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/treatSens/CITATION
/usr/lib64/R/library/treatSens/DESCRIPTION
/usr/lib64/R/library/treatSens/INDEX
/usr/lib64/R/library/treatSens/Meta/Rd.rds
/usr/lib64/R/library/treatSens/Meta/features.rds
/usr/lib64/R/library/treatSens/Meta/hsearch.rds
/usr/lib64/R/library/treatSens/Meta/links.rds
/usr/lib64/R/library/treatSens/Meta/nsInfo.rds
/usr/lib64/R/library/treatSens/Meta/package.rds
/usr/lib64/R/library/treatSens/NAMESPACE
/usr/lib64/R/library/treatSens/R/treatSens
/usr/lib64/R/library/treatSens/R/treatSens.rdb
/usr/lib64/R/library/treatSens/R/treatSens.rdx
/usr/lib64/R/library/treatSens/help/AnIndex
/usr/lib64/R/library/treatSens/help/aliases.rds
/usr/lib64/R/library/treatSens/help/paths.rds
/usr/lib64/R/library/treatSens/help/treatSens.rdb
/usr/lib64/R/library/treatSens/help/treatSens.rdx
/usr/lib64/R/library/treatSens/html/00Index.html
/usr/lib64/R/library/treatSens/html/R.css
/usr/lib64/R/library/treatSens/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/treatSens/libs/treatSens.so
/usr/lib64/R/library/treatSens/libs/treatSens.so.avx2
/usr/lib64/R/library/treatSens/libs/treatSens.so.avx512
