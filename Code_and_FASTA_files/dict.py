#!/usr/bin/env python
import sys

FileList = sys.argv[1:]
name_list = []

for element in FileList:
	seq_name = element.replace(".fasta","")
	name_list.append(seq_name)
	globals()[seq_name] = {}
	
for x in name_list:
	print globals()[x]









	