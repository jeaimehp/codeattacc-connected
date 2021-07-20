#!/bin/bash
echo "Updating apt installer"
sudo apt -y update
echo "Replacing vi-tiny with Vim"
sudo apt -y remove vi-tiny
sudo apt -y install vim
