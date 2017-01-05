import csv
import json
from collections import OrderedDict

fieldnames = ("ID","Artist","Song", "Artist")

entries = []
#the with statement is better since it handles closing your file properly after usage.
with open('spot.csv', 'r') as csvfile:
    #python's standard dict is not guaranteeing any order, 
    #but if you write into an OrderedDict, order of write operations will be kept in output.
    reader = csv.DictReader(csvfile, fieldnames)
    for row in reader:
        entry = OrderedDict()
        for field in fieldnames:
            entry[field] = row[field]
        entries.append(entry)

output = {
    "Music": entries
}

with open('file.json', 'w') as jsonfile:
    json.dump(output, jsonfile)
    jsonfile.write('\n')