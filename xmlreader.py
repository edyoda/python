import xmltodict

with open('test.xml') as fd:
	doc = xmltodict.parse(fd.read())
	
print doc['mydocument']['plus']['@a']
print doc['mydocument']['@has']