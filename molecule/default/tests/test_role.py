import pytest


@pytest.mark.parametrize(
    "name",
    [
        ("apt-transport-https"),
        ("gnupg"),
    ],
)
def test_dependencies_are_installed(host, name):
    package = host.package(name)
    assert package.is_installed


@pytest.mark.parametrize(
    "name",
    [
        ("filebeat"),
    ],
)
def test_filebeat_package_is_installed(host, name):
    package = host.package(name)
    assert package.is_installed


def test_filebeat_service_is_running(host):
    service = host.service("filebeat")
    assert service.is_running
    assert service.is_enabled


@pytest.mark.parametrize(
    "path,user,group,mode",
    [
        ("/etc/filebeat/filebeat.yml", "root", "root", 0o600),
    ],
)
def test_filebeat_config_file_exists(host, path, user, group, mode):
    config = host.file(path)
    assert config.exists
    assert config.is_file
    assert config.user == user
    assert config.group == group
    assert config.mode == mode


def test_filebeat_command_works(host):
    cmd = host.run("filebeat version")
    assert cmd.rc == 0
