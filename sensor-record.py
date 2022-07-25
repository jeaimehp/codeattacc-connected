#!/usr/bin/python
####################
# Needed Libraries #
####################

import time
from bme280 import BME280
bme280 = BME280()

from ltr559 import LTR559
ltr559 =LTR559()

from enviroplus import gas

from pms5003 import PMS5003, ReadTimeoutError

from enviroplus.noise import Noise
import sounddevice
import numpy

import ST7735
from PIL import Image, ImageDraw, ImageFont
from fonts.ttf import RobotoMedium as UserFont

import os
import datetime

from enviroplus.noise import Noise
import sounddevice
import numpy
noise = Noise()

from pms5003 import PMS5003, ReadTimeoutError
import time

pms5003 = PMS5003()

################################
#       PROGRAM SETTINGS       #
################################
# Sets number of recordings
numberRecordings = 30
# Seconds between recordings
timeBetweenRecordings = 1
# Data file location
path = os.path.expanduser('~/Desktop/data')





#Setup Enviro+ Display
disp = ST7735.ST7735(
    port=0,
    cs=1,
    dc=9,
    backlight=12,
    rotation=270,
    spi_speed_hz=10000000
)
disp.begin()

WIDTH = disp.width
HEIGHT = disp.height

img = Image.new('RGB', (WIDTH, HEIGHT), color=(0, 0, 0))
draw = ImageDraw.Draw(img)

# Position on LCD
x = 10
y = 10

# Font to use, size and color
font_size = 12
font = ImageFont.truetype(UserFont, font_size)
text_colour = (255, 255, 255) #RGB colors



#The background of what you want to display
back_colour = (0, 0, 0) #RGB colors
draw.rectangle((0, 0, 160, 80), back_colour)

def clearLCD():
    disp.reset()
    back_colour = (0, 0, 0) #RGB colors
    draw.rectangle((0, 0, 160, 80), back_colour)
    disp.display(img)

# Easier method to display
def updateLCD (line, fsize, message):
  font = ImageFont.truetype(UserFont, fsize)  
  #Setup text
  draw.text((x, line), message, fill=text_colour, font=font)
  #Show on the LCD
  disp.display(img)
  
def statusLCD (numrecordings):
  if numrecordings == 1:
      updateLCD(42,12, "Recording: {} of {}".format(numrecordings,numberRecordings))
  elif numrecordings%2 == 0:
      clearLCD()
      updateLCD(10,12,"Filename =")
      updateLCD(20,20,fileName)
      updateLCD(42,12, "Recording: {} of {}".format(numrecordings,numberRecordings))
    


# Ouput to terminal that the program is starting
print("Begining to record sensor readings........")
#What you want to display on Enviro+ LCD
updateLCD(10,12, "Preparing to record...")



# Create a file



# Check whether the specified path exists or not
isExist = os.path.exists(path)
print(path + "Exists= " + str(isExist))
if not isExist:
  # Create a new directory because it does not exist 
  os.makedirs(path)
  print("The new directory is created!")

# Count number of files to account for no date when no wifi
listfiles = os.listdir(path)
number_files = len(listfiles)
print ("Current number of recordings = ",number_files)
updateLCD(23,12,"# of Recordings = " + str(number_files))



#creates a unique time stamp for the file with monthdaytime-hourminutesecond format
fileTime = datetime.datetime.now().strftime("%m%d%y-%H%M%S")
fileName= "recording_{}-{}.csv".format(str(number_files+1),fileTime)
time.sleep(2)
clearLCD()
updateLCD(10,12,"Filename =")
#updateLCD(49,17,"recording_{}".format(str(number_files+1)))
updateLCD(20,20,fileName)


#Print the path and name of file that will be created
fullFileName = path + "/" + fileName
print(fullFileName)
f = open(fullFileName, "w") #open a file named in the fileName variable to write

# create a header for the csv file
f.write("recording,date,time,temperature,humidity,pressure,lux,oxidizing,reducing,nh3,noise_amp,pm1_0,pm2_5,pm_10\n") #write out to file.txt
f.close()

loopCount = 1

# Loop for recordings
for reading in range(numberRecordings):
    f = open(fullFileName, "a") #open a file named in the fileName variable to write
    #creates a timestamp for when the data was recorded
    timestamp = datetime.datetime.now().strftime("%m/%d/%y,%H:%M:%S")
    temperature = bme280.get_temperature()*9/5+32
    low, mid, high, amp = noise.get_noise_profile()
    low *= 128
    mid *= 128
    high *= 128
    amp *= 64
    pms_data = pms5003.read()
    
    
    #build the data record line to be saved
    textline = "{},{},{},{},{},{},{},{},{},{},{},{},{}\n".format("recording_" + str(number_files+1),\
                                        timestamp,\
                                         temperature,\
                                         bme280.get_humidity(),\
                                         bme280.get_pressure(),\
                                         ltr559.get_lux(),\
                                         gas.read_all().oxidising,\
                                         gas.read_all().reducing,\
                                         gas.read_all().nh3,\
                                                     amp,\
                                                     float(pms_data.pm_ug_per_m3(1.0)),\
                                                     float(pms_data.pm_ug_per_m3(2.5)),\
                                                     float(pms_data.pm_ug_per_m3(10)),)
    
    #Save the data to a file
    f.write(textline)
    print("Recording: {} of {}".format(loopCount,numberRecordings))
    statusLCD(loopCount)
    print(textline)
    loopCount += 1
    
    # Close the file
    f.close()
    
    #delay before taking the next recording
    time.sleep(timeBetweenRecordings)
    

print("Done!")
updateLCD(55,16, "Done!")


