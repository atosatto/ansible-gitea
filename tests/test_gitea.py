import yaml
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


@pytest.fixture()
def AnsibleDefaults(Ansible):
    with open("./defaults/main.yml", 'r') as stream:
        return yaml.load(stream)


def test_gitea_installed(File, AnsibleDefaults):

    f = File(AnsibleDefaults['gitea_bin'])
    assert f.exists
    assert f.user == AnsibleDefaults['gitea_user']
    assert f.group == AnsibleDefaults['gitea_group']
    assert oct(f.mode) == '0755'


def test_gitea_service(Service, Command, SystemInfo):

    # Testinfra fails on Ubuntu trying to use systemd to get
    # the status of Gitea
    dist = SystemInfo.distribution
    if dist == 'debian' or dist == 'ubuntu':
        Command("/etc/init.d/gitea status").rc == 0
    else:
        s = Service('gitea')
        assert s.is_running
        assert s.is_enabled
