# GPS Tracker
Collection, visualization, and analysis of GPS data gathered with a homemade GPS module.

## Motivation
The concept of connectivity recives a lot of attention from a wide variety of fields. While we tend to reserve the main discussions about connectivity to the digital realm, I find myself drawn to the concept of connectivity in the physical world. Where we travel everyday and how we get there directly influences what we are exposed to and what is exposed to us. This has consequences for everything from disease epidemics to advertising. Moreover, such a record of movement would allow individuals to create an auxiliary memory of the history of places visited with great detail. Having access to this kind of information could have the potential for changing our sense of ourselves. 

For these reasons, I decided to track everywhere I go every day. I hope that this will give me an idea about how I move and where I go in this city, this country, and this world. Moreover, it will be a direct record of everywhere I have gone. I want to extract from this data the balance between my walking and using vehicular transport, my carbon footprint, and the geographical web in which I live my life. 

## Hardware
The homemade GPS module consists of Arduino Nano, an SD card module, an SD card, a passive ceramic GPS module, a 3.7V to 5V boost converter, and a LiPo battery. A schematic is shown below but more detail can be found in the [Hardware](https://github.com/MiningMyBusiness/GPSTracker/raw/master/Hardware) folder of the repository. The code used to program the Arduino can be found in the [Code](https://github.com/MiningMyBusiness/GPSTracker/raw/master/Code) folder of this repository.

<img src="https://github.com/MiningMyBusiness/GPSTracker/raw/master/Hardware/GPSSchematic_bb.png" width="500">

I chose to make a homemade GPS over using the GPS in my smart phone. The cons of doing this include having to build and carry another piece of hardware. The pros include not having to worry about data plans, about your cell phone battery dying, about how your data may be held hostage or used by apps like [Swarm](https://en.wikipedia.org/wiki/Swarm_(app)), and the opportunity to learn something new. Additionally, since this homemade GPS module doesn't rely on cellular phone networks, it can track me anywhere in the world including in the middle of an ocean or a desert (assuming I go there). 

### Pilot hardware
I implemented the beta version of this hardware in a carboard Sparkfun box shown below (the mouse is in the image for comparison). This was adequately portable to collect pilot data. Use the mouse in the photo for size comparison.

<img src="https://github.com/MiningMyBusiness/GPSTracker/raw/master/Hardware/boxOpen.JPG" width="500">

### Prototype hardware
I also made a much smaller version which I took with me when I travelled out of the country. The battery is blocking the view to the remainder of the parts.

<img src="https://github.com/MiningMyBusiness/GPSTracker/raw/master/Hardware/Mini_OpenTop1.JPG" width="500">

More pictures of the smaller version and the .stl files for the 3D model of the box are provided in the [Hardware](https://github.com/MiningMyBusiness/GPSTracker/raw/master/Hardware) folder of the repository. This was tested on mountain roads between Bogota, Chaochi, and Ubaque in Colombia. These roads often do not have very dependable cell or data service. However, the main towns are well connected. 

## Data
The GPS module transmits recieved data to the Arduino. The Arduino writes this data to a text file in the SD card. Some lines in the text file might look like the following:

$GPRMC,070750.00,A,4200.31462,N,08739.74022,W,0.980,,251017,,,A*64 <br />
$GPVTG,,T,,M,0.980,N,1.815,K,A*2F <br />
$GPGGA,070750.00,4200.31462,N,08739.74022,W,1,03,4.76,257.7,M,-33.8,M,,*6D <br />
$GPGSA,A,2,16,27,08,,,,,,,,,,4.86,4.76,1.00*07 <br />
$GPGSV,1,1,04,08,68,076,33,16,13,068,35,27,34,047,23,33,04,102,33*70 <br />
$GPG076,33,16,13,068,34,27,34,047,23,33,04,102,32*70 <br />
$GPGLL,4200.31735,N,08739.74210,W,070755.00,A,A*7B <br />

Please take a look at the [Code](https://github.com/MiningMyBusiness/GPSTracker/raw/master/Code) in the repo to see how to make sense of this data. There is a [Python script](https://github.com/MiningMyBusiness/GPSTracker/raw/master/Code/gpsDataExtractor.py) in the [Code](https://github.com/MiningMyBusiness/GPSTracker/raw/master/Code) folder of the repository that parses through this data and organizes the date, time, latitude and longitude into lists. Then plots this data onto a Google roadmap and saves to an .html with zoom functionality. 

### Pilot data
I collected some data with the pilot hardware around Chicago as I went to work or went out to eat. Open the [html file](https://rawgit.com/MiningMyBusiness/GPSTracker/master/Results/mymap.html) to explore the dataset but I've also provided a static screenshot of the map below. 

<img src="https://github.com/MiningMyBusiness/GPSTracker/raw/master/Results/mapImg.png" width="500">

## Work in progress
The next steps involve breaking this data into trips taken by day. Then using the speed of movement I can determine if I was walking or on vehicular transport. Potentially, by using locations where data is collected I can also determine if I was using the L-train. 

