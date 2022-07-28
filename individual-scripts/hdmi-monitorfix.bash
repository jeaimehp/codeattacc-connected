#!/bin/bash

echo "Adding lines to /boot/config.txt to resolve dual monitor switch issue"
sudo echo " " >> /boot/config.txt 
sudo echo "hdmi_edid_file:1=1" >> /boot/config.txt
sudo echo "hdmi_edid_filename:1=edid.dat" >> /boot/config.txt 
sudo echo "hdmi_force_hotplug:1=1" >> /boot/config.txt 

