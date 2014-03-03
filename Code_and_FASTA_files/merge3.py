#!/usr/bin/env python
import sys
import re

OutFileName = raw_input('Output file name?')
OutFile = open(OutFileName, 'w')
FileList = sys.argv[1:]
TotalFiles = len(FileList)

FileNumber = 1
MasterList = []

for InFileName in FileList:
	InFile = open(InFileName, 'r')
	LineNumber = 0
	RecordNum = 0

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
		if FileNumber == 1:
			MasterList.append(Line)
		elif FileNumber == TotalFiles:
			Elements = Line.split('\t')
			MasterList[RecordNum] += (Elements[1])
			MasterList[RecordNum] += ('\r')
			RecordNum += 1	
		else:
			Elements = Line.split('\t')
			MasterList[RecordNum] += (Elements[1])
			RecordNum += 1
		LineNumber += 1
	InterFile.close()
	FileNumber += 1

MasterList = ''.join(MasterList)
OutFile.write(MasterList)
	
#print MasterList
