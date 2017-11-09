# GPS Tracker
Collection, visualization, and analysis of GPS data gathered with a homemade GPS module.

## Motivation
The concept of connectivity recives a lot of attention from a wide variety of fields. While we tend to reserve the main discussions about connectivity to the digital realm, I find myself drawn to the concept of connectivity in the physical world. Where we travel everyday and how we get there directly influences what we are exposed to and what is exposed to us. This has consequences for everything from disease epidemics to advertising.  

I wanted to know how connected (or disconnected) I was to the rest of Chicago, the city where I live. I decided to measure this by tracking everywhere I go every day. I hope that this will give me an idea about how I move and where I go in this city, this country, and this world. Moreover, it will be a direct record of everywhere I have gone. I want to extract from this data the balance between my walking and using vehicular transport, my carbon footprint, and the geographical web in which I live my life. 

## Hardware
The homemade GPS module consists of Arduino Nano, an SD card module, an SD card, a passive ceramic GPS module, a 3.7V to 5V boost converter, and a LiPo battery. A schematic is shown below but more detail can be found in the [Hardware](https://github.com/MiningMyBusiness/GPSTracker/raw/master/Hardware) folder of the repository.

<img src="https://github.com/MiningMyBusiness/GPSTracker/raw/master/Hardware/GPSSchematic_bb.png" width="500">

I chose to make a homemade GPS over using the GPS in my smart phone. The cons of doing this include having to build and carry another piece of hardware. The pros include not having to worry about data plans, about your cell phone battery dying, and the opportunity to learn something new. Additionally, since this homemade GPS module doesn't rely on cellular phone networks, it can track me anywhere in the world including in the middle of an ocean or a desert (assuming I go there). 

The code used to program the Arduino can be found in the [Code](https://github.com/MiningMyBusiness/GPSTracker/raw/master/Code) folder of this repository. I implemented the beta version of this hardware in a carboard Sparkfun box shown below (the mouse is in the image for comparison). This was adequately portable to collect pilot data. 

<img src="https://github.com/MiningMyBusiness/GPSTracker/raw/master/Hardware/boxOpen.JPG" width="500">

## Data
The GPS module transmits recieved data to the Arduino. The Arduino writes this data to a text file in the SD card. Some lines in the text file might look like the following:

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

There is a [Python script](https://github.com/MiningMyBusiness/GPSTracker/raw/master/Code/gpsDataExtractor.py) in the [Code](https://github.com/MiningMyBusiness/GPSTracker/raw/master/Code) folder of the repository that parses through this data and organizes the date, time, latitude and longitude into lists. Then plots this data onto a Google roadmap and saves to an [html file](https://github.com/MiningMyBusiness/GPSTracker/raw/master/Results/mymap.html) with zoom functionality. There is a screenshot of the map below. 

<img src="https://github.com/MiningMyBusiness/GPSTracker/raw/master/Results/mapImg.png" width="500">

