#!/usr/bin/env python
import sys
import re

#OutFileName = raw_input('Output file name? ')
#OutFile = open(OutFileName, 'w')
filelist = sys.argv[1:]
filetally = 1
for x in filelist:
	print ("Gene #%d being added: " + x) % filetally
	filetally += 1


# Making a list to identify all unique taxa across all alignments
mastertaxa = []
for infilename in filelist:
	infile = open(infilename, 'r')
	for line in infile:
		line = line.strip()
		if line[0] == '>':
			if not line in mastertaxa:
				mastertaxa.append(line)
print mastertaxa
# For each gene, fill in missing taxa with dashes
#for infilename in filelist:
#	infile = open(infilename, 'r')
#	localtaxa = []
#	for line in infile:
#		line = line.strip()
#		if line[0] == '>':
#			localtaxa.append(line)
#		for taxon in mastertaxa:
#			if taxon != [localname for localname in localtaxa]:
#				print 'what'
#	print localtaxa
		#	if taxa != line:
		#		print '%s is not in that fasta file' % taxon
#print mastertaxa


		

# The actual concatenation of all genes
master = {}
for infilename in filelist:
	infile = open(infilename, 'r')
	for line in infile:
		line = line.strip()						
		if line[0] == '>':
			name = line.replace(">","")
			if not name in master:
				master[name] = ''
		else:
			master[name] += line
print master