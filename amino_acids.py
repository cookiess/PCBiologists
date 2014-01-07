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


s = "TTTCAATACTAGCATGACCAAAGTGGGAACCCCCTTACGTAGCATGACCCATATATATATATATA"
# for y in range(1):
# 	bases = [s[x:x+3] for x in range(y, len(s) - 2, 3)]
# print bases

bases = [s[x:x+3] for x in range(0,len(s) - 2, 3)]
print bases
print len(s) - 2, 3

aminos = []
for b in bases:
	aminos.extend(dct[b]+"-")
all_aminos =  ''.join(aminos)
print all_aminos[:-1]
