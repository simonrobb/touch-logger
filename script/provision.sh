#!/bin/sh

block_comment()
{
  COMMENT=$1
  printf "\n\n"
  printf "###########################\n"
  printf "#\n"
  printf "# $COMMENT\n"
  printf "#\n"
  printf "###########################\n"
  printf "\n"
}

block_comment "Update pi packages"
sudo apt-get -y update
sudo apt-get -y upgrade

# Add the influx repos
block_comment "Install influxdb"
wget https://dl.influxdata.com/influxdb/releases/influxdb_1.2.4_armhf.deb
sudo dpkg -i influxdb_1.2.4_armhf.deb

# Install chronograf
block_comment "Install chronograf"
wget https://dl.influxdata.com/chronograf/releases/chronograf_1.3.3.4_armhf.deb
sudo dpkg -i chronograf_1.3.3.4_armhf.deb

# Install pip and dependencies
block_comment "Install pip and python dependencies"
sudo apt-get install -y python-pip
sudo pip install influxdb
sudo pip install --upgrade influxdb