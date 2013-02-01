import requests
import ipdb
import csv
from json import dumps
from log import logger
from datetime import datetime

ifile  = open('zips.csv', "rU")
reader = csv.reader(ifile) 
output_filep = 'logs/output_' + str(datetime.now()) + '.json' 
logo = logger('log')

logo.log('Output file initiated at: '+ output_filep)

res = {}
c = 1
for row in reader:
	logo.log( '[%d] %s' %(c,row))
	zip = int(row[0])
	c+=1
	try:
	# zip = 48103
		r = requests.get('http://data.tmsapi.com/v1/movies/showings?startDate=2013-01-30&zip='+str(zip)+'&radius=5&api_key=pbsxwvjascgj72kd6rffxpxv')
		r.status_code

		j = r.json()

		res[zip] = j
	except Error as e:
		logo.log('Error with zip code ' + str(zip))
		logo.log('Error log: ' + str(e))

# logo.log( res

for z in res:
	for m in res[z]:
		logo.log( m['title'])

logo.log('Done!... Dumping to file now')
f = open(output_filep, "wb")
f.write(dumps(res))
f.close()

# ipdb.set_trace()
