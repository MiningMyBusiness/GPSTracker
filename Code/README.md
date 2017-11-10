# Code overview
This folder contains all relevant code to 
1. Collect data
2. Parse and clean data
3. Visualize data

## Descriptions of code 
Below I've provided functional level descriptions of code. The code contains detailed comments about each line and how to use it. 

### ArduinoGPSwSDcard_continous.ino
This is the code that needs to be uploaded on the Arduino so it can collect data from the GPS and save it on the SD card. The Arduino 

1. Recieves data from the GPS and puts that data into a buffer. 
2. Then writes the data to a file in the SD card through the SD module. 
3. After this it pauses for 5 seconds and repeats the last two steps. 

Please refer to the [Hardware](https://github.com/MiningMyBusiness/GPSTracker/raw/master/Hardware) folder in the repo for info about wiring and possible troubleshooting before this code will run correctly. 

### gpsDataExtractor.py
This Python code goes through the saved data and parses it 
