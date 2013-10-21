#!/bin/bash
#!/bin/bash

# Install saltstack
add-apt-repository ppa:saltstack/salt -y
apt-get update -y
apt-get install salt-minion -y

echo "edit the minion -set up the master location"
cat << EOF > /etc/salt/minion
master: salt.leahmoler.com
file_client: remote
EOF

echo "start salt minion"
salt-minion -d
