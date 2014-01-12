#! /usr/bin/env python #open up a terminal

#good coding habits - svn, git or dropbox

#DNA_sequence = 'ATG'
DNA_sequence = raw_input("Enter a DNA sequence:") #script now asks a question from user for input
DNA_sequence = DNA_sequence.upper().replace(" ","") #case sensitive #removes white space

#-----where to find out answers??
# print dir(DNA_sequence)
# help(DNA_sequence.count)
# built in functions http://docs.python.org/2/library/functions.html


#move to a function next go round
#-----------------------------
y = True #is setting the variable
bases = ['A','T','C','G']
for x in DNA_sequence:
	for z in bases:
		if x not in bases: #and/or
			y = False
			break
			
if y == False: #is a comparison
	print "your sequence %s contains bad characters" % DNA_sequence
elif y == True:
	print "your sequence %s is alright" % DNA_sequence
else:
	print "something wrong"
#----------------------------


#what does this mean % - kind of a insert sequence
#what does : mean (creates a slice)

#strong typing in python
# %d = interger digit
# %s = string
# %f = float
#print '7' + str(3*2)
#print float(7) #same as 7.0

print 'Sequence:', DNA_sequence
sequence_length =  float(len(DNA_sequence))
print 'Sequence Length:', sequence_length

#way to do this #1
numberA = DNA_sequence.count('A')
numberG = DNA_sequence.count('G')
numberC = DNA_sequence.count('C')
numberT = DNA_sequence.count('T')

print 'A:', numberA/sequence_length * 100
print 'G:', numberG/sequence_length * 100 
print 'C:', numberC/sequence_length * 100
print 'T:', numberT/sequence_length * 100

#looping way to do the same thing #2
BaseList = "ACGT"
for Base in BaseList:	
	Percent = 100 * DNA_sequence.count(Base) / sequence_length
	print "%s: %4.1f" % (Base,Percent)

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

#modify to create complementary sequence
#--------------------------
#A with T: the purine adenine (A) always pairs with the pyrimidine thymine (T)
#C with G: the pyrimidine cytosine (C) always pairs with the purine guanine (G)
# working with lists: http://effbot.org/zone/python-list.htm
# an iterable reversed()

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

reverse_sequence = ''.join(list(reversed(DNA_sequence)))
complement = ''.join(pair)
reverse_complement = ''.join((list(reversed(pair))))
print "The reverse of %s is %s" % (DNA_sequence, reverse_sequence)	
print "The complement of %s is %s" % (DNA_sequence,complement)
print "The reverse complement of %s is %s" % (DNA_sequence, reverse_complement)	
#--------------------------

reverse = reverse[::-1]
baseconversion = {A:T, T:A}



