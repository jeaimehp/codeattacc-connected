#!/bin/bash
echo "Setting up the PCF8523 Reat-time clock on i2c 0x68"

sudo echo "" >> /boot/config.txt
sudo echo "# Added for RTC support of Adafruit PCF8523" >> /boot/config.txt
sudo echo "dtoverlay=i2c-rtc,pcf8523" >> /boot/config.txt


