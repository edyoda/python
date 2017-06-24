#Use case of json - exchange data / info among servers
#json & xml are data exchanging mechanisms

import json

with open('file2.json') as fd:
	#x = fd.read()
	doc = json.loads(fd.read()) #Converts a string of json to dictionary

#print doc
print type(doc)
print doc['menu']['']

