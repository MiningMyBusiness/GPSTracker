# GPS data extractor and visualizer
# Extracts GPS data from a saved text file collected with homemade GPS tracking
#   module
# Author: Kiran Bhattacharyya (bhattacharyyakiran12@gmail.com)
# License: MIT License


##############################
### Get data from gps file ###
# open gps data file
fileName = 'GPS.TXT'
readFile = open(fileName)

# initialize variables used to read data file
state = 1 # state variable to indicate if code should keep reading from data file
lookFor = 'GPRMC' # string match to look for in data file
lineCounter = 0 # initialize counter to see how many lines are read
lineLimit = 1000000 # the most number of lines to read from gps data file
allLookFor = list() # list to store all extracted relevant lines
charLimit_lo = 60 # upper and lower character limits for lines with relevant info
charLimit_hi = 72
# these limits were determined by studying the data closely, it is likely the same
# for all gps modules out there. Sometimes a lot of garbage is read out by the
# gps modules, this will help remove that garbage from the data we store.

# start reading every line of the gps data file
while state == 1:
    newLine = readFile.readline() # read  lines
    lineCounter = lineCounter + 1 # update counter
    locInLine = newLine.find(lookFor) # see if line has what we want
    if locInLine == 1: # if so
        numOfChar = len(newLine) # get the number of characters in line
        if (numOfChar >= charLimit_lo) & (numOfChar <= charLimit_hi): # if line has right number of characters
            allLookFor.append(newLine) # append line to list of relevant lines
    if lineCounter == lineLimit: # if counter reaches limit
        state = 2 # change state to stop reading

readFile.close() # close gps data file

#################################################################
### Create data table with time, date, latitude and longitude ###

# initialize lists to store extracted data
timeStr = list() # time of readout
lat = list() # latitude of readout
lon = list() # longitude of readout
dateStr = list() # date of readout

commaNumber = 12 # the line needs to have 12 commas to have all relevant info in the correct order

# converts string latitude and longitude in degrees and minutes to float decimals
def degminToDec(latOrLon):
    pointLoc = latOrLon.find(".")
    degrees = float(latOrLon[0:(pointLoc - 2)])
    minutes = float(latOrLon[(pointLoc - 2):])/60
    total = degrees + minutes
    return total;

# give sign to latitude and longitude value based on hemisphere
def giveSign(latOrLon, hemi):
    if (hemi == "N") or (hemi == "E"):
        withSign = latOrLon
    if (hemi == "S") or (hemi == "W"):
        withSign = -latOrLon
    return withSign

# look through all relevant lines in our list and extract data
import re
for i in xrange(0, len(allLookFor)):
    thisLine = allLookFor[i] # get line
    commaIndx = [m.start() for m in re.finditer(',', thisLine)] # find commas in line
    if len(commaIndx) == commaNumber: # if line has the right number of commas
        # get latitude and longitude as string
        thisLat = thisLine[commaIndx[2]+1:commaIndx[3]] # get latitude
        thisLon = thisLine[commaIndx[4]+1:commaIndx[5]] # get longitude
        hemiNS = thisLine[commaIndx[3]+1:commaIndx[4]] # get hemisphere
        hemiEW = thisLine[commaIndx[5]+1:commaIndx[6]]

        if len(thisLat) > 0:
            thisLat = degminToDec(thisLat) # convert from string to float with signs
            thisLat = giveSign(thisLat, hemiNS)
            thisLon = degminToDec(thisLon)
            thisLon = giveSign(thisLon, hemiEW)
            lat.append(thisLat)
            lon.append(thisLon)

            # extract date and time
            timeStr.append(thisLine[commaIndx[0]+1:commaIndx[1]]) # extract time
            dateStr.append(thisLine[commaIndx[8]+1:commaIndx[9]]) # extract date

###################################
### Plot data on google roadmap ###

# import relevant libraries
import numpy as np
import gmplot

# calculate mean latitude and longitude
meanLat = np.mean(lat)
meanLon = np.mean(lon)

# pull map from database
zoomLevel = 13 # set map zoom level
gmap = gmplot.GoogleMapPlotter(meanLat, meanLon, zoomLevel)

# plot points on map
gmap.scatter(lat, lon, '#3B0B39', size=40, marker=False)
gmap.plot(lat, lon, 'cornflowerblue', edge_width=2)

# save map as html file
gmap.draw("mymap.html")
