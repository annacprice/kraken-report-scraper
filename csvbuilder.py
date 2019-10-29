#!/usr/bin/env python3

from collections import defaultdict
import csv
import os

dictSpecies = defaultdict(dict)

def csvbuild(input, output):
    for txt in os.listdir(input):
        fileExtension = txt.split(".")[-1]
        if fileExtension == "txt":
	   txtFile = input + "/" + txt
	   with open(txtFile, 'r') as file_in:
	       csvInput = csv.reader(file_in, delimiter='\t')
               for row in csvInput:
                   dictSpecies[str(row[5])].update({txt : int(row[1])})

    with open(output + "/" + "krakensummary.csv", 'wb') as file_out:
	fieldnames = ['name'] + [txt for txt in os.listdir(input)]
	csvOutput = csv.DictWriter(file_out, fieldnames=fieldnames, restval=0)
	csvOutput.writeheader()
	for name in sorted(dictSpecies.keys()):
	    nameValues = dictSpecies[name]
	    nameValues['name'] = name
	    csvOutput.writerow(nameValues) 
