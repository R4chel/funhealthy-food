import urllib2

url = "https://data.cityofnewyork.us/api/views/43nn-pn8j/rows.csv?accessType=DOWNLOAD"
req = urllib2.Request(url)
response = urllib2.urlopen(req)
text = response.read()
with open('data/doh_inspections.csv', 'w') as f:
    f.write(text)
