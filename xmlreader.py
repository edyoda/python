import xmltodict

with open('test.xml') as fd:
	doc = xmltodict.parse(fd.read())
	
print doc['mydocument']['plus']['@a']
print doc['mydocument']['@has']
for m in doc['mydocument']['and']['many']:
	print m