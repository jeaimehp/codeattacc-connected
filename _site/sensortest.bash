#!/bin/bash
CYAN='\033[0;36m'
PURPLE='\033[0;35m'
NC='\033[0m' # No Color
printf "${PURPLE}Running Pimoroni Enviro+ Sensor Test....\n"
echo " "
printf "${CYAN}Press Ctrl + c to stop the test\n"
python3 ~/codeattacc-connected/enviroplus-python/examples/weather-and-light.py
