import json
import pandas

df = pandas.read_csv('spot.csv', names=("id","Artist","Song", "Album"))

with open('file.json', 'w') as f:
    json.dump({'Music': df.to_dict(orient='records')}, f, indent=4)
