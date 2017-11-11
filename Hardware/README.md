# Hardware build descriptions
This folder and ReadMe contains relevant information about how to build the GPS module. 

### Parts list
To build the GPS module as described here you will need the following parts:

1. [Arduino Nano](https://www.amazon.com/gp/product/B0713XK923/ref=oh_aui_search_detailpage?ie=UTF8&psc=1)
2. [GPS module](https://www.amazon.com/gp/product/B01AW5QYES/ref=oh_aui_search_detailpage?ie=UTF8&psc=1)
3. [SD card module](https://www.amazon.com/gp/product/B01JYNEX56/ref=oh_aui_search_detailpage?ie=UTF8&psc=1)
4. [SD card](https://www.amazon.com/SanDisk-Memory-SDSDUN-008G-G46-Newest-Version/dp/B00M55BS5O/ref=sr_1_7?s=pc&ie=UTF8&qid=1510386475&sr=1-7&keywords=8gb+SD+card)
5. [3.7V Lipo battery](https://www.amazon.com/gp/product/B01HG7TYNI/ref=oh_aui_detailpage_o03_s00?ie=UTF8&psc=1)
6. [3.7V to 5V boost converter](https://www.amazon.com/gp/product/B01LW57OUM/ref=oh_aui_detailpage_o07_s00?ie=UTF8&psc=1)

Each part name is a link to the Amazon page for the parts I used to make my module. However, you do not need to adhere exactly to these parts.

### Schematic
The images below represent the wiring of all components in two different ways.

1. A breadboard view with cartoon representation of components made with [Fritzing](http://fritzing.org/home/).
<img src="https://github.com/MiningMyBusiness/GPSTracker/raw/master/Hardware/GPSSchematic_bb.png" width="500">

2. A circuit diagram of the wiring of components also made with Fritzing. 
<img src="https://github.com/MiningMyBusiness/GPSTracker/raw/master/Hardware/GPSSchematic_schem.png" width="500">

I used a different 3.7V to 5V boost converter than the one shown in the schematic (link is provided in parts list above) which was a lot simpler and cheaper. 

IMPORTANT NOTE: Do not have the GPS module powered and connected to the RX pin of the Arduino when uploading code onto the Arduino. This will interfere with uploading code onto the Arduino. Power the GPS module after the code has been uploaded onto the Arduino. 

### Initial prototype
I've attached some images which show the prototype I made to collect some pilot data and test feasibility of this project. The computer mouse in the image provides a size comparison with the prototype. 

1. Prototype innards
<img src="https://github.com/MiningMyBusiness/GPSTracker/raw/master/Hardware/boxOpen.JPG" width="500">

2. Top view
<img src="https://github.com/MiningMyBusiness/GPSTracker/raw/master/Hardware/boxTop.JPG" width="500">

3. Side view
<img src="https://github.com/MiningMyBusiness/GPSTracker/raw/master/Hardware/boxSide.JPG" width="500">

I plan to miniaturize this further and solder components onto a smaller board.

### Tips for hardware replication
I would HIGHLY recommend building this project in pieces and troubleshooting along the way. These are some webpages I found to be very useful. 

- [SD card notes](https://www.arduino.cc/en/Reference/SDCardNotes)
- [SD card read/write](https://www.arduino.cc/en/Tutorial/ReadWrite)

I would not recommend trying to use the SoftwareSerial library with the GPS module. I found that it did not work well for me.

