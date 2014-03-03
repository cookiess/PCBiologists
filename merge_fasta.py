#! /usr/bin/env python
#import fasta files

import sys

# ask question if have another; if true than build dictionary based on that gene name
# break on a no
# could requre specific file name

def create_dictionary():
	Dict_name = raw_input("which gene?: ")
	print 'Creating dictionary for:', Dict_name
	masterlist[Dict_name] = ''
	filelist = raw_input("which files?: ")
	print "filelist for %s: %s" %  (Dict_name,filelist)
	masterlist[Dict_name] = filelist
	next_gene = raw_input("do you have another gene for the file? Y/N: ")
	if next_gene == 'Y': 
		create_dictionary()
	else:	
		print masterlist
		
# add is this correct?
# loop and ask if done
masterlist = {}
create_dictionary()

for genes in masterlist.items():
 	gene_name = genes[0]
	# 	dict_name = []
	# 	dict_name = genes[0],genes[1]
	# 	print dict_name
	dict_name = "seq_dictionary_" + gene_name
	dict_name = {}
	filelist = genes[1].split(',') #need to loop over a list
	print filelist
	for infilename in filelist:
		print infilename
	 	infile = open(infilename, 'r')
	 	for line in infile:
	 			line = line.strip()
	 			print line
	 			if line[0] == '>': #what is line?
	 				name = line.replace(">","")
	 				dict_name[name] = ''
	 			else:
	 				dict_name[name] += line #+= is important here; show example
	 	print gene_name
		print dict_name
	 		# masterlist = seq_dictionary.items()

