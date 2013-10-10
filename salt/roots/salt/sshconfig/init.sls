/etc/ssh/ssh_config:
    file.managed::
       - source: salt://sshd_config
