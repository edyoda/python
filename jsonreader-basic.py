import json

def printMenuItem(db):
	for k,v in db.items():
		if isinstance(v,dict):
			printMenuItem(v)
		else:
			print k, ' : ', v

def parseInt(x):
	print 'Hello' + x
	return int(x)+1

def parseConst(x):
	print 'Cost ' + x
	return x

with open('file.json') as fd:
	doc = json.loads(fd.read(),parse_int=parseInt,parse_constant=parseConst)

printMenuItem(doc)