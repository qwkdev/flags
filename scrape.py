import json
import os
import time

import requests as rq

TOKEN = input('Token: ')

def get(cc: str):
	r = rq.get('https://api.restcountries.com/countries/v5?codes.alpha_2='+cc, headers={'Authorization': 'Bearer '+TOKEN})
	if r.status_code == 429:
		print('\nWaiting...')
		time.sleep(10)
		r = rq.get('https://api.restcountries.com/countries/v5?codes.alpha_2='+cc, headers={'Authorization': 'Bearer '+TOKEN})
	return r

cn = 0

with open('data.json') as f:
	data = json.load(f)

for fn in os.listdir('svg'):
	if os.path.isfile(os.path.join('svg', fn)):
		print(cn, end='\r', flush=True)

		cc = fn.split('.svg')[0]
		if cc in data:
			cn += 1
			continue

		r = get(cc).json()['data']['objects']
		if len(r) > 1: raise ValueError(cc)
		if not r:
			print('\nError on', cc)
			data[cc] = 'Error'
			continue
		r = r[0]
		
		data[cc] = {
			'name': r['names']['common'],
			'capital': {},
			'flag': {
				'colors': [
					r['flag']['colors']['prominent'],
					r['flag']['colors']['dominant']
				],
				'desc': r['flag']['description']
			},
			'location': {
				'region': r['region'],
				'subregion': r['subregion'],
				'continents': r['continents'],
				'coords': [r['coordinates']['lat'], r['coordinates']['lng']],
				'borders': r['borders'],
				'landlocked': r['landlocked'],
				'area': r['area']['kilometers']
			},
			'languages': [[i['iso639_1'], i['name']] for i in r['languages']],
			'timezones': r['timezones']
		}

		for capital in r['capitals']:
			if capital['attributes']['primary']:
				data[cc]['capital'] = {
					'name': capital['name'],
					'coords': [capital['coordinates']['lat'], capital['coordinates']['lng']]
				}

		with open('data.json', 'w') as f:
			json.dump(data, f)

		time.sleep(1)

		cn += 1

parse3 = {'UNK': 'XK', 'AFG': 'AF', 'ALB': 'AL', 'DZA': 'DZ', 'ASM': 'AS', 'AND': 'AD', 'AGO': 'AO', 'AIA': 'AI', 'ATA': 'AQ', 'ATG': 'AG', 'ARG': 'AR', 'ARM': 'AM', 'ABW': 'AW', 'AUS': 'AU', 'AUT': 'AT', 'AZE': 'AZ', 'BHS': 'BS', 'BHR': 'BH', 'BGD': 'BD', 'BRB': 'BB', 'BLR': 'BY', 'BEL': 'BE', 'BLZ': 'BZ', 'BEN': 'BJ', 'BMU': 'BM', 'BTN': 'BT', 'BOL': 'BO', 'BES': 'BQ', 'BIH': 'BA', 'BWA': 'BW', 'BVT': 'BV', 'BRA': 'BR', 'IOT': 'IO', 'BRN': 'BN', 'BGR': 'BG', 'BFA': 'BF', 'BDI': 'BI', 'CPV': 'CV', 'KHM': 'KH', 'CMR': 'CM', 'CAN': 'CA', 'CYM': 'KY', 'CAF': 'CF', 'TCD': 'TD', 'CHL': 'CL', 'CHN': 'CN', 'CXR': 'CX', 'CCK': 'CC', 'COL': 'CO', 'COM': 'KM', 'COD': 'CD', 'COG': 'CG', 'COK': 'CK', 'CRI': 'CR', 'HRV': 'HR', 'CUB': 'CU', 'CUW': 'CW', 'CYP': 'CY', 'CZE': 'CZ', 'CIV': 'CI', 'DNK': 'DK', 'DJI': 'DJ', 'DMA': 'DM', 'DOM': 'DO', 'ECU': 'EC', 'EGY': 'EG', 'SLV': 'SV', 'GNQ': 'GQ', 'ERI': 'ER', 'EST': 'EE', 'SWZ': 'SZ', 'ETH': 'ET', 'FLK': 'FK', 'FRO': 'FO', 'FJI': 'FJ', 'FIN': 'FI', 'FRA': 'FR', 'GUF': 'GF', 'PYF': 'PF', 'ATF': 'TF', 'GAB': 'GA', 'GMB': 'GM', 'GEO': 'GE', 'DEU': 'DE', 'GHA': 'GH', 'GIB': 'GI', 'GRC': 'GR', 'GRL': 'GL', 'GRD': 'GD', 'GLP': 'GP', 'GUM': 'GU', 'GTM': 'GT', 'GGY': 'GG', 'GIN': 'GN', 'GNB': 'GW', 'GUY': 'GY', 'HTI': 'HT', 'HMD': 'HM', 'VAT': 'VA', 'HND': 'HN', 'HKG': 'HK', 'HUN': 'HU', 'ISL': 'IS', 'IND': 'IN', 'IDN': 'ID', 'IRN': 'IR', 'IRQ': 'IQ', 'IRL': 'IE', 'IMN': 'IM', 'ISR': 'IL', 'ITA': 'IT', 'JAM': 'JM', 'JPN': 'JP', 'JEY': 'JE', 'JOR': 'JO', 'KAZ': 'KZ', 'KEN': 'KE', 'KIR': 'KI', 'PRK': 'KP', 'KOR': 'KR', 'KWT': 'KW', 'KGZ': 'KG', 'LAO': 'LA', 'LVA': 'LV', 'LBN': 'LB', 'LSO': 'LS', 'LBR': 'LR', 'LBY': 'LY', 'LIE': 'LI', 'LTU': 'LT', 'LUX': 'LU', 'MAC': 'MO', 'MDG': 'MG', 'MWI': 'MW', 'MYS': 'MY', 'MDV': 'MV', 'MLI': 'ML', 'MLT': 'MT', 'MHL': 'MH', 'MTQ': 'MQ', 'MRT': 'MR', 'MUS': 'MU', 'MYT': 'YT', 'MEX': 'MX', 'FSM': 'FM', 'MDA': 'MD', 'MCO': 'MC', 'MNG': 'MN', 'MNE': 'ME', 'MSR': 'MS', 'MAR': 'MA', 'MOZ': 'MZ', 'MMR': 'MM', 'NAM': 'NA', 'NRU': 'NR', 'NPL': 'NP', 'NLD': 'NL', 'NCL': 'NC', 'NZL': 'NZ', 'NIC': 'NI', 'NER': 'NE', 'NGA': 'NG', 'NIU': 'NU', 'NFK': 'NF', 'MKD': 'MK', 'MNP': 'MP', 'NOR': 'NO', 'OMN': 'OM', 'PAK': 'PK', 'PLW': 'PW', 'PSE': 'PS', 'PAN': 'PA', 'PNG': 'PG', 'PRY': 'PY', 'PER': 'PE', 'PHL': 'PH', 'PCN': 'PN', 'POL': 'PL', 'PRT': 'PT', 'PRI': 'PR', 'QAT': 'QA', 'ROU': 'RO', 'RUS': 'RU', 'RWA': 'RW', 'REU': 'RE', 'BLM': 'BL', 'SHN': 'SH', 'KNA': 'KN', 'LCA': 'LC', 'MAF': 'MF', 'SPM': 'PM', 'VCT': 'VC', 'WSM': 'WS', 'SMR': 'SM', 'STP': 'ST', 'SAU': 'SA', 'SEN': 'SN', 'SRB': 'RS', 'SYC': 'SC', 'SLE': 'SL', 'SGP': 'SG', 'SXM': 'SX', 'SVK': 'SK', 'SVN': 'SI', 'SLB': 'SB', 'SOM': 'SO', 'ZAF': 'ZA', 'SGS': 'GS', 'SSD': 'SS', 'ESP': 'ES', 'LKA': 'LK', 'SDN': 'SD', 'SUR': 'SR', 'SJM': 'SJ', 'SWE': 'SE', 'CHE': 'CH', 'SYR': 'SY', 'TWN': 'TW', 'TJK': 'TJ', 'TZA': 'TZ', 'THA': 'TH', 'TLS': 'TL', 'TGO': 'TG', 'TKL': 'TK', 'TON': 'TO', 'TTO': 'TT', 'TUN': 'TN', 'TKM': 'TM', 'TCA': 'TC', 'TUV': 'TV', 'TUR': 'TR', 'UGA': 'UG', 'UKR': 'UA', 'ARE': 'AE', 'GBR': 'GB', 'UMI': 'UM', 'USA': 'US', 'URY': 'UY', 'UZB': 'UZ', 'VUT': 'VU', 'VEN': 'VE', 'VNM': 'VN', 'VGB': 'VG', 'VIR': 'VI', 'WLF': 'WF', 'ESH': 'EH', 'YEM': 'YE', 'ZMB': 'ZM', 'ZWE': 'ZW', 'ALA': 'AX'}
def p3(a3, d):
	if a3 in parse3:
		return parse3[a3].lower()
	print('Error', a3, d)

errors = {
	'ab': {
		"name": "Scotland",
		"capital": {
			"name": "Edinburgh",
			"coords": [55.9, -3.2]
		},
		"flag": {
			"colors": ["#005eb8", "#ffffff"],
			"desc": "The flag of Scotland is the Saltire, a white diagonal cross on a blue field, said to have appeared in the sky in 832 AD after St Andrew, Scotland's patron saint."
		},
		"location": {
			"region": "Europe",
			"subregion": "Northern Europe",
			"continents": ["Europe"],
			"coords": [57, -4],
			"borders": ["en"],
			"landlocked": False,
			"area": 80231
		},
		"languages": [["en", "English"]],
		"timezones": ["UTC", "UTC+01:00"]
	},
	'en': {
		"name": "England",
		"capital": {
			"name": "London",
			"coords": [51.5, -0.1]
		},
		"flag": {
			"colors": ["#ffffff", "#ce1124"],
			"desc": "The flag of England is the St George's Cross, a red cross on a white field, named for England's patron saint."
		},
		"location": {
			"region": "Europe",
			"subregion": "Northern Europe",
			"continents": ["Europe"],
			"coords": [52, -1],
			"borders": ["ab", "wl"],
			"landlocked": False,
			"area": 132932
		},
		"languages": [["en", "English"]],
		"timezones": ["UTC", "UTC+01:00"]
	},
	'wl': {
		"name": "Wales",
		"capital": {
			"name": "Cardiff",
			"coords": [51.5, -3.2]
		},
		"flag": {
			"colors": ["#00ab39", "#d21034"],
			"desc": "The flag of Wales is the red dragon on a green and white field, a symbol of Welsh sovereignty since the medieval period."
		},
		"location": {
			"region": "Europe",
			"subregion": "Northern Europe",
			"continents": ["Europe"],
			"coords": [52, -5],
			"borders": ["en"],
			"landlocked": False,
			"area": 21218
		},
		"languages": [["en", "English"]],
		"timezones": ["UTC", "UTC+01:00"]
	}
}

for i in data:
	if data[i] == 'Error': data[i] = errors[i]
	else: data[i]['location']['borders'] = [p3(j, data[i]) for j in data[i]['location']['borders']]

with open('data.json', 'w') as f:
	json.dump(data, f)

print()

