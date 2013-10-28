#!/bin/bash
cat << EOF > /etc/salt/grains
roles:
 - dbserver
EOF
