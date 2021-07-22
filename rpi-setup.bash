#!/bin/bash
echo "Updating apt installer"
sudo apt -y update
echo " "
echo "Replacing vi-tiny with Vim"
sudo apt -y remove vi-tiny
sudo apt -y install vim
echo " "
echo "Setting Python3 as the default "
echo "Updating update-alternatives with python"
sudo update-alternatives --install /usr/bin/python python /usr/bin/python2.7 1
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.7 2
echo "Checking"
sudo update-alternatives --list python
echo "Setting Python 3 as the default"
sudo update-alternatives --set python /usr/bin/python3.7
echo "Verifying"
python --version
echo " "
echo "Installing Enviro+ Libraries"
echo "Downloading and installing the python libray"
curl -sSL https://get.pimoroni.com/enviroplus | bash
echo "Cloning the github repo"
git clone https://github.com/pimoroni/enviroplus-python.git
echo " "
echo "Installing Jupyter Notebook "
yes|pip3 install notebook
yes|pip3 install jupyter

echo "To start jupyter notebooks type \"jupyter notebook\" "

