#! /bin/bash
echo "install master"
sudo apt-get install python-software-properties
sudo add-apt-repository ppa:saltstack/salt
sudo apt-get install salt-master -y
sudo apt-get upgrade -y
echo "Done install master"

echo "install pip and libcloud"
sudo apt-get install python-pip
sudo pip install apache-libcloud
