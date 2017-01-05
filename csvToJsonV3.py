import csv
import json
from collections import OrderedDict

fieldnames = ("ID","Artist","Song", "Artist")

with open('music.csv', 'r') as csvfile, open('file.json', 'w') as jsonfile:
	
	reader = csv.reader(csvfile, fieldnames)
	json.dump({'Muisc': [OrderedDict(zip(fieldnames,r)) for r in reader]}, jsonfile)