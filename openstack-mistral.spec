# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pydefault 3
# oslo-config does not comply with Fedora for python versioned binaries. Until fixed
# in https://review.rdoproject.org/r/#/c/15370 we need to use this hack
%global pydefault_oslo_config_gen python3-oslo-config-generate
%else
%global pydefault 2
%global pydefault_oslo_config_gen oslo-config-generate
%endif

%global pydefault_bin python%{pydefault}
%global pydefault_sitelib %python%{pydefault}_sitelib
%global pydefault_install %py%{pydefault}_install
%global pydefault_build %py%{pydefault}_build
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

BuildArch:      noarch

BuildRequires:  git
BuildRequires:  openstack-macros
BuildRequires:  python%{pydefault}-devel
BuildRequires:  python%{pydefault}-oslo-config >= 2:5.1.0
BuildRequires:  python%{pydefault}-pbr >= 2.0.0
BuildRequires:  systemd

%description
%{summary}


%package -n     python%{pydefault}-%{service}
Summary:        Mistral Python libraries
%{?python_provide:%python_provide python%{pydefault}-%{service}}
Provides:       python-%{name} = %{version}-%{release}
Obsoletes:      python-%{name} < 5.0.0-1

Requires:       python%{pydefault}-alembic >= 0.8.10
Requires:       python%{pydefault}-babel >= 2.3.4
Requires:       python%{pydefault}-croniter >= 0.3.4
Requires:       python%{pydefault}-cachetools >= 2.0.0
Requires:       python%{pydefault}-eventlet >= 0.18.2
Requires:       python%{pydefault}-iso8601 >= 0.1.9
Requires:       python%{pydefault}-jinja2
Requires:       python%{pydefault}-jsonschema >= 2.6.0
Requires:       python%{pydefault}-kombu
Requires:       python%{pydefault}-mock
Requires:       python%{pydefault}-paramiko >= 2.0
Requires:       python%{pydefault}-pbr >= 2.0.0
Requires:       python%{pydefault}-pecan >= 1.0.0
Requires:       python%{pydefault}-requests >= 2.14.2
Requires:       python%{pydefault}-six >= 1.10.0
Requires:       python%{pydefault}-sqlalchemy >= 1.0.10
Requires:       python%{pydefault}-tenacity >= 3.2.1
Requires:       python%{pydefault}-wsme >= 0.8
Requires:       python%{pydefault}-yaql >= 1.1.3
# OpenStack dependencies
Requires:       python%{pydefault}-oslo-concurrency >= 3.25.0
Requires:       python%{pydefault}-oslo-config >= 2:5.1.0
Requires:       python%{pydefault}-oslo-context >= 2.19.2
Requires:       python%{pydefault}-oslo-db >= 4.27.0
Requires:       python%{pydefault}-oslo-i18n >= 3.15.3
Requires:       python%{pydefault}-oslo-middleware >= 3.31.0
Requires:       python%{pydefault}-oslo-messaging >= 5.29.0
Requires:       python%{pydefault}-oslo-utils >= 3.33.0
Requires:       python%{pydefault}-oslo-log >= 3.36.0
Requires:       python%{pydefault}-oslo-serialization >= 2.18.0
Requires:       python%{pydefault}-oslo-service >= 1.24.0
Requires:       python%{pydefault}-oslo-policy >= 1.30.0
Requires:       python%{pydefault}-osprofiler >= 1.4.0
Requires:       python%{pydefault}-stevedore >= 1.20.0
Requires:       python%{pydefault}-tooz >= 1.58.0
Requires:       python%{pydefault}-aodhclient >= 0.9.0
Requires:       python%{pydefault}-barbicanclient >= 4.0.0
Requires:       python%{pydefault}-cinderclient >= 3.3.0
Requires:       python%{pydefault}-glanceclient >= 1:2.8.0
Requires:       python%{pydefault}-gnocchiclient >= 3.3.1
# TODO (amoraje) move ironicclient back to 2.2.0 after next promotion
#Requires:       python2-ironicclient >= 2.2.0
Requires:       python%{pydefault}-ironicclient >= 2.1.0
Requires:       python%{pydefault}-ironic-inspector-client >= 1.5.0
Requires:       python%{pydefault}-heatclient >= 1.10.0
Requires:       python%{pydefault}-keystoneclient >= 1:3.8.0
Requires:       python%{pydefault}-keystonemiddleware >= 4.17.0
Requires:       python%{pydefault}-neutronclient >= 6.3.0
Requires:       python%{pydefault}-novaclient >= 1:9.1.0
Requires:       python%{pydefault}-swiftclient >= 3.2.0
Requires:       python%{pydefault}-zaqarclient >= 1.0.0
Requires:       python%{pydefault}-mistralclient >= 3.1.0
Requires:       python%{pydefault}-mistral-lib >= 0.3.0
Requires:       python%{pydefault}-designateclient >= 2.7.0
Requires:       python%{pydefault}-magnumclient >= 2.1.0
%if 0%{rhosp} == 0
Requires:       python%{pydefault}-glareclient >= 0.3.0
Requires:       python%{pydefault}-muranoclient >= 0.8.2
Requires:       python%{pydefault}-senlinclient >= 1.1.0
Requires:       python%{pydefault}-tackerclient >= 0.8.0
%endif
Requires:       python%{pydefault}-troveclient >= 2.2.0

# Handle python2 exceptions
%if %{pydefault} == 2
Requires:       python-jwt >= 1.0.1
Requires:       python-retrying >= 1.2.3
Requires:       python-networkx >= 1.10
Requires:       PyYAML >= 3.10
%else
Requires:       python%{pydefault}-jwt >= 1.0.1
Requires:       python%{pydefault}-retrying >= 1.2.3
Requires:       python%{pydefault}-networkx >= 1.10
Requires:       python%{pydefault}-PyYAML >= 3.10
%endif

%description -n python%{pydefault}-%{service}
%{common_desc}

This package contains the Python libraries.

%package        common
Summary: Components common for OpenStack Mistral

Requires:       python%{pydefault}-%{service} = %{version}-%{release}
%{?systemd_requires}

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

%package        all
Summary: OpenStack Mistral All-in-one daemon

Requires:       %{name}-common = %{version}-%{release}

%description    all
OpenStack Mistral All service.
.
This package contains the mistral api, engine, and executor service as
an all-in-one process.

%package -n python%{pydefault}-mistral-tests
Summary:        Mistral tests
%{?python_provide:%python_provide python%{pydefault}-%{service}}
Requires:       %{name}-common = %{version}-%{release}

%description -n python%{pydefault}-mistral-tests
This package contains the mistral test files.


%if 0%{?with_doc}
%package        doc
Summary:        Documentation for OpenStack Workflow Service

BuildRequires:  python%{pydefault}-sphinx
BuildRequires:  python%{pydefault}-openstackdocstheme
BuildRequires:  python%{pydefault}-sphinxcontrib-pecanwsme
BuildRequires:  python%{pydefault}-wsme
BuildRequires:  python%{pydefault}-croniter
BuildRequires:  python%{pydefault}-eventlet
BuildRequires:  python%{pydefault}-jsonschema
BuildRequires:  python%{pydefault}-keystoneclient
BuildRequires:  python%{pydefault}-keystonemiddleware
BuildRequires:  python%{pydefault}-mistral-lib
BuildRequires:  python%{pydefault}-oslo-db
BuildRequires:  python%{pydefault}-oslo-log
BuildRequires:  python%{pydefault}-oslo-messaging
BuildRequires:  python%{pydefault}-oslo-policy
BuildRequires:  python%{pydefault}-osprofiler
BuildRequires:  python%{pydefault}-pecan
BuildRequires:  python%{pydefault}-tooz
BuildRequires:  python%{pydefault}-yaql
BuildRequires:  openstack-macros

# Handle python2 exceptions
%if %{pydefault} == 2
BuildRequires:  python-sphinxcontrib-httpdomain
BuildRequires:  python-networkx
%else
BuildRequires:  python%{pydefault}-sphinxcontrib-httpdomain
BuildRequires:  python%{pydefault}-networkx
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
%{pydefault_build}
%{pydefault_oslo_config_gen} --config-file tools/config/config-generator.mistral.conf \
                      --output-file etc/mistral.conf.sample

%install
%{pydefault_install}


%if 0%{?with_doc}
export PYTHONPATH=.
sphinx-build-%{pydefault} -W -b html doc/source doc/build/html
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

install -p -D -m 644 ./mistral/actions/openstack/mapping.json %{buildroot}%{pydefault_sitelib}/%{service}/actions/openstack/mapping.json
install -p -D -m 644 ./mistral/db/sqlalchemy/migration/alembic.ini %{buildroot}%{pydefault_sitelib}/%{service}/db/sqlalchemy/migration/alembic.ini
mkdir -p %{buildroot}/%{pydefault_sitelib}/%{service}/resources/workflows/
mkdir -p %{buildroot}/%{pydefault_sitelib}/%{service}/resources/actions/
install -p -D -m 644 ./mistral/resources/workflows/* %{buildroot}/%{pydefault_sitelib}/%{service}/resources/workflows/
install -p -D -m 644 ./mistral/resources/actions/* %{buildroot}/%{pydefault_sitelib}/%{service}/resources/actions/

%pre common
USERNAME=mistral
GROUPNAME=$USERNAME
HOMEDIR=/home/$USERNAME
getent group $GROUPNAME >/dev/null || groupadd -r $GROUPNAME
getent passwd $USERNAME >/dev/null ||
    useradd -r -g $GROUPNAME -G $GROUPNAME -d $HOMEDIR -s /sbin/nologin \
            -c "Mistral Daemons" $USERNAME
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

%files all
%config(noreplace) %attr(-, root, root) %{_unitdir}/openstack-mistral-all.service


%files -n python%{pydefault}-%{service}
%{pydefault_sitelib}/%{service}
%{pydefault_sitelib}/%{service}-*.egg-info
%exclude %{pydefault_sitelib}/mistral/tests

%files -n python%{pydefault}-mistral-tests
%license LICENSE
%{pydefault_sitelib}/mistral/tests

%changelog
