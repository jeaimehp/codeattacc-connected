#!/bin/bash

echo "Downloading and installing the python libray"
curl -sSL https://get.pimoroni.com/enviroplus | bash
echo "Cloning the github repo"
git clone https://github.com/pimoroni/enviroplus-python.git
