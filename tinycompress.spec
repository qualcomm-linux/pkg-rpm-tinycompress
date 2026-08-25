%global debug_package %{nil}

Name:           tinycompress
Version:        1.2.16
Release:        1%{?dist}
Summary:        Tiny ALSA compress library for compressed audio offload
License:        BSD-3-Clause AND LGPL-2.1-only
URL:            https://github.com/alsa-project/tinycompress
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

ExclusiveArch:  aarch64

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0)

%description
tinycompress is a user-space library for the ALSA compressed audio
interface. It enables offloaded audio decoding using the kernel
compress interface (e.g., MP3, AAC offload on Qualcomm platforms).

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers and pkg-config files for building applications that use
the tinycompress library.

%prep
%autosetup -n %{name}-%{version}

%build
autoreconf -fi
%configure --with-glib

%make_build

%install
%make_install
find %{buildroot} -name '*.la' -delete

%files
%license COPYING
%{_libdir}/libtinycompress.so*
%{_bindir}/cplay
%{_bindir}/crecord
%{_bindir}/sofprobeclient

%files devel
%{_includedir}/tinycompress/
%{_libdir}/pkgconfig/tinycompress.pc

%changelog
* Fri Aug 14 2026 Qualcomm Linux <quic_linux@quicinc.com> - 1.2.16-1
- Initial RPM packaging of tinycompress version 1.2.16
