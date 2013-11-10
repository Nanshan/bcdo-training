base:
#   '*':
#     - motd
  'roles:webserver':
     - match: grain
     - apache
     - apache.vhosts.standard
     - php
     - mysql.server
     - mysql.client
#     - wordpress
     - zabbix.server
     - zabbix.agent
     - rabbitmq
     - mongodb
     - haproxy

