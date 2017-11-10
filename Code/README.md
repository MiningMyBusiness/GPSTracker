# Code overview
This folder contains all relevant code to 
1. Collect data
2. Parse and clean data
3. Visualize data

## Descriptions of code 
Below I've provided higher-level descriptions of functions the code performs. The code files contain detailed comments about each line and how to use it. 

### ArduinoGPSwSDcard_continous.ino
This is the code that needs to be uploaded on the Arduino so it can collect data from the GPS and save it on the SD card. The Arduino 

1. Recieves data from the GPS and puts that data into a buffer. 
2. Then writes the data to a file in the SD card through the SD module. 
3. After this it pauses for 5 seconds and repeats the last two steps. 

Please refer to the [Hardware](https://github.com/MiningMyBusiness/GPSTracker/raw/master/Hardware) folder in the repo for info about wiring and possible troubleshooting before this code will run correctly. 

### gpsDataExtractor.py
This Python code processes and visualizes the saved data. It performs the following functions:

1. Goes through the saved data and parses it to extract relevant lines. 
2. Ignores any nonsense lines that don't make sense. 
3. Creates a list of dates, times, latitudes, and longitudes.
4. Plots these points on a Google roadmap and saves an html file. 

Lines written to the SD card may look like the chunk of text below:

$GPRMC,070750.00,A,4200.31462,N,08739.74022,W,0.980,,251017,,,A*64 <br />
$GPVTG,,T,,M,0.980,N,1.815,K,A*2F <br />
$GPGGA,070750.00,4200.31462,N,08739.74022,W,1,03,4.76,257.7,M,-33.8,M,,*6D <br />
$GPGSA,A,2,16,27,08,,,,,,,,,,4.86,4.76,1.00*07 <br />
$GPGSV,1,1,04,08,68,076,33,16,13,068,35,27,34,047,23,33,04,102,33*70 <br />
$GPG076,33,16,13,068,34,27,34,047,23,33,04,102,32*70 <br />
$GPGLL,4200.31735,N,08739.74210,W,070755.00,A,A*7B <br />

You can look at the [GPS Module](https://playground.arduino.cc/Tutorials/GPS) webpage on the Arduino site to understand what all this means but I'll give you the crash course. The line starting with $GPRMC is the most important line (first line). It needs to be broken at the commas to decode the information. 

070750.00 --- 07:07:50.00 UTC (coordinated universal time) <br />
A --- Active <br />
4200.31462 --- 42 degrees and 00.31462 minutes Latitude <br />
N --- Northern hemisphere <br />
08739.74022 --- 87 degrees and 39.74022 minutes Longitude <br />
W --- Western hemisphere <br />
0.980 --- Speed in knots <br />
251017 --- 25/10/2017 date of readout <br />

These are organized into the lists of dates, times, latitudes, and longitudes. Often the GPS also writes a lot of nonsense that needs to be excludes. The Python script does that as well. Finally, it plots these points on a Google roadmap and saves an html file with zoom capabilites. 

This code will be expanded in the future to break this data into trips organized by day and mode of transport. 
