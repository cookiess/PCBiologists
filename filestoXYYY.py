#! /usr/bin/env python
# imports 4 files and appends list based on matching first row
# run with an argument filestoXYYY.py spectra/LED*.txt
import sys


if len(sys.argv)<2:
	print "file not in correct format, reads tab delimited files with first column being an identifier or number to match"
else:
	filelist = sys.argv[2:] #takes certain number of files in list (all)
	print filelist
	for infilename in filelist:
		sys.stderr.write("processing file %s\n" % (infilename))
	header = 'lamda'
	linestoskip = 1
	
	delimiter = '\t'	
	filenumber = 0
	masterlist = [] #set empty and make first list

#modify to improve filename
	for infilename in filelist:
		header += delimiter + infilename.replace("spectra/","").replace(".txt","") #what is += here?
		infile = open(infilename, 'r')
		linenumber = 0
		recordnumber = 0
		
		for line in infile:
			if linenumber > (linestoskip-1) and len(line) > 3:
				line=line.strip('\n')
				if filenumber == 0:
					masterlist.append(line)
				else:
					elementlist=line.split(delimiter)
					if len(elementlist)>1:
						masterlist[recordnumber] += "\t" + elementlist[1]
						recordnumber+=1
			linenumber += 1
			
		sys.stderr.write("converted file %s\n" % (filenumber))
		
		filenumber  += 1
		infile.close()
		
	print header
	for item in masterlist:
		print item
		#output file filestoXYYY.py spectra/LED*.txt >test.txt (>> appends)
		
	
	
		
		
#may need to strip endline characters from windows '/r' or open using paremeter 'rU'