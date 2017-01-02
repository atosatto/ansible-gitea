Ansible Role: Gitea
===================

[![Build Status](https://travis-ci.org/atosatto/ansible-gitea.svg?branch=master)](https://travis-ci.org/atosatto/ansible-gitea)

Install and configure the [Gitea](https://gitea.io/) self-hosted Git service
on RHEL/CentOS and Debian/Ubuntu.

Requirements
------------

None.

Role Variables
--------------

Available variables are listed below, along with default values (see `defaults/main.yml`):

    gitea_version: 1.0.0

The Gitea version that has to be installed.

    gitea_bin: /usr/local/bin/minio

Installation path of the Gitea binary.

    # Path to the file containing the ENV configuration variables for gitea
    gitea_envfile: /etc/default/gitea

Path to the file containing the Gitea configuration ENV variables.

    gitea_working_dir: /home/gitea

Parent directory of the Gitea log and repositories folders.

    gitea_user: git
    gitea_group: git

Name and group of the user running Gitea.
**NB**: This role automatically creates the gitea user and/or group if these does not exist in the system.

------------

None.

Example Playbook
----------------

    $ cat playbook.yml
    - name: "Install gitea"
      hosts: all
      roles:
         - { role: atosatto.gitea }

License
-------

MIT

Author Information
------------------

Andrea Tosatto ([@\_hilbert\_](https://twitter.com/_hilbert_))
