#! /usr/bin/env python
# basic method for reading a file

# set input file name
filename = "Marrus_claudanielis.txt"

#open file and read
file = open(filename, 'r')

#line number set
lnumber = 0

#loop through each file
for Line in file:
	Line = Line.strip('\n')
	print lnumber, ':', Line
	lnumber = lnumber + 1
	
file.close()