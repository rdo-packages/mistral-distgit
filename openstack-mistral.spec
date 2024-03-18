%global milestone .0rc1
%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x2ef3fe0ec2b075ab7458b5f8b702b20b13df2318

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
# we are excluding some BRs from automatic generator
%global excluded_brs doc8 bandit pre-commit hacking flake8-import-order os-api-ref unittest2
# Exclude sphinx from BRs if docs are disabled
%if ! 0%{?with_doc}
%global excluded_brs %{excluded_brs} sphinx openstackdocstheme
%endif
%global service mistral
%global rhosp 0

%global with_doc 1

%global common_desc \
Mistral is a workflow service. \
Most business processes consist of multiple distinct interconnected steps that \
need to be executed in a particular order in a distributed environment. One can \
describe such process as a set of tasks and task relations and upload such \
description to Mistral so that it takes care of state management, correct \
execution order, parallelism, synchronization and high availability.

Name:           openstack-mistral
Version:        18.0.0
Release:        0.1%{?milestone}%{?dist}
Summary:        Task Orchestration and Scheduling service for OpenStack cloud
License:        Apache-2.0
URL:            https://launchpad.net/mistral
Source0:        https://tarballs.openstack.org/%{service}/%{service}-%{upstream_version}.tar.gz
#
# patches_base=18.0.0.0rc1
#

Source1:        mistral.logrotate
# Systemd scripts
Source10:       openstack-mistral-api.service
Source11:       openstack-mistral-engine.service
Source12:       openstack-mistral-executor.service
Source13:       openstack-mistral-all.service
Source14:       openstack-mistral-event-engine.service
Source15:       openstack-mistral-notifier.service
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{service}/%{service}-%{upstream_version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildArch:      noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif

BuildRequires:  git-core
BuildRequires:  openstack-macros
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  systemd

%description
%{summary}


%package -n     python3-%{service}
Summary:        Mistral Python libraries

Requires:    python3-mistral-extra >= 10.0.0

%description -n python3-%{service}
%{common_desc}

This package contains the Python libraries.

%package        common
Summary: Components common for OpenStack Mistral

Requires:       python3-%{service} = %{version}-%{release}

%{?systemd_ordering}

%description    common
%{common_desc}

This package contains the common files.

%package        api
Summary: OpenStack Mistral API daemon

Requires:       %{name}-common = %{version}-%{release}

%description    api
OpenStack rest API to the Mistral Engine.
.
This package contains the ReST API.

%package        engine
Summary: OpenStack Mistral Engine daemon

Requires:       %{name}-common = %{version}-%{release}

%description    engine
OpenStack Mistral Engine service.
.
This package contains the mistral engine, which is one of core services of
mistral.

%package        executor
Summary: OpenStack Mistral Executor daemon

Requires:       %{name}-common = %{version}-%{release}

%description    executor
OpenStack Mistral Executor service.
.
This package contains the mistral executor, which is one of core services of
mistral, and which the API servers will use.

%package        event-engine
Summary: Openstack Mistral Event Engine daemon

Requires:       %{name}-common = %{version}-%{release}

%description    event-engine
Openstack Mistral Event Engine service.
.
This package contains the mistral event engine, which is one of the core
services of mistral.

%package        notifier
Summary: Openstack Mistral Notifier daemon

Requires:       %{name}-common = %{version}-%{release}

%description    notifier
Openstack Mistral Notifier service.
.
This package contains the mistral notifier, which is one of the core
services of mistral.

%package        all
Summary: OpenStack Mistral All-in-one daemon

Requires:       %{name}-common = %{version}-%{release}

%description    all
OpenStack Mistral All service.
.
This package contains the mistral api, engine, and executor service as
an all-in-one process.

%package -n python3-mistral-tests
Summary:        Mistral tests
Requires:       %{name}-common = %{version}-%{release}
Requires:       python3-mock
Requires:       python3-yaml >= 5.1
Requires:       python3-zake >= 0.1.6

%description -n python3-mistral-tests
This package contains the mistral test files.


%if 0%{?with_doc}
%package        doc
Summary:        Documentation for OpenStack Workflow Service

BuildRequires: python3-openstackdocstheme

%description    doc
OpenStack Mistral documentation.
.
This package contains the documentation.
%endif

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n mistral-%{upstream_version} -S git

sed -i '1i #!/usr/bin/python' tools/sync_db.py

sed -i /^[[:space:]]*-c{env:.*_CONSTRAINTS_FILE.*/d tox.ini
sed -i "s/^deps = -c{env:.*_CONSTRAINTS_FILE.*/deps =/" tox.ini
sed -i /^minversion.*/d tox.ini
sed -i /^requires.*virtualenv.*/d tox.ini

# py_mini_racer is an optional requirement
sed -i '/.*py_mini_racer.*/d' tox.ini

# not running linters
rm -f mistral/tests/unit/hacking/test_checks.py

# Exclude some bad-known BRs
for pkg in %{excluded_brs}; do
  for reqfile in doc/requirements.txt test-requirements.txt; do
    if [ -f $reqfile ]; then
      sed -i /^${pkg}.*/d $reqfile
    fi
  done
done

# Automatic BR generation
%generate_buildrequires
%if 0%{?with_doc}
  %pyproject_buildrequires -t -e %{default_toxenv},docs
%else
  %pyproject_buildrequires -t -e %{default_toxenv}
%endif

%build
%pyproject_wheel

%install
%pyproject_install

export PYTHONPATH=%{buildroot}/%{python3_sitelib}
oslo-config-generator --config-file tools/config/config-generator.mistral.conf \
                      --output-file etc/mistral.conf.sample

%if 0%{?with_doc}
%tox -e docs
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif

mkdir -p %{buildroot}/etc/mistral/
mkdir -p %{buildroot}/var/log/mistral
mkdir -p %{buildroot}/var/run/mistral
mkdir -p %{buildroot}/var/lib/mistral

install -p -D -m 644 %SOURCE10 %{buildroot}%{_unitdir}/openstack-mistral-api.service
install -p -D -m 644 %SOURCE11 %{buildroot}%{_unitdir}/openstack-mistral-engine.service
install -p -D -m 644 %SOURCE12 %{buildroot}%{_unitdir}/openstack-mistral-executor.service
install -p -D -m 644 %SOURCE13 %{buildroot}%{_unitdir}/openstack-mistral-all.service
install -p -D -m 644 %SOURCE14 %{buildroot}%{_unitdir}/openstack-mistral-event-engine.service
install -p -D -m 644 %SOURCE15 %{buildroot}%{_unitdir}/openstack-mistral-notifier.service

install -p -D -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/logrotate.d/openstack-mistral
install -p -D -m 640 etc/mistral.conf.sample \
                     %{buildroot}%{_sysconfdir}/mistral/mistral.conf
install -p -D -m 640 etc/logging.conf.sample \
                     %{buildroot}%{_sysconfdir}/mistral/logging.conf
install -p -D -m 640 etc/wf_trace_logging.conf.sample \
                     %{buildroot}%{_sysconfdir}/mistral/wf_trace_logging.conf
install -p -D -m 640 tools/sync_db.py \
                     %{buildroot}/usr/bin/mistral-db-sync
chmod +x %{buildroot}/usr/bin/mistral*

# Fix shebangs for Python 3-only distros
%py3_shebang_fix %{buildroot}/usr/bin/mistral-db-sync

%pre common
USERNAME=mistral
GROUPNAME=$USERNAME
HOMEDIR=/var/lib/mistral
getent group $GROUPNAME >/dev/null || groupadd -r $GROUPNAME
getent passwd $USERNAME >/dev/null ||
    useradd -r -g $GROUPNAME -G $GROUPNAME -d $HOMEDIR -s /sbin/nologin \
            -c "Mistral Daemons" $USERNAME
# Related Bug LP#1778269
if [ "$(getent passwd $USERNAME | cut -d: -f6)" != "$HOMEDIR" ]; then
    usermod -m -d $HOMEDIR $USERNAME
fi
exit 0


%post api
%systemd_post openstack-mistral-api.service
%preun api
%systemd_preun openstack-mistral-api.service
%postun api
%systemd_postun_with_restart openstack-mistral-api.service

%post engine
%systemd_post openstack-mistral-engine.service
%preun engine
%systemd_preun openstack-mistral-engine.service
%postun engine
%systemd_postun_with_restart openstack-mistral-engine.service

%post executor
%systemd_post openstack-mistral-executor.service
%preun executor
%systemd_preun openstack-mistral-executor.service
%postun executor
%systemd_postun_with_restart openstack-mistral-executor.service

%post event-engine
%systemd_post openstack-mistral-event-engine.service
%preun event-engine
%systemd_preun openstack-mistral-event-engine.service
%postun event-engine
%systemd_postun_with_restart openstack-mistral-event-engine.service

%post notifier
%systemd_post openstack-mistral-notifier.service
%preun notifier
%systemd_preun openstack-mistral-notifier.service
%postun notifier
%systemd_postun_with_restart openstack-mistral-notifier.service

%post all
%systemd_post openstack-mistral-all.service
%preun all
%systemd_preun openstack-mistral-all.service
%postun all
%systemd_postun_with_restart openstack-mistral-all.service

%check
%tox -e %{default_toxenv}

%files api
%config(noreplace) %attr(-, root, root) %{_unitdir}/openstack-mistral-api.service

%files common
%dir %{_sysconfdir}/mistral
%config(noreplace) %attr(-, mistral, mistral) %{_sysconfdir}/mistral/*
%config(noreplace) %{_sysconfdir}/logrotate.d/openstack-mistral
%{_bindir}/mistral-*
%dir %attr(755, mistral, mistral) /var/run/mistral
%dir %attr(750, mistral, mistral) /var/lib/mistral
%dir %attr(750, mistral, mistral) /var/log/mistral


%if 0%{?with_doc}
%files doc
%doc doc/build/html
%endif

%files engine
%config(noreplace) %attr(-, root, root) %{_unitdir}/openstack-mistral-engine.service

%files executor
%config(noreplace) %attr(-, root, root) %{_unitdir}/openstack-mistral-executor.service

%files event-engine
%config(noreplace) %attr(-, root, root) %{_unitdir}/openstack-mistral-event-engine.service

%files notifier
%config(noreplace) %attr(-, root, root) %{_unitdir}/openstack-mistral-notifier.service

%files all
%config(noreplace) %attr(-, root, root) %{_unitdir}/openstack-mistral-all.service


%files -n python3-%{service}
%{python3_sitelib}/%{service}
%{python3_sitelib}/%{service}-*.dist-info
%exclude %{python3_sitelib}/mistral/tests

%files -n python3-mistral-tests
%license LICENSE
%{python3_sitelib}/mistral/tests

%changelog
* Mon Mar 18 2024 RDO <dev@lists.rdoproject.org> 18.0.0-0.1.0rc1
- Update to 18.0.0.0rc1


