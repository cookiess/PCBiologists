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

#list of lists?
#look for start codon
#frame shifting
#reading from a file

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
"GAG":"Glu","GGT":"Gly","GGC":"Gly","GGA":"Gly","GGG":"Gly", "RGA":"unknown"}

#iterates through a text file and takes first element

#opens file
filename = "primers.txt"
file = open(filename, 'r')

#strips new line and splits on tab
for Line in file:
	Line = Line.strip('\n')
	element = Line.split('\t')
	
#looks at first element in file row
	a = element[0]
	
#modifies list to be a range starting with first element and containing every 3
	bases = [a[x:x+3] for x in range(0,len(a), 3)]
	print bases

#converts to amino acids ====TODO put this in a function	
	aminos = []
	for b in bases:
		if len(b) == 3:
			aminos.extend(dct[b]+"-")
	all_aminos =  ''.join(aminos)
	print all_aminos[:-1]
	
#closes the file opened at the beginning
file.close()
