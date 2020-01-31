import pytest

import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('name', [
  ('filebeat'),
])
def test_packages_are_installed(host, name):
    package = host.package(name)
    assert package.is_installed


@pytest.mark.parametrize('username,groupname,path', [
  ('root', 'root', '/etc/filebeat/filebeat.yml'),
])
def test_curator_config_file(host, username, groupname, path):
    curator_config = host.file(path)
    assert curator_config.exists
    assert curator_config.is_file
    assert curator_config.user == username
    assert curator_config.group == groupname
