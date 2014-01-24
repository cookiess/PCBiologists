#! /usr/bin/env python
#import fasta files


import sys
if len(sys.argv)<1:
	print "file not in correct format, should be fasta file"
else:
	filelist = sys.argv[1:] #takes certain number of files in list (all)
	print filelist
	for infilename in filelist:
		sys.stderr.write("processing file %s\n" % (infilename))
	delimiter = '\t'	
	masterlist = [] #set empty and make first list
	seq_dictionary = {}
	
#modify to improve filename
	for infilename in filelist:
		infile = open(infilename, 'r')
		
		for line in infile:
			line = line.strip()
		#	print line
			if line[0] == '>': #what is line?
				name = line.replace(">","")
				seq_dictionary[name] = ''
			else:
				seq_dictionary[name] += line #+= is important here; show example
	masterlist = seq_dictionary.items()
	 #print seq_dictionary
	header = ''
	header += "name" + delimiter + "sequence"
	print header
	for x in masterlist:
		print x[0] + "\t" + x[1]
