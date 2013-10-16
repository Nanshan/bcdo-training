/etc/salt/minion:
    file.managed:
       - source: salt://createAmi/minion.copy
