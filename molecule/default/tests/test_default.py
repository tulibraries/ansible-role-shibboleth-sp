import os

import testinfra.utils.ansible_runner
import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_shibboleth_package(host):
    shibboleth = host.package('shibboleth')
    assert shibboleth.is_installed


def test_shibd_process(host):
    shibd = host.service("shibd")
    assert shibd.is_running
    assert shibd.is_enabled


@pytest.mark.parametrize('f', [
    'idp-metadata.xml',
    'shibboleth2.xml',
    'attribute-map.xml',
    'shib-sp.crt',
    'shib-sp.key'
    ])
def test_idp_config_files(host, f):
    remote_file = host.file('/etc/shibboleth/' + f)
    assert remote_file.exists


def test_shibd_http_config(host):
    remote_file = host.file('/etc/httpd/conf.d/shib.conf')
    assert remote_file.exists
    assert remote_file.contains("/users/auth/shibboleth/callback")
