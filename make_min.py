import json

with open('data.json') as f:
	data = json.load(f)

out = {k: [
	v['name'],
	v['capital'].get('name'),
	v['flag']['colors'],
	v['flag']['desc'],
	v['location']['continents']
] for k, v in data.items()}

with open('min_data.json', 'w') as f:
	json.dump(out, f)
