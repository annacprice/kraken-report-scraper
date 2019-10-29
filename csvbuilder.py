#!/usr/bin/env python3

from collections import defaultdict
import csv
import os

dictSpecies = defaultdict(dict)

def csvbuild(input, output):
    txtList = ['species name']
    for txt in os.listdir(input):
        fileExtension = txt.split(".")[-1]
        if fileExtension == "txt":
            txtFile = input + "/" + txt
            txtList.append(txtFile)
	    with open(txtFile, 'r') as file_in:
                csvInput = csv.reader(file_in, delimiter='\t')
                for row in csvInput:
                    dictSpecies[str(row[5])].update({txtFile : int(row[1])})

    with open(output + "/" + "krakensummary.csv", 'wb') as file_out:
        csvOutput = csv.DictWriter(file_out, fieldnames=txtList, restval=0)
        csvOutput.writeheader()
        for name in sorted(dictSpecies.keys()):
            nameValues = dictSpecies[name]
            nameValues['species name'] = name
            csvOutput.writerow(nameValues)
