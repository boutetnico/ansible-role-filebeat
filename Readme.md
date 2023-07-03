[![tests](https://github.com/boutetnico/ansible-role-filebeat/workflows/Test%20ansible%20role/badge.svg)](https://github.com/boutetnico/ansible-role-filebeat/actions?query=workflow%3A%22Test+ansible+role%22)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-boutetnico.filebeat-blue.svg)](https://galaxy.ansible.com/boutetnico/filebeat)

ansible-role-filebeat
=====================

This role installs and configures [Filebeat](https://www.elastic.co/guide/en/beats/filebeat/current/index.html).

Requirements
------------

Ansible 2.10 or newer.

Supported Platforms
-------------------

- [Debian - 11 (Bullseye)](https://wiki.debian.org/DebianBullseye)
- [Debian - 12 (Bookworm)](https://wiki.debian.org/DebianBookworm)
- [Ubuntu - 20.04 (Focal Fossa)](http://releases.ubuntu.com/20.04/)
- [Ubuntu - 22.04 (Jammy Jellyfish)](http://releases.ubuntu.com/22.04/)

Role Variables
--------------

| Variable                     | Required | Default                  | Choices   | Comments                                      |
|------------------------------|----------|--------------------------|-----------|-----------------------------------------------|
| filebeat_dependencies        | true     | `[apt-transport-https]`  | list      |                                               |
| filebeat_package             | true     | `filebeat`               | string    |                                               |
| filebeat_package_state       | true     | `present`                | string    |                                               |
| filebeat_use_oss             | true     | `false`                  | bool      | Whether to use Open Source version or not.    |
| filebeat_config              | true     |                          | dict      | Configuration object. See `defaults/main.yml`.|

Dependencies
------------

None

Example Playbook
----------------

    - hosts: all
      roles:
        - role: ansible-role-filebeat

Testing
-------

    molecule test

License
-------

MIT

Author Information
------------------

[@boutetnico](https://github.com/boutetnico)
