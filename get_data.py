import os, urllib2

if not os.path.exists('data'):
    os.makedirs('data')

def dl_file(url, f_name):
   req = urllib2.Request(url)
   response = urllib2.urlopen(req)
   text = response.read()
   with open(f_name, 'w') as f:
       f.write(text)

dl_file('https://data.cityofnewyork.us/api/views/43nn-pn8j/rows.csv?accessType=DOWNLOAD',
        'data/doh_inspections.csv')
dl_file('https://data.cityofnewyork.us/api/views/w7w3-xahh/rows.csv?accessType=DOWNLOAD',
        'data/lob.csv')
