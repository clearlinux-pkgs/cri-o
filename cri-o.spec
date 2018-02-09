#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cri-o
Version  : 1.0.0
Release  : 10
URL      : https://github.com/kubernetes-incubator/cri-o/archive/v1.0.0.tar.gz
Source0  : https://github.com/kubernetes-incubator/cri-o/archive/v1.0.0.tar.gz
Summary  : Kubelet Container Runtime Interface (CRI) for OCI runtimes.
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSD-3-Clause CC-BY-SA-4.0 ISC LGPL-3.0 MIT MPL-2.0-no-copyleft-exception WTFPL
Requires: cri-o-bin
Requires: cri-o-config
Requires: cri-o-data
Requires: cri-o-doc
BuildRequires : go
BuildRequires : golang-github-cpuguy83-go-md2man
BuildRequires : gpgme-dev
BuildRequires : libassuan-dev
BuildRequires : libgpg-error-dev
BuildRequires : pkgconfig(devmapper)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(libseccomp)
BuildRequires : pkgconfig(ostree-1)
Patch1: 0001-Specify-the-cri-o-symlink-filename.patch
Patch2: 0002-Fix-path-of-crio.service-s-ExecStart-crio-binary.patch
Patch3: 0003-Update-default-crio.conf-file-for-Clear-Linux.patch

%description
The crio package provides an implementation of the
Kubelet Container Runtime Interface (CRI) using OCI conformant runtimes.

crio provides following functionalities:

    Support multiple image formats including the existing Docker image format
    Support for multiple means to download images including trust & image verification
    Container image management (managing image layers, overlay filesystems, etc)
    Container process lifecycle management
    Monitoring and logging required to satisfy the CRI
    Resource isolation as required by the CRI

%package bin
Summary: bin components for the cri-o package.
Group: Binaries
Requires: cri-o-data
Requires: cri-o-config

%description bin
bin components for the cri-o package.


%package config
Summary: config components for the cri-o package.
Group: Default

%description config
config components for the cri-o package.


%package data
Summary: data components for the cri-o package.
Group: Data

%description data
data components for the cri-o package.


%package doc
Summary: doc components for the cri-o package.
Group: Documentation

%description doc
doc components for the cri-o package.


%prep
%setup -q -n cri-o-1.0.0
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1518193154
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1518193154
rm -rf %{buildroot}
%make_install PREFIX=%{buildroot}/usr
## make_install_append content
make install.completions PREFIX=%{buildroot}/usr
make install.systemd PREFIX=%{buildroot}/usr
install -D -m 644 crio.conf %{buildroot}/usr/share/cri-o/crio.conf
install -D -m 644 seccomp.json %{buildroot}/usr/share/cri-o/seccomp.json
install -D -m 644 crio-umount.conf %{buildroot}/usr/share/cri-o/crio-umount.conf
## make_install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/crio
/usr/bin/crioctl
/usr/bin/kpod
/usr/libexec/crio/conmon
/usr/libexec/crio/pause

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/system/cri-o.service
/usr/lib/systemd/system/crio-shutdown.service
/usr/lib/systemd/system/crio.service

%files data
%defattr(-,root,root,-)
/usr/share/bash-completion/completions/kpod
/usr/share/cri-o/crio-umount.conf
/usr/share/cri-o/crio.conf
/usr/share/cri-o/seccomp.json

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
%doc /usr/share/man/man5/*
%doc /usr/share/man/man8/*
