#! /bin/bash
echo "install master"
apt-get upgrade -y
apt-get install salt-master -y
apt-get upgrade -y
echo "Done install master"

echo "install pip and libcloud"
sudo apt-get install python-pip
sudo pip install apache-libcloud
