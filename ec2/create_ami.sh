#!/bin/bash
echo "install stalstack ppa"
sudo apt-get install python-software-properties
sudo add-apt-repository ppa:saltstack/salt
echo "done ppa"

echo "updating"
apt-get update
echo "done updating"

echo "install salt minion"
sudo apt-get install salt-minion
echo "done salt minion"