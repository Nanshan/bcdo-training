#!/bin/bash
echo "install stalstack ppa"
sudo apt-get install python-software-properties
sudo add-apt-repository ppa:saltstack/salt
echo "done ppa"

echo "updating"
sudo apt-get update
echo "done updating"

echo "install salt minion"
sudo apt-get install salt-minion
echo "done salt minion"
<<<<<<< HEAD
####
# make some chages to minion
# and set minion start on reboot
#
####
=======

echo "edit the minion -set up the master location"
cat << EOF > /etc/salt/minion

master: localhost

EOF
salt-minion
>>>>>>> 3cbc965372529a8d6affcc51d1e0ef66216748ab
