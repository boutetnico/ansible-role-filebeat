ansible-role-filebeat
=====================

This role installs and configures Filebeat.

Requirements
------------

Ansible 2.6 or newer.

Supported Platforms
-------------------

- [Debian - 9 (Stretch)](https://wiki.debian.org/DebianStretch)
- [Debian - 10 (Buster)](https://wiki.debian.org/DebianBuster)
- [Ubuntu - 16.04 (Xenial Xerus)](http://releases.ubuntu.com/16.04/)
- [Ubuntu - 18.04 (Bionic Beaver)](http://releases.ubuntu.com/18.04/)

Role Variables
--------------

| Variable                     | Required | Default                         | Choices   | Comments                                      |
|------------------------------|----------|---------------------------------|-----------|-----------------------------------------------|
| filebeat_dependencies        | true     | `[apt-transport-https]`         | list      |                                               |
| filebeat_package             | true     | `filebeat`                      | string    |                                               |
| filebeat_use_oss             | true     | `false`                         | bool      | Whether to use Open Source version or not.    |
| filebeat_config              | true     |                                 | dict      | Configuration object. See `defaults/main.yml`.|

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
