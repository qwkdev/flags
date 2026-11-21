import json

with open('data.json') as f:
	data = json.load(f)

for k in data:
	with open(f'svg/{k}.svg') as f:
		s = f.read()
	with open(f'svg/{k}.svg', 'w') as f:
		f.write(s.replace('<svg ', '<svg preserveAspectRatio="none" '))