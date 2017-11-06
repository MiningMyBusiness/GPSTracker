// Grabs data from GPS module and writes to an SD card every 5 seconds.
//
// License: MIT License
//
// Author: Kiran Bhattacharyya (bhattacharyyakiran12@gmail.com)   


// include relevant libraries
#include <SPI.h> 
#include <SD.h>

int chipSelect = 4; // set the digital out pin to connect to SD card module chip select
 
void setup() {

  //Being serial communication with Arduino and GPS Module //Important rate must be 9600
  Serial.begin(9600);
  
  // see if the card is present and can be initialized:
  if (!SD.begin(chipSelect)) {
    // don't do anything more:
    return;
  }    
}
 
void loop() {

  byte pbyGpsBuffer[500]; // initialize a variable to store GPS data 
  int byBufferIndex = 0; // initialize an indexing variable

  while (byBufferIndex < 500) { // while indexing variable is smaller than index available in storing variable
    
    //Read output of GPS (if available) and save in a buffer
    if (Serial.available()) {
      pbyGpsBuffer[byBufferIndex ++] = Serial.read(); // put data in buffer
    }
  }

  File myFile = SD.open("gps.txt", FILE_WRITE); // open file in SD card
    
  if (myFile) { // if file opens 
    myFile.write(pbyGpsBuffer, byBufferIndex); // then write data
    myFile.close(); // close the file 
  }

  delay(5000); // delay 5 seconds before relooping
  
}
