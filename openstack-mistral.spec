%global milestone .0rc1
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
Version:        7.0.0
Release:        0.1%{?milestone}%{?dist}
Summary:        Task Orchestration and Scheduling service for OpenStack cloud
License:        ASL 2.0
URL:            https://launchpad.net/mistral
Source0:        https://tarballs.openstack.org/%{service}/%{service}-%{upstream_version}.tar.gz
#
# patches_base=7.0.0.0rc1
#

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
BuildRequires:  python2-devel
BuildRequires:  python2-oslo-config >= 2:5.2.0
BuildRequires:  python2-pbr >= 2.0.0
BuildRequires:  systemd

%description
%{summary}


%package -n     python-%{service}
Summary:        Mistral Python libraries
Provides:       python-%{name} = %{version}-%{release}
Obsoletes:      python-%{name} < 5.0.0-1

Requires:       python2-alembic >= 0.9.6
Requires:       python2-babel >= 2.3.4
Requires:       python2-croniter >= 0.3.4
Requires:       python-cachetools >= 2.0.0
Requires:       python2-eventlet >= 0.20.0
Requires:       python2-iso8601 >= 0.1.9
Requires:       python2-jinja2
Requires:       python2-jsonschema >= 2.6.0
Requires:       python2-kombu
Requires:       python2-mock
Requires:       python-networkx >= 1.10
Requires:       python2-paramiko >= 2.0
Requires:       python2-pbr >= 2.0.0
Requires:       python2-pecan >= 1.2.1
Requires:       python2-requests >= 2.14.2
Requires:       python-retrying >= 1.2.3
Requires:       python2-six >= 1.10.0
Requires:       python2-sqlalchemy >= 1.2.5
Requires:       python2-tenacity >= 4.4.0
Requires:       python2-wsme >= 0.8
Requires:       python2-yaql >= 1.1.3
Requires:       PyYAML >= 3.10
# OpenStack dependencies
Requires:       python2-oslo-concurrency >= 3.26.0
Requires:       python2-oslo-config >= 2:5.2.0
Requires:       python2-oslo-context >= 2.21.0
Requires:       python2-oslo-db >= 4.27.0
Requires:       python2-oslo-i18n >= 3.15.3
Requires:       python2-oslo-middleware >= 3.31.0
Requires:       python2-oslo-messaging >= 5.29.0
Requires:       python2-oslo-utils >= 3.33.0
Requires:       python2-oslo-log >= 3.36.0
Requires:       python2-oslo-serialization >= 2.18.0
Requires:       python2-oslo-service >= 1.24.0
Requires:       python2-oslo-policy >= 1.30.0
Requires:       python2-osprofiler >= 1.4.0
Requires:       python2-stevedore >= 1.20.0
Requires:       python-tooz >= 1.58.0
Requires:       python2-aodhclient >= 0.9.0
Requires:       python2-barbicanclient >= 4.5.2
Requires:       python2-cinderclient >= 3.3.0
Requires:       python2-glanceclient >= 1:2.8.0
Requires:       python2-gnocchiclient >= 3.3.1
Requires:       python2-ironicclient >= 2.3.0
Requires:       python-ironic-inspector-client >= 1.5.0
Requires:       python2-heatclient >= 1.10.0
Requires:       python2-keystoneclient >= 1:3.8.0
Requires:       python2-keystonemiddleware >= 4.17.0
Requires:       python2-neutronclient >= 6.7.0
Requires:       python2-novaclient >= 1:9.1.0
Requires:       python2-manilaclient >= 1.23.0
Requires:       python2-swiftclient >= 3.2.0
Requires:       python2-zaqarclient >= 1.0.0
Requires:       python2-mistralclient >= 3.1.0
Requires:       python2-mistral-lib >= 0.4.0
Requires:       python-jwt >= 1.0.1
Requires:       python2-designateclient >= 2.7.0
Requires:       python2-magnumclient >= 2.1.0
%if 0%{rhosp} == 0
Requires:       python2-glareclient >= 0.3.0
Requires:       python2-muranoclient >= 0.8.2
Requires:       python2-senlinclient >= 1.1.0
Requires:       python2-tackerclient >= 0.8.0
Requires:       python2-vitrageclient >= 2.0.0
%endif
Requires:       python2-troveclient >= 2.2.0

%description -n python-%{service}
%{common_desc}

This package contains the Python libraries.

%package        common
Summary: Components common for OpenStack Mistral

Requires:       python-%{service} = %{version}-%{release}
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

%package -n python-mistral-tests
Summary:        Mistral tests
Requires:       %{name}-common = %{version}-%{release}

%description -n python-mistral-tests
This package contains the mistral test files.


%if 0%{?with_doc}
%package        doc
Summary:        Documentation for OpenStack Workflow Service

BuildRequires:  python2-sphinx
BuildRequires:  python2-openstackdocstheme
BuildRequires:  python-sphinxcontrib-httpdomain
BuildRequires:  python2-sphinxcontrib-pecanwsme
BuildRequires:  python2-wsme
BuildRequires:  python2-croniter
BuildRequires:  python2-eventlet
BuildRequires:  python2-jsonschema
BuildRequires:  python2-keystoneclient
BuildRequires:  python2-keystonemiddleware
BuildRequires:  python2-mistral-lib
BuildRequires:  python2-oslo-db
BuildRequires:  python2-oslo-log
BuildRequires:  python2-oslo-messaging
BuildRequires:  python2-oslo-policy
BuildRequires:  python2-osprofiler
BuildRequires:  python2-pecan
BuildRequires:  python-tooz
BuildRequires:  python2-yaql
BuildRequires:  python-networkx
BuildRequires:  openstack-macros

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
%{__python2} setup.py build
oslo-config-generator --config-file tools/config/config-generator.mistral.conf \
                      --output-file etc/mistral.conf.sample

%install
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}

%if 0%{?with_doc}
export PYTHONPATH=.
sphinx-build -W -b html doc/source doc/build/html
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

install -p -D -m 644 ./mistral/actions/openstack/mapping.json %{buildroot}%{python2_sitelib}/%{service}/actions/openstack/mapping.json
install -p -D -m 644 ./mistral/db/sqlalchemy/migration/alembic.ini %{buildroot}%{python2_sitelib}/%{service}/db/sqlalchemy/migration/alembic.ini
mkdir -p %{buildroot}/%{python2_sitelib}/%{service}/resources/workflows/
mkdir -p %{buildroot}/%{python2_sitelib}/%{service}/resources/actions/
install -p -D -m 644 ./mistral/resources/workflows/* %{buildroot}/%{python2_sitelib}/%{service}/resources/workflows/
install -p -D -m 644 ./mistral/resources/actions/* %{buildroot}/%{python2_sitelib}/%{service}/resources/actions/

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


%files -n python-%{service}
%{python2_sitelib}/%{service}
%{python2_sitelib}/%{service}-*.egg-info
%exclude %{python2_sitelib}/mistral/tests

%files -n python-mistral-tests
%license LICENSE
%{python2_sitelib}/mistral/tests

%changelog
* Tue Aug 21 2018 RDO <dev@lists.rdoproject.org> 7.0.0-0.1.0rc1
- Update to 7.0.0.0rc1

