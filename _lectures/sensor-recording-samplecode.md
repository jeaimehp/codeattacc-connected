---
layout: page
type: lecture
date: 2022-07-25T12:59:00+3:30
title: Sensor Recording Code
lecttag: 'Code'
hide_from_announcments: true
tldr: "Record (log) data from all the EnviroPlus Sensors."
#thumbnail: /static_files/presentations/lec.jpg
#links: 
#    - url: /static_files/presentations/lec.zip
#      name: notes
#    - url: /static_files/presentations/code.zip
#      name: codes
#    - url: https://google.com
#      name: slides
---
## Example Python code:

```
#!/usr/bin/python
import time
from bme280 import BME280
bme280 = BME280()

from ltr559 import LTR559
ltr559 =LTR559()

from enviroplus import gas

# Sets number of recordings
numberRecordings = 10

# Create a file
import os
import datetime

#creates a unique time stamp for the file with monthdaytime-hourminutesecond format
fileTime = datetime.datetime.now().strftime("%m%d%y-%H%M%S")
fileName= "recordings-{}.csv".format(fileTime)

#Print the path and name of file that will be created
print(os.getcwd() + "/" + fileName)
f = open(fileName, "w") #open a file named in the fileName variable to write

# create a header for the csv file
f.write("date,time,temperature,humidity,pressure,lux,oxidizing,reducing,nh3\n") #write out to file.txt

# Loop for recordings
for reading in range(numberRecordings):
    #creates a timestamp for when the data was recorded
    timestamp = datetime.datetime.now().strftime("%m/%d/%y,%H:%M:%S")
    temperature = bme280.get_temperature()*9/5+32
    
    #build the data record line to be saved
    textline = "{},{},{},{},{},{},{},{}\n".format(timestamp,\
                                         temperature,\
                                         bme280.get_humidity(),\
                                         bme280.get_pressure(),\
                                         ltr559.get_lux(),\
                                         gas.read_all().oxidising,\
                                         gas.read_all().reducing,
                                         gas.read_all().nh3)
    
    #Save the data to a file
    f.write(textline)
    print(textline)
    
    #delay before taking the next recording
    time.sleep(1)

# Close the file
f.close()
```
