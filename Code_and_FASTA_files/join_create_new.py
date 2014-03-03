#!/usr/bin/env python
import sys
import os
import glob
import csv
import fnmatch

#OutFileName = raw_input('Output file name?')
#OutFile = open(OutFileName, 'w')

FileList = sys.argv[1:]
headers = []

for element in FileList:
	SequenceDict = {}
	name_list = {}
	seq_name = element.replace(".fasta","")
	name = str(seq_name)
	InFile = open(element, 'r')

	
	#create outfile for printing dict
	OutFile = open(name +".dict", 'w')

	for line in InFile:
		line = line.strip()
		#print line
		if line[0] == '>': #what is line?
			name = line.replace(">","")
			SequenceDict[name] = ''
		else:
			SequenceDict[name] += line
	name_list[seq_name] = ''
	name_list[seq_name] = SequenceDict
	
	#create outfile dictionary			
	dict_for_file = str(SequenceDict)
	OutFile.write(dict_for_file)
	
#print headers

# for file in os.listdir('.'):
#     if fnmatch.fnmatch(file, '*.dict'):
# 		#print file
# 		InFile = open(file, 'r')
# 		for x in InFile:
# 			MyList = []
# 			MyList.append(x)
# 			MyList = line.replace("{","")
# 			MyList = line.replace("}","")
# 		for y in MyList:
# 			print y
# 		
		







	