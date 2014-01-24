#! /usr/bin/env python

# Alanine	GCA, GCC, GCG, GCT
# Asparagine	AAC, AAT, GAC, GAT
# Cysteine	TGC, TGT
# Aspartic acid	GAC, GAT
# Glutamic acid	GAA, GAG
# Phenylalanine	TTC, TTT
# Glycine	GGA, GGC, GGG, GGT
# Histidine	CAC, CAT
# Isoleucine	ATA, ATC, ATT
# Lysine	AAA, AAG
# Leucine	CTA, CTC, CTG, CTT, TTA, TTG
# Methionine	ATG
# Asparagine	AAC, AAT
# Proline	CCA, CCC, CCG, CCT
# Glutamine	CAA, CAG
# Arginine	AGA, AGG, CGA, CGC, CGG, CGT
# Serine	AGC, AGT, TCA, TCC, TCG, TCT
# Threonine	ACA, ACC, ACG, ACT
# Valine	GTA, GTC, GTG, GTT
# Tryptophan	TGG
# Tyrosine	TAC, TAT
# Glutamine or Glutamic acid	CAA, CAG, GAA, GAG
# stop codon	TAA, TAG, TGA
# start codons	AUG, GUG, UUG
#look for start codon
#frame shifting

dct = {"TTT":"Phe","TTC":"Phe","TTA":"Leu","TTG":"Leu","TCT":"Ser","TCC":"Ser", 
"TCA":"Ser","TCG":"Ser", "TAT":"Tyr","TAC":"Tyr","TAA":"Stp","TAG":"Stp", 
"TGT":"Cys","TGC":"Cys","TGA":"Stp","TGG":"Trp", "CTT":"Leu","CTC":"Leu", 
"CTA":"Leu","CTG":"Leu","CCT":"Pro","CCC":"Pro","CCA":"Pro","CCG":"Pro", 
"CAT":"His","CAC":"His","CAA":"Gln","CAG":"Gln","CGT":"Arg","CGC":"Arg", 
"CGA":"Arg","CGG":"Arg", "ATT":"Ile","ATC":"Ile","ATA":"Ile","ATG":"Met", 
"ACT":"Thr","ACC":"Thr","ACA":"Thr","ACG":"Thr", "AAT":"Asn","AAC":"Asn", 
"AAA":"Lys","AAG":"Lys","AGT":"Ser","AGC":"Ser","AGA":"Arg","AGG":"Arg", 
"GTT":"Val","GTC":"Val","GTA":"Val","GTG":"Val","GCT":"Ala","GCC":"Ala", 
"GCA":"Ala","GCG":"Ala", "GAT":"Asp","GAC":"Asp","GAA":"E|Glu", 
"GAG":"Glu","GGT":"Gly","GGC":"Gly","GGA":"Gly","GGG":"Gly"}


#check that bases are correct
def check_bases(DNA_sequence):
	y = True #is setting the variable
	bases = ['A','T','C','G','U']
	for x in DNA_sequence:
		for z in bases:
			if x not in bases: #and/or
				y = False
				break
	return y
#end of function 

#pass a range value to the function and the base, return amino acid and print the base
def return_aminos(bases,range_value): #pass a value to a function
	bases = [a[x:x+3] for x in range(range_value,len(a), 3)]
	print bases
	aminos = []
	for b in bases:
		if len(b) == 3:
			aminos.extend(dct[b]+"-")
			if dct[b] == 'Stp':
				print "stop codons identified in sequence"
			all_aminos =  ''.join(aminos)
	return all_aminos[:-1]
#end of function

#opens file; make sure all that you want to print is below this line, functions above
filename = "primers.txt"
file = open(filename, 'r')

#creates an outfile <== TODO modify to print to file
outfilename = filename + "_modified.txt"
outfile = open(outfilename, 'w') ##outfile

#strips new line and splits on tab
#TODO import from fasta file, have fasta to work with?
for Line in file:
	Line = Line.strip('\n')
	element = Line.split('\t')
	
#looks at first element in file row
	a = element[0]
	a = a.upper().replace(" ","")
	if check_bases(a) == True:
		for r in range(3):
			print return_aminos(a,r)
	else:
		print "error in sequence %s" % a
		
#closes the files opened at the beginning
file.close()
outfile.close()
