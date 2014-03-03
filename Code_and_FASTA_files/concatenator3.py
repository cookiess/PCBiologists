#!/usr/bin/env python
# run this script as: python concatenator3.py *.fasta

#import globals
import sys
import random

# returns list of total length
# [3, 9, 12]
def get_longest_line(filelist):
	lineLength = {}
	fileLength = []
	
	for infilename in filelist:
		for line in open(infilename, 'r'):
			gene = infilename.replace(".fasta","")
			line = line.strip()
			if line[0] == '>':
				name = line.replace(">","")
				if not name in lineLength: #does not work if on 2 lines
					lineLength[name] = ''
			else:
				lineLength[name] += line
		x = len(random.choice(lineLength.values()))
		fileLength.append(x)
	return fileLength
	

# defines list of names
# prints ['Aus_bus', 'Cus_dus', 'Zus-yus', 'Eus_fus', 'Gus_hus', 'Auss_bus']
def totalNames(infilename):
	nameList = []
	for infilename in filelist:
		for line in open(infilename, 'r'):
			line = line.strip()
			if line[0] == '>':
				x = line.replace(">","")
				if x not in nameList:
					nameList.append(x)
	return nameList		


# takes arguments from system
if len(sys.argv)<1:
	print "file not in correct format, should be fasta file"
else:
	filelist = sys.argv[1:] #takes certain number of files in list (all)
	#print filelist
	for infilename in filelist:
		sys.stderr.write("processing file %s\n" % (infilename))

master = {}
longestString = []
longestString = get_longest_line(filelist)
fileNumber = 0

#create a dict named master and add keys
for infilename in filelist:
	infile = open(infilename, 'r')
	nameList = totalNames(infilename)
	tempList = []
	for line in infile:
		line = line.strip()

		if line[0] == '>':
			name = line.replace(">","")
			if not name in master:
				master[name] = '' #has final dict of name = ''
		else:
			master[name] += line
			tempList.append(name)

# look for keys not added to master and deal with these separately
# use length of sequence per file (gene) and tempList of what was added during last iteration			
	notIn = list(set(nameList) - set(tempList))
	for x in notIn:
		if not x in master:
			master[x] = ''
			#print nameList,master[x],longestString[fileNumber]
			while len(master[x]) < longestString[fileNumber]:
				master[x] += "-"
		else:	
			#print nameList,master[x],longestString[fileNumber]
			while len(master[x]) < longestString[fileNumber]:
				master[x] += "-"					

	fileNumber += 1
			
			
	infile.close()
	
# print final dictionary
print master
