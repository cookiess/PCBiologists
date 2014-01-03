#! /usr/bin/env python #open up a terminal

#good coding habits - svn, git or dropbox

DNA_sequence = 'ATGTCTCATTCAFAGCA'
#DNA_sequence = raw_input("Enter a DNA sequence:") #script now asks a question from user for input
DNA_sequence = DNA_sequence.upper().replace(" ","") #case sensitive #removes white space


#-----------------------
for x in DNA_sequence:
		if x != ('A' and 'T' and 'C' and 'G'):
			y = 'TRUE'
			#add here to show same repeat
			
if y == 'TRUE':
	print "your sequence %s contains bad characters" % DNA_sequence
#-----------------------


#what does this mean %
#what does : mean (creates a slice)
	
########write a script that gives you the reverse sequence

print 'Sequence:', DNA_sequence
sequence_length =  float(len(DNA_sequence))
print 'Sequence Length:', sequence_length

numberA = DNA_sequence.count('A')
numberG = DNA_sequence.count('G')
numberC = DNA_sequence.count('C')
numberT = DNA_sequence.count('T')

print 'A:', numberA/sequence_length
print 'G:', numberG/sequence_length
print 'C:', numberC/sequence_length
print 'T:', numberT/sequence_length

print "there are %5d A bases, out of %d" % (numberA,sequence_length) #padded with 5 decimal places
print "there are %.2f A bases, out of %d" % (numberA,sequence_length) #control length of your float
print "there are %s A bases, out of (%s + %s)" % (numberA,sequence_length,"5")

TotalStrong = numberG + numberC
TotalWeak = numberA + numberT

if sequence_length >= 14:
	MeltTempLong = 64.9 + 41 * (TotalStrong - 16.4) / sequence_length
	print "Tm Long (>14): %.if C" % (MeltTempLong) ### explain this statement in words
else:  ##fix this error, why wont it run?
	MeltTemp = (4 * TotalStrong) + (2 * TotalWeak)
	print "Melting Temp : %.if C" % (MeltTemp)
		
#-----------------------
	pair = []
for x in DNA_sequence:
	if x == 'A':
		pair.extend('T')
	elif x == 'T':
		pair.extend('A')
	elif x == 'G':
		pair.extend('C')
	elif x == 'C':
		pair.extend('G')

print "The complementary sequence of %s is %s" % (DNA_sequence, pair)	
#-----------------------		
	#A with T: the purine adenine (A) always pairs with the pyrimidine thymine (T)
	#C with G: the pyrimidine cytosine (C) always pairs with the purine guanine (G)
# %d = interger digit
# %s = string
# %f = float


#single and double quotes; quotes type it as a string
#functions lowecase; capitilize variables and use _. TextMate has no trouble figuing out variables
#which version of python? python -V (if 3.0)
#functions http://docs.python.org/2.7/library/functions.html

#print '7' + str(3*2)
#print float(7) #same as 7.0
