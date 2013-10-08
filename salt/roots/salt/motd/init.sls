/etc/motd.tail:
  file.managed:
   - contents: "Welcome to your Vagrant-built virtual machine!"
   - user: root
   - group: root
   - mode: 644


