%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global service mistral

%global with_doc 1

Name:           openstack-mistral
Version:        4.0.0
Release:        1%{?dist}
Summary:        Task Orchestration and Scheduling service for OpenStack cloud
License:        ASL 2.0
URL:            https://launchpad.net/mistral
Source0:        https://tarballs.openstack.org/%{service}/%{service}-%{upstream_version}.tar.gz
# Systemd scripts
Source10:       openstack-mistral-api.service
Source11:       openstack-mistral-engine.service
Source12:       openstack-mistral-executor.service
Source13:       openstack-mistral-all.service

BuildArch:      noarch

BuildRequires:  git
BuildRequires:  openstack-macros
BuildRequires:  python-devel
BuildRequires:  python-oslo-config >= 2:2.3.0
BuildRequires:  python-setuptools
BuildRequires:  python-pbr >= 1.6
BuildRequires:  systemd

%description
System package - mistral
Python package - mistral

%package -n     python-%{name}

Summary:        Mistral Python libraries

Requires:       python-alembic >= 0.8.4
Requires:       python-babel >= 2.3.4
Requires:       python-croniter >= 0.3.4
Requires:       python-cachetools >= 1.1.0
Requires:       python-eventlet >= 0.17.4
Requires:       python-iso8601 >= 0.1.9
Requires:       python-jinja2
Requires:       python-jsonschema >= 2.0.0
Requires:       python-kombu
Requires:       python-mock
Requires:       python-networkx >= 1.10
Requires:       python-paramiko >= 1.13.0
Requires:       python-pbr >= 1.8
Requires:       python-pecan >= 1.0.0
Requires:       python-requests >= 2.10.0
Requires:       python-retrying >= 1.2.3
Requires:       python-six >= 1.9.0
Requires:       python-sqlalchemy >= 1.0.10
Requires:       python-tenacity >= 3.2.1
Requires:       python-wsme >= 0.8
Requires:       python-yaql >= 1.1.0
Requires:       PyYAML >= 3.10
# OpenStack dependencies
Requires:       python-oslo-concurrency >= 3.8.0
Requires:       python-oslo-config >= 2:3.14.0
Requires:       python-oslo-db >= 4.15.0
Requires:       python-oslo-i18n >= 2.1.0
Requires:       python-oslo-middleware >= 3.0.0
Requires:       python-oslo-messaging >= 5.14.0
Requires:       python-oslo-utils >= 3.18.0
Requires:       python-oslo-log >= 3.11.0
Requires:       python-oslo-serialization >= 1.10.0
Requires:       python-oslo-service >= 1.10.0
Requires:       python-oslo-policy >= 1.17.0
Requires:       python-osprofiler >= 1.4.0
Requires:       python-stevedore >= 1.17.1
Requires:       python-tooz >= 1.47.0
Requires:       python-aodhclient >= 0.7.0
Requires:       python-barbicanclient >= 4.0.0
Requires:       python-ceilometerclient >= 2.5.0
Requires:       python-cinderclient >= 1.6.0
Requires:       python-glanceclient >= 1:2.5.0
Requires:       python-gnocchiclient >= 2.7.0
Requires:       python-ironicclient >= 1.11.0
Requires:       python-ironic-inspector-client >= 1.5.0
Requires:       python-heatclient >= 1.6.1
Requires:       python-keystoneclient >= 1:3.8.0
Requires:       python-keystonemiddleware >= 4.12.0
Requires:       python-neutronclient >= 5.1.0
Requires:       python-novaclient >= 1:6.0.0
Requires:       python-swiftclient >= 3.2.0
Requires:       python-troveclient >= 2.2.0
Requires:       python-zaqarclient >= 1.0.0
Requires:       python-mistralclient >= 2.0.0
Requires:       python-designateclient >= 1.5.0
Requires:       python-magnumclient >= 2.0.0
Requires:       python-muranoclient >= 0.8.2

%description -n python-%{name}
Mistral is a workflow service.
Most business processes consist of multiple distinct interconnected steps that need to be executed in a particular order
in a distributed environment. One can describe such process as a set of tasks and task relations and upload such description
to Mistral so that it takes care of state management, correct execution order, parallelism, synchronization and high availability.
.
This package contains the Python libraries.

%package        common

Summary: Components common for OpenStack Mistral

Requires:       python-%{name} = %{version}-%{release}
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd

%description    common
Mistral is a workflow service.
Most business processes consist of multiple distinct interconnected steps that
need to be executed in a particular order in a distributed environment. One can
describe such process as a set of tasks and task relations and upload such
description to Mistral so that it takes care of state management, correct
execution order, parallelism, synchronization and high availability.
.
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

%package        all

Summary: OpenStack Mistral Executor daemon

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

BuildRequires:  python-sphinx
BuildRequires:  python-oslo-sphinx
BuildRequires:  python-sphinxcontrib-httpdomain
BuildRequires:  python-sphinxcontrib-pecanwsme
BuildRequires:  python2-wsme
BuildRequires:  python-croniter
BuildRequires:  python-eventlet
BuildRequires:  python-jsonschema
BuildRequires:  python-keystoneclient
BuildRequires:  python-keystonemiddleware
BuildRequires:  python-oslo-db
BuildRequires:  python-oslo-log
BuildRequires:  python-oslo-messaging
BuildRequires:  python-oslo-policy
BuildRequires:  python-osprofiler
BuildRequires:  python-pecan
BuildRequires:  python-tooz
BuildRequires:  python-yaql
BuildRequires:  python-networkx

%description    doc
OpenStack Mistral documentaion.
.
This package contains the documentation
%endif

%prep
%autosetup -n mistral-%{upstream_version} -S git

sed -i '1i #!/usr/bin/python' tools/sync_db.py

rm -rf {test-,}requirements.txt tools/{pip,test}-requires

%build
%{__python} setup.py build
oslo-config-generator --config-file tools/config/config-generator.mistral.conf \
                      --output-file etc/mistral.conf.sample

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

# Create fake egg-info for the tempest plugin
%py2_entrypoint %{service} %{service}

%if 0%{?with_doc}
export PYTHONPATH="$( pwd ):$PYTHONPATH"
pushd doc
sphinx-build -b html source build/html
popd
%endif

mkdir -p %{buildroot}/etc/mistral/
mkdir -p %{buildroot}/var/log/mistral
mkdir -p %{buildroot}/var/run/mistral

install -p -D -m 644 %SOURCE10 %{buildroot}%{_unitdir}/openstack-mistral-api.service
install -p -D -m 644 %SOURCE11 %{buildroot}%{_unitdir}/openstack-mistral-engine.service
install -p -D -m 644 %SOURCE12 %{buildroot}%{_unitdir}/openstack-mistral-executor.service
install -p -D -m 644 %SOURCE13 %{buildroot}%{_unitdir}/openstack-mistral-all.service

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

# Install tempest tests files
# TODO(apevec) remove when setup.cfg fix is merged to stable/mitaka
# http://review.openstack.org/#/q/I5c34f3516c4f171ab4f34647f1cc4a08883feacf
if [ ! -d %{buildroot}%{python2_sitelib}/mistral_tempest_tests ]
then
   cp -r mistral_tempest_tests %{buildroot}%{python2_sitelib}/mistral_tempest_tests
fi

%pre common
USERNAME=mistral
GROUPNAME=$USERNAME
HOMEDIR=/home/$USERNAME
getent group $GROUPNAME >/dev/null || groupadd -r $GROUPNAME
getent passwd $USERNAME >/dev/null ||
    useradd -r -g $GROUPNAME -G $GROUPNAME -d $HOMEDIR -s /sbin/nologin \
            -c "Mistral Daemons" $USERNAME
exit 0


%clean
rm -rf %{buildroot}

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
%{_bindir}/mistral-*
%dir %attr(755, mistral, mistral) /var/run/mistral
%dir %attr(755, mistral, mistral) /var/log/mistral


%if 0%{?with_doc}
%files doc
%doc doc/build/html
%endif

%files engine
%config(noreplace) %attr(-, root, root) %{_unitdir}/openstack-mistral-engine.service

%files executor
%config(noreplace) %attr(-, root, root) %{_unitdir}/openstack-mistral-executor.service

%files all
%config(noreplace) %attr(-, root, root) %{_unitdir}/openstack-mistral-all.service


%files -n python-%{name}
%{python2_sitelib}/%{service}
%{python2_sitelib}/%{service}-*.egg-info
%exclude %{python2_sitelib}/mistral/tests
%exclude %{python2_sitelib}/mistral_tempest_tests

%files -n python-mistral-tests
%license LICENSE
%{python2_sitelib}/mistral/tests
%{python2_sitelib}/mistral_tempest_tests
%{python2_sitelib}/%{service}_tests.egg-info

%changelog
* Wed Feb 22 2017 Alfredo Moralejo <amoralej@redhat.com> 4.0.0-1
- Update to 4.0.0

* Mon Feb 20 2017 Alfredo Moralejo <amoralej@redhat.com> 4.0.0-0.2.0rc2
- Update to 4.0.0.0rc2

* Fri Feb 10 2017 Alfredo Moralejo <amoralej@redhat.com> 4.0.0-0.1.0rc1
- Update to 4.0.0.0rc1

