#! /usr/bin/env python #open up a terminal

#include as external dictionary
#dict = eval(open("yourfile.txt").read())
#dictionary=dict(zip(one,two)); one=[a,b]; two=[a,b]

#key -> value
AminoDict={
'A':89.09,
'R':174.20,
'N':132.12,
'D':133.10,
'C':121.15,
'Q':146.15,
'E':147.13,
'G':75.07,
'H':155.16,
'I':131.17,
'L':131.17,
'K':146.19,
'M':149.21,
'F':165.19,
'P':115.13,
'S':105.09,
'T':119.12,
'W':204.23,
'Y':181.19,
'V':117.15
}

#ProteinSeq = raw_input("Enter a Protein sequence:")
#ProteinSeq = ProteinSeq.upper().replace(" ","")

ProteinSeq = "FDILSATFTYGNR"
for AminoAcid in ProteinSeq:
	#print AminoAcid
	print AminoAcid, AminoDict[AminoAcid]
	
#molecular weight of protein

MolWeight = 0 #must set to 0 for start
for AminoAcid in ProteinSeq:
	MolWeight = MolWeight + AminoDict[AminoAcid]
	
print "Protein: ", ProteinSeq
print "Molecular weight: %1f" % (MolWeight)

#other dictionary functions .get, .sort
#lists count the spaces (this will become more important when returning mysql results)

#list replacement, create a quick list
seq_string = 'ACTGA'
seq_list = list(seq_string)
seq_list[3] = 'U' # replacement
print seq_string
print seq_list


