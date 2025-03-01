%global forname kwin-effects-forceblur

Name:           kwin-effects-forceblur
Version:        0.1
Release:        1%{?dist}
Summary:        Force blur effect for KDE Plasma KWin

License:        GPLv3+
URL:            https://github.com/taj-ny/kwin-effects-forceblur
Source0:        %{url}/archive/refs/heads/main.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-kwindowsystem-devel
BuildRequires:  plasma-workspace-devel
BuildRequires:  libplasma-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  kwin-devel
BuildRequires:  kf6-knotifications-devel
BuildRequires:  kf6-kio-devel
BuildRequires:  kf6-kcrash-devel
BuildRequires:  kf6-ki18n-devel
BuildRequires:  kf6-kguiaddons-devel
BuildRequires:  libepoxy-devel
BuildRequires:  kf6-kglobalaccel-devel
BuildRequires:  kf6-kcmutils-devel
BuildRequires:  kf6-kconfigwidgets-devel
BuildRequires:  kf6-kdeclarative-devel
BuildRequires:  kdecoration-devel
BuildRequires:  wayland-devel

Requires:       kf6-kglobalaccel
Requires:       kf6-kdeclarative
Requires:       libplasma
Requires:       kf6-kio
Requires:       qt6-qtbase
Requires:       kf6-kguiaddons
Requires:       kf6-ki18n

%description
A KWin effect that allows you to force blur on windows that don't support 
it natively. This plugin adds a KWin window rule that can be configured to 
apply blur to specific windows or window classes.

%prep
%setup -q -n %{name}-main

%build
%cmake -DCMAKE_INSTALL_PREFIX=/usr
%cmake_build

%install
%cmake_install
# List installed files for debugging
find %{buildroot} -type f -o -type l | sort

%files
# Use wildcard paths to be more flexible
%dir %{_libdir}/qt6/plugins/kwin/effects/
%{_libdir}/qt6/plugins/kwin/effects/*.so
%dir %{_datadir}/kwin/
%{_datadir}/kwin/*
# Configuration files
%{_datadir}/config.kcfg/*
# License
%license LICENSE
# Documentation
%doc README.md
