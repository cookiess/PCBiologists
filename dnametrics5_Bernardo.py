#!/usr/bin/env python
import sys
import re
InFileName = raw_input('What is the file name?')
InFile = open(InFileName, 'r')
OutFileName = '%s_output.txt' %(InFileName)
OutFile = open(OutFileName, 'w')

#This block of code transforms the FASTA file into a format that can be read by Blocks 1 to 4. It does so by placing each taxon name and its whole sequence at the same line (by adding a tab to each line that starts with a '>', then stripping the end of the line characters of all line except those before a line that has a '>'). Then it removes end-of-line characters and the '>' symbol. Finally, it splits each line, making the taxon name and the sequence into separate elements.

InFile = ''.join(InFile)
InFile = re.sub('(>.+)', r'\1\t', InFile)
InFile = re.sub('\n([^>].+)', r'\1', InFile)
InterFile = open('InterFile', 'w')
InterFile.write(InFile)
InterFile.close()
InterFile = open('InterFile', 'r')

for Line in InterFile:
	Line = Line.strip('\n')
	Line = Line.strip('>')
	Elements = Line.split('\t')	

	#--------------Block 1: open and verify input sequence---------------------------------------------------------------------------------------------------------

	DNASeq = Elements[1]
	DNASeq = DNASeq.upper()
	DNASeq = DNASeq.replace (" ", "")
	OutFile.write('Reading data from %s\r' % (Elements[0])) 
	OutFile.write('DNA sequence: %s\r' % DNASeq)
	
	ValidBases = ['A', 'C', 'G', 'T', 'R', 'Y', 'S', 'W', 'K', 'M', 'B', 'D', 'H', 'V', 'N']
	BaseList = list(set(DNASeq))

	for base in DNASeq:
		if base in ValidBases:
			y = True
		else:
			y = False
			break
	if y == False:
		sys.exit('Warning; your sequence contains invalid characters. Please enter a valid DNA sequence')

	#--------------Block 2: Length, base content and TMelt---------------------------------------------------------------------------------------------------------


	SeqLength = float(len(DNASeq))
	OutFile.write('Sequence Length: %s\r' %SeqLength)

	for Base in BaseList:
		#if Base == 'A' or 'C' or 'G' or 'T'
			Percent = 100 * DNASeq.count(Base) / SeqLength
			OutFile.write("%s: %4.1f%%\r" % (Base, Percent))

	CGcontent= 100*((DNASeq.count("C")+DNASeq.count("G")+DNASeq.count('S'))/SeqLength)

	OutFile.write("CG content:%.1f%%\r" % CGcontent)

	TotalStrong = DNASeq.count("C")+DNASeq.count("G")
	TotalWeak = DNASeq.count("A")+DNASeq.count("T")

	if SeqLength >= 14:
		#formula for sequences 14 or more nucleotides long
		MeltTempLong = 64.9 + 41 * (TotalStrong - 16.4) / SeqLength
		OutFile.write("Melting Temp (>14): %.1f C\r" % (MeltTempLong))

	else:
		MeltTemp = (4 * TotalStrong) + (2 * TotalWeak)
		OutFile.write("Melting Temp: %.1f C\r" % MeltTemp)


	#--------------Block 3: Reverse complement---------------------------------------------------------------------------------------------------------------------


	Complement = []

	for base in DNASeq:
		if base == 'A':
			Complement.append('T') 
		if base == 'C':
			Complement.append('G') 	
		if base == 'G':
			Complement.append('C') 
		if base == 'T':
			Complement.append('A') 
		
	Reverse = Complement[::-1]
	Reverse = ''.join(Reverse)

	OutFile.write('Reverse-complement sequence: %s\r' % Reverse)

	#--------------#Block 4: Print amino acid translation and molecular weight-------------------------------------------------------------------------------------


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
	'V':117.15,
	'X':0.0,
	'-':0.0,
	'*':0.0
	}

	CodonDict={
	'TAA': 'X',
	'TAG': 'X',
	'TGA': 'X',
	'TTT': 'F',
	'TTC': 'F',
	'TTA': 'L',
	'TTG': 'L',
	'TCT': 'S',
	'TCC': 'S',
	'TCA': 'S',
	'TCG': 'S',
	'TAT': 'Y',
	'TAC': 'Y',
	'TGT': 'C',
	'TGC': 'C',
	'TGG': 'W',
	'CTT': 'L',
	'CTC': 'L',
	'CTA': 'L',
	'CTG': 'L',
	'CCT': 'P',
	'CCA': 'P',
	'CCC': 'P',
	'CCG': 'P',
	'CAT': 'H',
	'CAC': 'H',
	'CAA': 'Q',
	'CAG': 'Q',
	'CGT': 'R',
	'CGA': 'R',
	'CGC': 'R',
	'CGG': 'R',
	'ATT': 'I',
	'ATC': 'I',
	'ATA': 'I',
	'ATG': 'M',
	'ACT': 'T',
	'ACA': 'T',
	'ACC': 'T',
	'ACG': 'T',
	'AAT': 'N',
	'AAC': 'N',
	'AAA': 'K',
	'AAG': 'K',
	'AGT': 'S',
	'AGC': 'S',
	'AGA': 'R',
	'AGG': 'R',
	'GTT': 'V',
	'GTC': 'V',
	'GTA': 'V',
	'GTG': 'V',
	'GCT': 'A',
	'GCC': 'A',
	'GCA': 'A',
	'GCG': 'A',
	'GAT': 'D',
	'GAC': 'D',
	'GAA': 'E',
	'GAG': 'E',
	'GGT': 'G',
	'GGC': 'G',
	'GGA': 'G',
	'GGG': 'G',
	}

	#--------------#Block 4.1: Define codon lists and protein sequence for all frames-----------------------------------------------------------------------

	CodonList_1 = [ ] 
	for x in range(0, len(DNASeq), 3):  
		CodonList_1.append(DNASeq[x:x+3]) 

	ProteinSeq_1 = []
	for codon in CodonList_1:
		if codon in CodonDict:
			ProteinSeq_1.append(CodonDict[codon])
		else:
			break

	CodonList_2 = [ ] 
	for x in range(1, len(DNASeq), 3):  
		CodonList_2.append(DNASeq[x:x+3]) 

	ProteinSeq_2 = []
	for codon in CodonList_2:
		if codon in CodonDict:
			ProteinSeq_2.append(CodonDict[codon])
		else:
			break
		
	CodonList_3 = [ ] 
	for x in range(2, len(DNASeq), 3):  
		CodonList_3.append(DNASeq[x:x+3]) 

	ProteinSeq_3 = []
	for codon in CodonList_3:
		if codon in CodonDict:
			ProteinSeq_3.append(CodonDict[codon])
		else:
			break

	CodonList_r1 = [ ] 
	for x in range(0, len(Reverse), 3):  
		CodonList_r1.append(Reverse[x:x+3]) 

	ProteinSeq_r1 = []
	for codon in CodonList_r1:
		if codon in CodonDict:
			ProteinSeq_r1.append(CodonDict[codon])
		else:
			break

	CodonList_r2 = [ ] 
	for x in range(1, len(Reverse), 3):  
		CodonList_r2.append(Reverse[x:x+3]) 

	ProteinSeq_r2 = []
	for codon in CodonList_r2:
		if codon in CodonDict:
			ProteinSeq_r2.append(CodonDict[codon])
		else:
			break

	CodonList_r3 = [ ] 
	for x in range(2, len(Reverse), 3):  
		CodonList_r3.append(Reverse[x:x+3]) 

	ProteinSeq_r3 = []
	for codon in CodonList_r3:
		if codon in CodonDict:
			ProteinSeq_r3.append(CodonDict[codon])
		else:
			break

	ProteinSeq_1 = ''.join(ProteinSeq_1)
	ProteinSeq_2 = ''.join(ProteinSeq_2)
	ProteinSeq_3 = ''.join(ProteinSeq_3)
	ProteinSeq_r1 = ''.join(ProteinSeq_r1)
	ProteinSeq_r2 = ''.join(ProteinSeq_r2)
	ProteinSeq_r3= ''.join(ProteinSeq_r3)

	#--------#Block 4.2: Define molecular weights for protein sequences in all frames------------------------------------------------------------------------------
	# Including checks for Stop Codons

	Frame_1 = '1'
	for y in ProteinSeq_1:	
		if y == 'X':
			StopCodon = True
			break		
		else:
			StopCodon = False

	if StopCodon == True:
		OutFile.write('Warning: there is a stop codon at position %d of frame %s\r' % (float(ProteinSeq_1.index('X'))+1.0, Frame_1))
	
	if StopCodon == False:

		OutFile.write('Protein sequence in frame 1: %s\r' % ProteinSeq_1)

		MolWeight_1 = 0
		for Aminoacid in ProteinSeq_1:
			MolWeight_1 = MolWeight_1 + AminoDict[Aminoacid]

		OutFile.write("\tMolecular Weight: %.1f\r" % MolWeight_1)

	Frame_2 = '2'

	for y in ProteinSeq_2:	
		if y == 'X':
			StopCodon = True
			break		
		else:
			StopCodon = False

	if StopCodon == True:
		OutFile.write('Warning: there is a stop codon at position %d of frame %s\r' % (float(ProteinSeq_2.index('X'))+1.0, Frame_2))

	if StopCodon == False:

		OutFile.write('Protein sequence in frame 2: %s\r' % ProteinSeq_2)
		MolWeight_2 = 0
		for Aminoacid in ProteinSeq_2:
			MolWeight_2 = MolWeight_2 + AminoDict[Aminoacid]

		OutFile.write("\tMolecular Weight: %.1f\r" % MolWeight_2)

	Frame_3 = '3'

	for y in ProteinSeq_3:	
		if y == 'X':
			StopCodon = True
			break		
		else:
			StopCodon = False

	if StopCodon == True:
		OutFile.write('Warning: there is a stop codon at position %d of frame %s\r' % (float(ProteinSeq_3.index('X'))+1.0, Frame_3))

	if StopCodon == False:

		OutFile.write('Protein sequence in frame 3: %s\r' % ProteinSeq_3)
		MolWeight_3 = 0
		for Aminoacid in ProteinSeq_3:
			MolWeight_3 = MolWeight_3 + AminoDict[Aminoacid]


		OutFile.write("\tMolecular Weight: %.1f\r" % MolWeight_3)
	
	Frame_r1 = 'reverse 1'

	for y in ProteinSeq_r1:	
		if y == 'X':
			StopCodon = True
			break		
		else:
			StopCodon = False

	if StopCodon == True:
		OutFile.write('Warning: there is a stop codon at position %d of frame %s\r' % (float(ProteinSeq_r1.index('X'))+1.0, Frame_r1))
	if StopCodon == False:

		OutFile.write('Protein sequence in frame reverse 1: %s\r' % ProteinSeq_r1)

		MolWeight_r1 = 0
		for Aminoacid in ProteinSeq_r1:
			MolWeight_r1 = MolWeight_r1 + AminoDict[Aminoacid]


		OutFile.write("\tMolecular Weight: %.1f\r" % MolWeight_r1)

	Frame_r2 = 'reverse 2'

	for y in ProteinSeq_r2:	
		if y == 'X':
			StopCodon = True
			break		
		else:
			StopCodon = False

	if StopCodon == True:
		OutFile.write('Warning: there is a stop codon at position %d of frame %s\r' % (float(ProteinSeq_r2.index('X'))+1.0, Frame_r2))

	if StopCodon == False:

		OutFile.write('Protein sequence in frame reverse 2: %s\r' % ProteinSeq_r2)
		MolWeight_r2 = 0
		for Aminoacid in ProteinSeq_r2:
			MolWeight_r2 = MolWeight_r2 + AminoDict[Aminoacid]


		OutFile.write("\tMolecular Weight: %.1f\r" % MolWeight_r2)

	Frame_r3 = 'reverse 3'
	for y in ProteinSeq_r3:	
		if y == 'X':
			StopCodon = True
			break		
		else:
			StopCodon = False

	if StopCodon == True:
		OutFile.write('Warning: there is a stop codon at position %d of frame %s\r\r' % (float(ProteinSeq_r3.index('X'))+1.0, Frame_r3))
	
	if StopCodon == False:

		OutFile.write('Protein sequence in frame reverse 3: %s\r' % ProteinSeq_r3)

		MolWeight_r3 = 0
		for Aminoacid in ProteinSeq_r3:
			MolWeight_r3 = MolWeight_r3 + AminoDict[Aminoacid]


		OutFile.write("\tMolecular Weight: %.1f\r\r" % MolWeight_r3)

InterFile.close()
OutFile.close()