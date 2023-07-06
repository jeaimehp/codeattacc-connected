#!/bin/bash
echo "Disabling fake-hwclock services"
sudo apt-get -y remove fake-hwclock
sudo update-rc.d -f fake-hw-clock remove
sudo systemctl disable fake-hwclock
echo "Copying new /lib/udev/hwclock-set" 
sudo cp hwclock-set /lib/udev/hwclock-set
echo "Reading from RTC"
sudo hwclock -r
echo "Writting New RTC Time"
sudo hwclock -w
echo "Checking RTC Time"
sudo hwclock -r
