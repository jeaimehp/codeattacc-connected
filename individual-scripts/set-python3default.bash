#!/bin/bash
echo "Updating update-alternatives with python"
sudo update-alternatives --install /usr/bin/python python /usr/bin/python2.7 1
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.7 2
echo "Checking"
sudo update-alternatives --list python
echo "Setting Python 3 as the default"
sudo update-alternatives --set python /usr/bin/python3.7
echo "Verifying"
python --version
