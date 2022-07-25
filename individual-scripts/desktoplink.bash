#!/bin/bash
echo "Creating ~/Desktop symlink (shortcut)"

ln -s ~/codeattacc-connected ~/Desktop/

echo "Creating Jupyter Notebook Launcher"
cp ~/codeattacc-connected/individual-scripts/Jupyter-Notebook.bash ~/Desktop/

echo "Creating Sensor Recordings Script"
cp ~/codeattacc-connected/sensor-record.py ~/Desktop/
