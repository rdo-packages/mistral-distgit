# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver %{python3_pkgversion}
%else
%global pyver 2
%endif

%global pyver_bin python%{pyver}
%global pyver_sitelib %python%{pyver}_sitelib
%global pyver_install %py%{pyver}_install
%global pyver_build %py%{pyver}_build
# End of macros for py2/py3 compatibility

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
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
Version:        XXX
Release:        XXX
Summary:        Task Orchestration and Scheduling service for OpenStack cloud
License:        ASL 2.0
URL:            https://launchpad.net/mistral
Source0:        https://tarballs.openstack.org/%{service}/%{service}-%{upstream_version}.tar.gz
Source1:        mistral.logrotate
# Systemd scripts
Source10:       openstack-mistral-api.service
Source11:       openstack-mistral-engine.service
Source12:       openstack-mistral-executor.service
Source13:       openstack-mistral-all.service
Source14:       openstack-mistral-event-engine.service
Source15:       openstack-mistral-notifier.service

BuildArch:      noarch

BuildRequires:  git
BuildRequires:  openstack-macros
BuildRequires:  python%{pyver}-devel
BuildRequires:  python%{pyver}-oslo-config >= 2:5.2.0
BuildRequires:  python%{pyver}-pbr >= 2.0.0
BuildRequires:  systemd

%if %{pyver} == 3
BuildRequires:  /usr/bin/pathfix.py
%endif

%description
%{summary}


%package -n     python%{pyver}-%{service}
Summary:        Mistral Python libraries
%{?python_provide:%python_provide python%{pyver}-%{service}}

Requires:       python%{pyver}-alembic >= 0.9.6
Requires:       python%{pyver}-babel >= 2.3.4
Requires:       python%{pyver}-croniter >= 0.3.4
Requires:       python%{pyver}-cachetools >= 2.0.0
Requires:       python%{pyver}-eventlet >= 0.20.0
Requires:       python%{pyver}-iso8601 >= 0.1.9
Requires:       python%{pyver}-jinja2
Requires:       python%{pyver}-jsonschema >= 2.6.0
Requires:       python%{pyver}-kombu
Requires:       python%{pyver}-paramiko >= 2.0
Requires:       python%{pyver}-pbr >= 2.0.0
Requires:       python%{pyver}-pecan >= 1.2.1
Requires:       python%{pyver}-requests >= 2.14.2
Requires:       python%{pyver}-six >= 1.10.0
Requires:       python%{pyver}-sqlalchemy >= 1.2.5
Requires:       python%{pyver}-tenacity >= 4.4.0
Requires:       python%{pyver}-wsme >= 0.8
Requires:       python%{pyver}-yaql >= 1.1.3
# OpenStack dependencies
Requires:       python%{pyver}-oslo-concurrency >= 3.25.0
Requires:       python%{pyver}-oslo-config >= 2:5.2.0
Requires:       python%{pyver}-oslo-context >= 2.19.2
Requires:       python%{pyver}-oslo-db >= 4.27.0
Requires:       python%{pyver}-oslo-i18n >= 3.15.3
Requires:       python%{pyver}-oslo-middleware >= 3.31.0
Requires:       python%{pyver}-oslo-messaging >= 5.29.0
Requires:       python%{pyver}-oslo-utils >= 3.33.0
Requires:       python%{pyver}-oslo-log >= 3.36.0
Requires:       python%{pyver}-oslo-serialization >= 2.18.0
Requires:       python%{pyver}-oslo-service >= 1.24.0
Requires:       python%{pyver}-oslo-policy >= 1.30.0
Requires:       python%{pyver}-osprofiler >= 1.4.0
Requires:       python%{pyver}-stevedore >= 1.20.0
Requires:       python%{pyver}-tooz >= 1.58.0
Requires:       python%{pyver}-aodhclient >= 0.9.0
Requires:       python%{pyver}-barbicanclient >= 4.0.0
Requires:       python%{pyver}-cinderclient >= 3.3.0
Requires:       python%{pyver}-glanceclient >= 1:2.8.0
Requires:       python%{pyver}-gnocchiclient >= 3.3.1
Requires:       python%{pyver}-ironicclient >= 2.3.0
Requires:       python%{pyver}-ironic-inspector-client >= 1.5.0
Requires:       python%{pyver}-heatclient >= 1.10.0
Requires:       python%{pyver}-keystoneclient >= 1:3.8.0
Requires:       python%{pyver}-keystonemiddleware >= 4.17.0
Requires:       python%{pyver}-neutronclient >= 6.3.0
Requires:       python%{pyver}-novaclient >= 1:9.1.0
Requires:       python%{pyver}-swiftclient >= 3.2.0
Requires:       python%{pyver}-zaqarclient >= 1.0.0
Requires:       python%{pyver}-mistralclient >= 3.1.0
Requires:       python%{pyver}-mistral-lib >= 0.3.0
Requires:       python%{pyver}-designateclient >= 2.7.0
Requires:       python%{pyver}-magnumclient >= 2.1.0
%if 0%{rhosp} == 0
Requires:       python%{pyver}-glareclient >= 0.3.0
Requires:       python%{pyver}-muranoclient >= 0.8.2
Requires:       python%{pyver}-senlinclient >= 1.1.0
Requires:       python%{pyver}-tackerclient >= 0.8.0
%endif
Requires:       python%{pyver}-troveclient >= 2.2.0

# Handle python2 exceptions
%if %{pyver} == 2
Requires:       python-jwt >= 1.0.1
Requires:       python-retrying >= 1.2.3
Requires:       python-networkx >= 1.10
Requires:       PyYAML >= 3.10
%else
Requires:       python%{pyver}-jwt >= 1.0.1
Requires:       python%{pyver}-retrying >= 1.2.3
Requires:       python%{pyver}-networkx >= 1.10
Requires:       python%{pyver}-PyYAML >= 3.10
%endif

%description -n python%{pyver}-%{service}
%{common_desc}

This package contains the Python libraries.

%package        common
Summary: Components common for OpenStack Mistral

Requires:       python%{pyver}-%{service} = %{version}-%{release}
%if 0%{?rhel} && 0%{?rhel} < 8
%{?systemd_requires}
%else
%{?systemd_ordering} # does not exist on EL7
%endif

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

%package -n python%{pyver}-mistral-tests
Summary:        Mistral tests
%{?python_provide:%python_provide python%{pyver}-mistral-tests}
Requires:       %{name}-common = %{version}-%{release}
Requires:       python%{pyver}-mock

%description -n python%{pyver}-mistral-tests
This package contains the mistral test files.


%if 0%{?with_doc}
%package        doc
Summary:        Documentation for OpenStack Workflow Service

BuildRequires:  python%{pyver}-sphinx
BuildRequires:  python%{pyver}-openstackdocstheme
BuildRequires:  python%{pyver}-sphinxcontrib-pecanwsme
BuildRequires:  python%{pyver}-wsme
BuildRequires:  python%{pyver}-croniter
BuildRequires:  python%{pyver}-eventlet
BuildRequires:  python%{pyver}-jsonschema
BuildRequires:  python%{pyver}-keystoneclient
BuildRequires:  python%{pyver}-keystonemiddleware
BuildRequires:  python%{pyver}-mistral-lib
BuildRequires:  python%{pyver}-oslo-db
BuildRequires:  python%{pyver}-oslo-log
BuildRequires:  python%{pyver}-oslo-messaging
BuildRequires:  python%{pyver}-oslo-policy
BuildRequires:  python%{pyver}-osprofiler
BuildRequires:  python%{pyver}-pecan
BuildRequires:  python%{pyver}-tooz
BuildRequires:  python%{pyver}-yaql
BuildRequires:  openstack-macros

# Handle python2 exceptions
%if %{pyver} == 2
BuildRequires:  python-sphinxcontrib-httpdomain
BuildRequires:  python-networkx
%else
BuildRequires:  python%{pyver}-sphinxcontrib-httpdomain
BuildRequires:  python%{pyver}-networkx
%endif


%description    doc
OpenStack Mistral documentation.
.
This package contains the documentation.
%endif

%prep
%autosetup -n mistral-%{upstream_version} -S git

sed -i '1i #!/usr/bin/python' tools/sync_db.py

%py_req_cleanup

%build
%{pyver_build}
oslo-config-generator-%{pyver} --config-file tools/config/config-generator.mistral.conf \
                      --output-file etc/mistral.conf.sample

%install
%{pyver_install}


%if 0%{?with_doc}
export PYTHONPATH=.
sphinx-build-%{pyver} -W -b html doc/source doc/build/html
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
install -p -D -m 640 etc/policy.json \
                     %{buildroot}%{_sysconfdir}/mistral/policy.json
install -p -D -m 640 tools/sync_db.py \
                     %{buildroot}/usr/bin/mistral-db-sync
chmod +x %{buildroot}/usr/bin/mistral*

%if %{pyver} == 3
# Fix shebangs for Python 3-only distros
pathfix.py -pni "%{__python3} %{py3_shbang_opts}" %{buildroot}/usr/bin/mistral-db-sync
%endif

install -p -D -m 644 ./mistral/actions/openstack/mapping.json %{buildroot}%{pyver_sitelib}/%{service}/actions/openstack/mapping.json
install -p -D -m 644 ./mistral/db/sqlalchemy/migration/alembic.ini %{buildroot}%{pyver_sitelib}/%{service}/db/sqlalchemy/migration/alembic.ini
mkdir -p %{buildroot}/%{pyver_sitelib}/%{service}/resources/workflows/
mkdir -p %{buildroot}/%{pyver_sitelib}/%{service}/resources/actions/
install -p -D -m 644 ./mistral/resources/workflows/* %{buildroot}/%{pyver_sitelib}/%{service}/resources/workflows/
install -p -D -m 644 ./mistral/resources/actions/* %{buildroot}/%{pyver_sitelib}/%{service}/resources/actions/

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


%files -n python%{pyver}-%{service}
%{pyver_sitelib}/%{service}
%{pyver_sitelib}/%{service}-*.egg-info
%exclude %{pyver_sitelib}/mistral/tests

%files -n python%{pyver}-mistral-tests
%license LICENSE
%{pyver_sitelib}/mistral/tests

%changelog
