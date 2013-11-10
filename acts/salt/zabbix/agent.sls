zabbix-agent:
    pkg:
      - installed
    service:
      -  running
      -  require:
           - pkg: zabbix-agent
