#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cri-o
Version  : 1.10.5
Release  : 14
URL      : https://github.com/kubernetes-incubator/cri-o/archive/v1.10.5.tar.gz
Source0  : https://github.com/kubernetes-incubator/cri-o/archive/v1.10.5.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSD-3-Clause CC-BY-SA-4.0 ISC MIT MPL-2.0-no-copyleft-exception WTFPL
Requires: cri-o-bin
Requires: cri-o-config
Requires: cri-o-data
Requires: cri-o-license
Requires: cri-o-man
BuildRequires : buildreq-golang
BuildRequires : golang-github-cpuguy83-go-md2man
BuildRequires : gpgme-dev
BuildRequires : libassuan-dev
BuildRequires : libgpg-error-dev
BuildRequires : pkgconfig(glib-2.0)
Patch1: 0002-Fix-path-of-crio.service-s-ExecStart-crio-binary.patch
Patch2: 0003-Update-default-crio.conf-file-for-Clear-Linux.patch
Patch3: 0004-Add-bin-subfolder.patch

%description
This repository provides supplementary Go time packages.

%package bin
Summary: bin components for the cri-o package.
Group: Binaries
Requires: cri-o-data
Requires: cri-o-config
Requires: cri-o-license
Requires: cri-o-man

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
Requires: cri-o-man

%description doc
doc components for the cri-o package.


%package license
Summary: license components for the cri-o package.
Group: Default

%description license
license components for the cri-o package.


%package man
Summary: man components for the cri-o package.
Group: Default

%description man
man components for the cri-o package.


%prep
%setup -q -n cri-o-1.10.5
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1532361946
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1532361946
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/cri-o
cp LICENSE %{buildroot}/usr/share/doc/cri-o/LICENSE
cp vendor/github.com/Azure/go-ansiterm/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_github.com_Azure_go-ansiterm_LICENSE
cp vendor/github.com/BurntSushi/toml/COPYING %{buildroot}/usr/share/doc/cri-o/vendor_github.com_BurntSushi_toml_COPYING
cp vendor/github.com/Microsoft/go-winio/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_github.com_Microsoft_go-winio_LICENSE
cp vendor/github.com/Microsoft/go-winio/archive/tar/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_github.com_Microsoft_go-winio_archive_tar_LICENSE
cp vendor/github.com/Microsoft/hcsshim/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_github.com_Microsoft_hcsshim_LICENSE
cp vendor/github.com/beorn7/perks/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_github.com_beorn7_perks_LICENSE
cp vendor/github.com/blang/semver/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_github.com_blang_semver_LICENSE
cp vendor/github.com/containerd/cgroups/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_github.com_containerd_cgroups_LICENSE
cp vendor/github.com/containerd/console/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_github.com_containerd_console_LICENSE
cp vendor/github.com/containernetworking/cni/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_github.com_containernetworking_cni_LICENSE
cp vendor/github.com/containers/image/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_github.com_containers_image_LICENSE
cp vendor/github.com/containers/storage/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_github.com_containers_storage_LICENSE
cp vendor/github.com/containers/storage/NOTICE %{buildroot}/usr/share/doc/cri-o/vendor_github.com_containers_storage_NOTICE
cp vendor/github.com/coreos/go-systemd/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_github.com_coreos_go-systemd_LICENSE
cp vendor/github.com/coreos/pkg/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_github.com_coreos_pkg_LICENSE
cp vendor/github.com/cri-o/ocicni/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_github.com_cri-o_ocicni_LICENSE
cp vendor/github.com/cyphar/filepath-securejoin/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_github.com_cyphar_filepath-securejoin_LICENSE
cp vendor/github.com/davecgh/go-spew/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_github.com_davecgh_go-spew_LICENSE
cp vendor/github.com/docker/distribution/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_github.com_docker_distribution_LICENSE
cp vendor/github.com/docker/docker-credential-helpers/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_github.com_docker_docker-credential-helpers_LICENSE
cp vendor/github.com/docker/docker/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_github.com_docker_docker_LICENSE
cp vendor/github.com/docker/docker/NOTICE %{buildroot}/usr/share/doc/cri-o/vendor_github.com_docker_docker_NOTICE
cp vendor/github.com/docker/docker/pkg/symlink/LICENSE.APACHE %{buildroot}/usr/share/doc/cri-o/vendor_github.com_docker_docker_pkg_symlink_LICENSE.APACHE
cp vendor/github.com/docker/docker/pkg/symlink/LICENSE.BSD %{buildroot}/usr/share/doc/cri-o/vendor_github.com_docker_docker_pkg_symlink_LICENSE.BSD
cp vendor/github.com/docker/go-connections/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_github.com_docker_go-connections_LICENSE
cp vendor/github.com/docker/go-units/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_github.com_docker_go-units_LICENSE
cp vendor/github.com/docker/libtrust/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_github.com_docker_libtrust_LICENSE
cp vendor/github.com/docker/spdystream/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_github.com_docker_spdystream_LICENSE
cp vendor/github.com/docker/spdystream/LICENSE.docs %{buildroot}/usr/share/doc/cri-o/vendor_github.com_docker_spdystream_LICENSE.docs
cp vendor/github.com/emicklei/go-restful/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_github.com_emicklei_go-restful_LICENSE
cp vendor/github.com/fsnotify/fsnotify/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_github.com_fsnotify_fsnotify_LICENSE
cp vendor/github.com/ghodss/yaml/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_github.com_ghodss_yaml_LICENSE
cp vendor/github.com/go-zoo/bone/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_github.com_go-zoo_bone_LICENSE
cp vendor/github.com/godbus/dbus/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_github.com_godbus_dbus_LICENSE
cp vendor/github.com/gogo/protobuf/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_github.com_gogo_protobuf_LICENSE
cp vendor/github.com/golang/glog/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_github.com_golang_glog_LICENSE
cp vendor/github.com/golang/groupcache/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_github.com_golang_groupcache_LICENSE
cp vendor/github.com/golang/protobuf/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_github.com_golang_protobuf_LICENSE
cp vendor/github.com/google/gofuzz/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_github.com_google_gofuzz_LICENSE
cp vendor/github.com/googleapis/gnostic/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_github.com_googleapis_gnostic_LICENSE
cp vendor/github.com/gorilla/context/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_github.com_gorilla_context_LICENSE
cp vendor/github.com/gorilla/mux/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_github.com_gorilla_mux_LICENSE
cp vendor/github.com/hashicorp/errwrap/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_github.com_hashicorp_errwrap_LICENSE
cp vendor/github.com/hashicorp/go-multierror/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_github.com_hashicorp_go-multierror_LICENSE
cp vendor/github.com/hashicorp/golang-lru/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_github.com_hashicorp_golang-lru_LICENSE
cp vendor/github.com/hpcloud/tail/LICENSE.txt %{buildroot}/usr/share/doc/cri-o/vendor_github.com_hpcloud_tail_LICENSE.txt
cp vendor/github.com/imdario/mergo/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_github.com_imdario_mergo_LICENSE
cp vendor/github.com/json-iterator/go/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_github.com_json-iterator_go_LICENSE
cp vendor/github.com/kr/pty/License %{buildroot}/usr/share/doc/cri-o/vendor_github.com_kr_pty_License
cp vendor/github.com/matttproud/golang_protobuf_extensions/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_github.com_matttproud_golang_protobuf_extensions_LICENSE
cp vendor/github.com/mistifyio/go-zfs/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_github.com_mistifyio_go-zfs_LICENSE
cp vendor/github.com/mrunalp/fileutils/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_github.com_mrunalp_fileutils_LICENSE
cp vendor/github.com/mtrmac/gpgme/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_github.com_mtrmac_gpgme_LICENSE
cp vendor/github.com/opencontainers/go-digest/LICENSE.code %{buildroot}/usr/share/doc/cri-o/vendor_github.com_opencontainers_go-digest_LICENSE.code
cp vendor/github.com/opencontainers/go-digest/LICENSE.docs %{buildroot}/usr/share/doc/cri-o/vendor_github.com_opencontainers_go-digest_LICENSE.docs
cp vendor/github.com/opencontainers/image-spec/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_github.com_opencontainers_image-spec_LICENSE
cp vendor/github.com/opencontainers/runc/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_github.com_opencontainers_runc_LICENSE
cp vendor/github.com/opencontainers/runtime-spec/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_github.com_opencontainers_runtime-spec_LICENSE
cp vendor/github.com/opencontainers/runtime-tools/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_github.com_opencontainers_runtime-tools_LICENSE
cp vendor/github.com/opencontainers/selinux/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_github.com_opencontainers_selinux_LICENSE
cp vendor/github.com/ostreedev/ostree-go/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_github.com_ostreedev_ostree-go_LICENSE
cp vendor/github.com/pkg/errors/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_github.com_pkg_errors_LICENSE
cp vendor/github.com/pmezard/go-difflib/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_github.com_pmezard_go-difflib_LICENSE
cp vendor/github.com/pquerna/ffjson/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_github.com_pquerna_ffjson_LICENSE
cp vendor/github.com/prometheus/client_golang/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_github.com_prometheus_client_golang_LICENSE
cp vendor/github.com/prometheus/client_golang/NOTICE %{buildroot}/usr/share/doc/cri-o/vendor_github.com_prometheus_client_golang_NOTICE
cp vendor/github.com/prometheus/client_model/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_github.com_prometheus_client_model_LICENSE
cp vendor/github.com/prometheus/common/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_github.com_prometheus_common_LICENSE
cp vendor/github.com/prometheus/procfs/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_github.com_prometheus_procfs_LICENSE
cp vendor/github.com/renstrom/dedent/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_github.com_renstrom_dedent_LICENSE
cp vendor/github.com/seccomp/libseccomp-golang/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_github.com_seccomp_libseccomp-golang_LICENSE
cp vendor/github.com/sirupsen/logrus/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_github.com_sirupsen_logrus_LICENSE
cp vendor/github.com/soheilhy/cmux/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_github.com_soheilhy_cmux_LICENSE
cp vendor/github.com/spf13/pflag/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_github.com_spf13_pflag_LICENSE
cp vendor/github.com/stretchr/testify/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_github.com_stretchr_testify_LICENSE
cp vendor/github.com/syndtr/gocapability/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_github.com_syndtr_gocapability_LICENSE
cp vendor/github.com/tchap/go-patricia/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_github.com_tchap_go-patricia_LICENSE
cp vendor/github.com/urfave/cli/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_github.com_urfave_cli_LICENSE
cp vendor/github.com/vbatts/tar-split/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_github.com_vbatts_tar-split_LICENSE
cp vendor/github.com/vishvananda/netlink/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_github.com_vishvananda_netlink_LICENSE
cp vendor/github.com/vishvananda/netns/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_github.com_vishvananda_netns_LICENSE
cp vendor/github.com/xeipuuv/gojsonpointer/LICENSE-APACHE-2.0.txt %{buildroot}/usr/share/doc/cri-o/vendor_github.com_xeipuuv_gojsonpointer_LICENSE-APACHE-2.0.txt
cp vendor/github.com/xeipuuv/gojsonreference/LICENSE-APACHE-2.0.txt %{buildroot}/usr/share/doc/cri-o/vendor_github.com_xeipuuv_gojsonreference_LICENSE-APACHE-2.0.txt
cp vendor/github.com/xeipuuv/gojsonschema/LICENSE-APACHE-2.0.txt %{buildroot}/usr/share/doc/cri-o/vendor_github.com_xeipuuv_gojsonschema_LICENSE-APACHE-2.0.txt
cp vendor/golang.org/x/crypto/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_golang.org_x_crypto_LICENSE
cp vendor/golang.org/x/net/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_golang.org_x_net_LICENSE
cp vendor/golang.org/x/sys/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_golang.org_x_sys_LICENSE
cp vendor/golang.org/x/text/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_golang.org_x_text_LICENSE
cp vendor/golang.org/x/time/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_golang.org_x_time_LICENSE
cp vendor/google.golang.org/grpc/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_google.golang.org_grpc_LICENSE
cp vendor/gopkg.in/cheggaaa/pb.v1/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_gopkg.in_cheggaaa_pb.v1_LICENSE
cp vendor/gopkg.in/fsnotify.v1/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_gopkg.in_fsnotify.v1_LICENSE
cp vendor/gopkg.in/inf.v0/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_gopkg.in_inf.v0_LICENSE
cp vendor/gopkg.in/mgo.v2/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_gopkg.in_mgo.v2_LICENSE
cp vendor/gopkg.in/square/go-jose.v2/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_gopkg.in_square_go-jose.v2_LICENSE
cp vendor/gopkg.in/square/go-jose.v2/json/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_gopkg.in_square_go-jose.v2_json_LICENSE
cp vendor/gopkg.in/tomb.v1/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_gopkg.in_tomb.v1_LICENSE
cp vendor/gopkg.in/yaml.v2/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_gopkg.in_yaml.v2_LICENSE
cp vendor/gopkg.in/yaml.v2/LICENSE.libyaml %{buildroot}/usr/share/doc/cri-o/vendor_gopkg.in_yaml.v2_LICENSE.libyaml
cp vendor/k8s.io/api/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_k8s.io_api_LICENSE
cp vendor/k8s.io/apiextensions-apiserver/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_k8s.io_apiextensions-apiserver_LICENSE
cp vendor/k8s.io/apimachinery/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_k8s.io_apimachinery_LICENSE
cp vendor/k8s.io/apiserver/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_k8s.io_apiserver_LICENSE
cp vendor/k8s.io/client-go/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_k8s.io_client-go_LICENSE
cp vendor/k8s.io/kube-openapi/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_k8s.io_kube-openapi_LICENSE
cp vendor/k8s.io/kubernetes/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_k8s.io_kubernetes_LICENSE
cp vendor/k8s.io/kubernetes/third_party/forked/golang/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_k8s.io_kubernetes_third_party_forked_golang_LICENSE
cp vendor/k8s.io/utils/LICENSE %{buildroot}/usr/share/doc/cri-o/vendor_k8s.io_utils_LICENSE
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
/usr/libexec/crio/conmon
/usr/libexec/crio/pause

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/system/cri-o.service
/usr/lib/systemd/system/crio-shutdown.service
/usr/lib/systemd/system/crio.service

%files data
%defattr(-,root,root,-)
/usr/share/cri-o/crio-umount.conf
/usr/share/cri-o/crio.conf
/usr/share/cri-o/seccomp.json

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/cri\-o/*

%files license
%defattr(-,root,root,-)
/usr/share/doc/cri-o/LICENSE
/usr/share/doc/cri-o/vendor_github.com_Azure_go-ansiterm_LICENSE
/usr/share/doc/cri-o/vendor_github.com_BurntSushi_toml_COPYING
/usr/share/doc/cri-o/vendor_github.com_Microsoft_go-winio_LICENSE
/usr/share/doc/cri-o/vendor_github.com_Microsoft_go-winio_archive_tar_LICENSE
/usr/share/doc/cri-o/vendor_github.com_Microsoft_hcsshim_LICENSE
/usr/share/doc/cri-o/vendor_github.com_beorn7_perks_LICENSE
/usr/share/doc/cri-o/vendor_github.com_blang_semver_LICENSE
/usr/share/doc/cri-o/vendor_github.com_containerd_cgroups_LICENSE
/usr/share/doc/cri-o/vendor_github.com_containerd_console_LICENSE
/usr/share/doc/cri-o/vendor_github.com_containernetworking_cni_LICENSE
/usr/share/doc/cri-o/vendor_github.com_containers_image_LICENSE
/usr/share/doc/cri-o/vendor_github.com_containers_storage_LICENSE
/usr/share/doc/cri-o/vendor_github.com_coreos_go-systemd_LICENSE
/usr/share/doc/cri-o/vendor_github.com_coreos_pkg_LICENSE
/usr/share/doc/cri-o/vendor_github.com_cri-o_ocicni_LICENSE
/usr/share/doc/cri-o/vendor_github.com_cyphar_filepath-securejoin_LICENSE
/usr/share/doc/cri-o/vendor_github.com_davecgh_go-spew_LICENSE
/usr/share/doc/cri-o/vendor_github.com_docker_distribution_LICENSE
/usr/share/doc/cri-o/vendor_github.com_docker_docker-credential-helpers_LICENSE
/usr/share/doc/cri-o/vendor_github.com_docker_docker_LICENSE
/usr/share/doc/cri-o/vendor_github.com_docker_docker_pkg_symlink_LICENSE.APACHE
/usr/share/doc/cri-o/vendor_github.com_docker_docker_pkg_symlink_LICENSE.BSD
/usr/share/doc/cri-o/vendor_github.com_docker_go-connections_LICENSE
/usr/share/doc/cri-o/vendor_github.com_docker_go-units_LICENSE
/usr/share/doc/cri-o/vendor_github.com_docker_libtrust_LICENSE
/usr/share/doc/cri-o/vendor_github.com_docker_spdystream_LICENSE
/usr/share/doc/cri-o/vendor_github.com_docker_spdystream_LICENSE.docs
/usr/share/doc/cri-o/vendor_github.com_emicklei_go-restful_LICENSE
/usr/share/doc/cri-o/vendor_github.com_fsnotify_fsnotify_LICENSE
/usr/share/doc/cri-o/vendor_github.com_ghodss_yaml_LICENSE
/usr/share/doc/cri-o/vendor_github.com_go-zoo_bone_LICENSE
/usr/share/doc/cri-o/vendor_github.com_godbus_dbus_LICENSE
/usr/share/doc/cri-o/vendor_github.com_gogo_protobuf_LICENSE
/usr/share/doc/cri-o/vendor_github.com_golang_glog_LICENSE
/usr/share/doc/cri-o/vendor_github.com_golang_groupcache_LICENSE
/usr/share/doc/cri-o/vendor_github.com_golang_protobuf_LICENSE
/usr/share/doc/cri-o/vendor_github.com_google_gofuzz_LICENSE
/usr/share/doc/cri-o/vendor_github.com_googleapis_gnostic_LICENSE
/usr/share/doc/cri-o/vendor_github.com_gorilla_context_LICENSE
/usr/share/doc/cri-o/vendor_github.com_gorilla_mux_LICENSE
/usr/share/doc/cri-o/vendor_github.com_hashicorp_errwrap_LICENSE
/usr/share/doc/cri-o/vendor_github.com_hashicorp_go-multierror_LICENSE
/usr/share/doc/cri-o/vendor_github.com_hashicorp_golang-lru_LICENSE
/usr/share/doc/cri-o/vendor_github.com_hpcloud_tail_LICENSE.txt
/usr/share/doc/cri-o/vendor_github.com_imdario_mergo_LICENSE
/usr/share/doc/cri-o/vendor_github.com_json-iterator_go_LICENSE
/usr/share/doc/cri-o/vendor_github.com_matttproud_golang_protobuf_extensions_LICENSE
/usr/share/doc/cri-o/vendor_github.com_mistifyio_go-zfs_LICENSE
/usr/share/doc/cri-o/vendor_github.com_mrunalp_fileutils_LICENSE
/usr/share/doc/cri-o/vendor_github.com_mtrmac_gpgme_LICENSE
/usr/share/doc/cri-o/vendor_github.com_opencontainers_go-digest_LICENSE.code
/usr/share/doc/cri-o/vendor_github.com_opencontainers_go-digest_LICENSE.docs
/usr/share/doc/cri-o/vendor_github.com_opencontainers_image-spec_LICENSE
/usr/share/doc/cri-o/vendor_github.com_opencontainers_runc_LICENSE
/usr/share/doc/cri-o/vendor_github.com_opencontainers_runtime-spec_LICENSE
/usr/share/doc/cri-o/vendor_github.com_opencontainers_runtime-tools_LICENSE
/usr/share/doc/cri-o/vendor_github.com_opencontainers_selinux_LICENSE
/usr/share/doc/cri-o/vendor_github.com_ostreedev_ostree-go_LICENSE
/usr/share/doc/cri-o/vendor_github.com_pkg_errors_LICENSE
/usr/share/doc/cri-o/vendor_github.com_pmezard_go-difflib_LICENSE
/usr/share/doc/cri-o/vendor_github.com_pquerna_ffjson_LICENSE
/usr/share/doc/cri-o/vendor_github.com_prometheus_client_golang_LICENSE
/usr/share/doc/cri-o/vendor_github.com_prometheus_client_model_LICENSE
/usr/share/doc/cri-o/vendor_github.com_prometheus_common_LICENSE
/usr/share/doc/cri-o/vendor_github.com_prometheus_procfs_LICENSE
/usr/share/doc/cri-o/vendor_github.com_renstrom_dedent_LICENSE
/usr/share/doc/cri-o/vendor_github.com_seccomp_libseccomp-golang_LICENSE
/usr/share/doc/cri-o/vendor_github.com_sirupsen_logrus_LICENSE
/usr/share/doc/cri-o/vendor_github.com_soheilhy_cmux_LICENSE
/usr/share/doc/cri-o/vendor_github.com_spf13_pflag_LICENSE
/usr/share/doc/cri-o/vendor_github.com_stretchr_testify_LICENSE
/usr/share/doc/cri-o/vendor_github.com_syndtr_gocapability_LICENSE
/usr/share/doc/cri-o/vendor_github.com_tchap_go-patricia_LICENSE
/usr/share/doc/cri-o/vendor_github.com_urfave_cli_LICENSE
/usr/share/doc/cri-o/vendor_github.com_vbatts_tar-split_LICENSE
/usr/share/doc/cri-o/vendor_github.com_vishvananda_netlink_LICENSE
/usr/share/doc/cri-o/vendor_github.com_vishvananda_netns_LICENSE
/usr/share/doc/cri-o/vendor_github.com_xeipuuv_gojsonpointer_LICENSE-APACHE-2.0.txt
/usr/share/doc/cri-o/vendor_github.com_xeipuuv_gojsonreference_LICENSE-APACHE-2.0.txt
/usr/share/doc/cri-o/vendor_github.com_xeipuuv_gojsonschema_LICENSE-APACHE-2.0.txt
/usr/share/doc/cri-o/vendor_golang.org_x_crypto_LICENSE
/usr/share/doc/cri-o/vendor_golang.org_x_net_LICENSE
/usr/share/doc/cri-o/vendor_golang.org_x_sys_LICENSE
/usr/share/doc/cri-o/vendor_golang.org_x_text_LICENSE
/usr/share/doc/cri-o/vendor_golang.org_x_time_LICENSE
/usr/share/doc/cri-o/vendor_google.golang.org_grpc_LICENSE
/usr/share/doc/cri-o/vendor_gopkg.in_cheggaaa_pb.v1_LICENSE
/usr/share/doc/cri-o/vendor_gopkg.in_fsnotify.v1_LICENSE
/usr/share/doc/cri-o/vendor_gopkg.in_inf.v0_LICENSE
/usr/share/doc/cri-o/vendor_gopkg.in_mgo.v2_LICENSE
/usr/share/doc/cri-o/vendor_gopkg.in_square_go-jose.v2_LICENSE
/usr/share/doc/cri-o/vendor_gopkg.in_square_go-jose.v2_json_LICENSE
/usr/share/doc/cri-o/vendor_gopkg.in_tomb.v1_LICENSE
/usr/share/doc/cri-o/vendor_gopkg.in_yaml.v2_LICENSE
/usr/share/doc/cri-o/vendor_gopkg.in_yaml.v2_LICENSE.libyaml
/usr/share/doc/cri-o/vendor_k8s.io_api_LICENSE
/usr/share/doc/cri-o/vendor_k8s.io_apiextensions-apiserver_LICENSE
/usr/share/doc/cri-o/vendor_k8s.io_apimachinery_LICENSE
/usr/share/doc/cri-o/vendor_k8s.io_apiserver_LICENSE
/usr/share/doc/cri-o/vendor_k8s.io_client-go_LICENSE
/usr/share/doc/cri-o/vendor_k8s.io_kube-openapi_LICENSE
/usr/share/doc/cri-o/vendor_k8s.io_kubernetes_LICENSE
/usr/share/doc/cri-o/vendor_k8s.io_kubernetes_third_party_forked_golang_LICENSE
/usr/share/doc/cri-o/vendor_k8s.io_utils_LICENSE

%files man
%defattr(-,root,root,-)
/usr/share/man/man5/crio.conf.5
/usr/share/man/man8/crio.8
