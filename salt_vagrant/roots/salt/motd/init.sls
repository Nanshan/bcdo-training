/etc/motd.tail:
      file.managed:
        - contents: "Welcome to your Vagrant-built virtual machine!\n Thanks to  SaltStack.\n"
        - user: root
        - group: root
        - mode: 644
