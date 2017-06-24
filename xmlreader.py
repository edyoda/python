import xmltodict

with open('test.xml') as fd:
	doc = xmltodict.parse(fd.read()) #Convert string of xml content to xml
	
print doc['mydocument']['plus']['@a']
print doc['mydocument']['@has']
for m in doc['mydocument']['and']['many']:
	print m