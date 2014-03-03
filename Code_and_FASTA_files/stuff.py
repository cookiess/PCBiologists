#! /usr/bin/env python
#import fasta files


import sys

if len(sys.argv)<1:
	print "file not in correct format, should be fasta file"
else:
	filelist = sys.argv[1:] #takes certain number of files in list (all)
	#print filelist
	for infilename in filelist:
		sys.stderr.write("processing file %s\n" % (infilename))
		
	finalDict = []
	seq_dictionary = {}
	newDict = {}
	SeqLength = {}
	
#modify to improve filename
	for infilename in filelist:
		infile = open(infilename, 'r')
		gene = infilename.replace(".fasta","")
		print gene
		
		for line in infile:
			line = line.strip()
			if line[0] != '>':
				print len(line)

			
		#	print line
			if line[0] == '>': #what is line?
				name = line.replace(">","")
				#name = line.replace(">",gene + "|")
				seq_dictionary[name] = ''
				SeqLength[gene] = ''
			else:
				seq_dictionary[name] += line #+= is important here; show example
				# l = len(line)
				# SeqLength[gene] = l
				
		# for x in seq_dictionary.items():
		# 	finalDict.append(x)
			

print seq_dictionary
		
	# for key, value in finalDict:
	# 	if newDict.has_key(key):
	# 		newDict[key] += value
	# 	else:
	# 		newDict[key] = ''
	# 		newDict[key] += value
	# 
	# 	tmp = None
	# for a,b in newDict.items():
	# 	tmp = a + "\t" + b
	# 	print tmp
	# 	
	# 	print SeqLength



		
				# 
				# +----------+--------------+------+-----+---------+----------------+
				# | Field    | Type         | Null | Key | Default | Extra          |
				# +----------+--------------+------+-----+---------+----------------+
				# | id       | int(11)      | NO   | PRI | NULL    | auto_increment |
				# | taxon    | varchar(64)  | NO   |     | NULL    |                |
				# | gene     | varchar(64)  | NO   |     | NULL    |                |
				# | sequence | varchar(128) | NO   |     | NULL    |                |
				# +----------+--------------+------+-----+---------+----------------+
				# 		
			
		







