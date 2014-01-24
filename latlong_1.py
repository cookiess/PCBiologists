#! /usr/bin/env python
#coding: utf-8

# basic method for reading a file
import re #module import, include at beginning

#add date to file export
from datetime import date
now = date.today()

#\d+ \d+\.\d+ \w #how did you write this? why the []?
#http://manual.macromates.com/en/regular_expressions

# set input file name
#functions have to be at front of file. Can we import them?
def decimalat(dstring):
	find = r"(\d+) ([\d+\.]+) (\w)"
	result = re.search(find,dstring)
	
	degrees = float(result.group(1))
	minutes = float(result.group(2))
	compass = result.group(3).upper()
	
	decimaldegree = degrees + minutes/60
	
	if compass == 'S' or compass == 'W':
		decimaldegree = -decimaldegree
		
	return decimaldegree
#end of function decimalat

filename = "Marrus_claudanielis.txt"
outfilename = "Marrus_claudanielis_processed_%s.kml" % now
#open file and read
file = open(filename, 'r')
outfile = open(outfilename, 'w')

#line number set
lnumber = 0
#w = "Depth\tLat\tLon"
#outfile.write(w + "\n") #create new headers

header = '''<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<kml xmlns=\"http://earth.google.com/kml/2.2\">
<Document>'''

outfile.write(header)
print header


#loop through each file
for Line in file:
	if lnumber > 0: #skips header line
		Line = Line.strip('\n')
		#print lnumber, ':', Line
		element = Line.split('\t')
		dlat = decimalat(element[2])
		dlong = decimalat(element[3])
		dive = element[0]
		date = element[1]
		depth = element[4]
		comment = element[5]
		
		#x = "%s\t%s\t%.4f\t%.4f\t%s\t%s" % (dive,depth,dlat,dlong,date,comment) #constrained to 4 floating point
		contentstring = '''
		<Placemark>
			<name>Marrus - %s</name>
			<description>%s</description>
			<Point>
				<altitudeMode>absolute</altitudeMode>
				<coordinates>%f,%f,-%s</coordinates>
			</Point>
		</Placemark>'''
		
		outfile.write(contentstring) #appends to file
		print contentstring
	#lnumber = lnumber + 1
	lnumber += 1
	
#closes the files
file.close()
outfile.close()