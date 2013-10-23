#!/bin/bash
#!/bin/bash

# Install saltstack
sudo apt-get install python-software-properties
sudo add-apt-repository ppa:saltstack/salt
sudo apt-get update


echo "start salt minion"
sudo apt-get install salt-minion
echo "done install minion"

echo "edit the minion -set up the master location"
cat << EOF > /etc/salt/minion
master: salt.leahmoler.com
#master: localhost
EOF
