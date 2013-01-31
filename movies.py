import requests
import ipdb
import csv
from json import dumps

ifile  = open('zips.csv', "rb")
reader = csv.reader(ifile)

res = {}

for row in reader:
	print row
	zip = int(row[0])
	
# zip = 48103
	r = requests.get('http://data.tmsapi.com/v1/movies/showings?startDate=2013-02-01&zip='+str(zip)+'&radius=100&api_key=pbsxwvjascgj72kd6rffxpxv')
	r.status_code
	j = r.json()

	res[zip] = j

print res
for z in res:
	print str(z) + '---'
	for m in res[z]:
		print m['title']


f = open('output.json', "wb")
f.write(dumps(res))
f.close()

# ipdb.set_trace()
