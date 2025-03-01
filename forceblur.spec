Name:           kwin-effects-forceblur
Version:        0.4.1
Release:        1%{?dist}
Summary:        KWin effect to blur the background behind semi-transparent windows

License:        GPL-3.0-or-later
URL:            https://github.com/taj-ny/kwin-effects-forceblur
Source0:        https://github.com/taj-ny/kwin-effects-forceblur/archive/refs/tags/v%{version}.tar.gz

# Build dependencies derived from the provided dnf install command
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

%description
Forceblur is a KWin effect that blurs the background behind semi-transparent windows.

%prep
%autosetup -n kwin-effects-forceblur-%{version}

%build
%cmake -DCMAKE_INSTALL_PREFIX=/usr
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_libdir}/qt6/plugins/kwin/effects/forceblur.so
%{_datadir}/kwin/effects/forceblur/metadata.desktop

%changelog
* Wed Oct 11 2023 Your Name <your@email.com> - 0.4.1-1
- Initial package
