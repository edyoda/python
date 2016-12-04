import json

def printMenuItem(db,pattern):
	for k,v in db.items():
		if k == 'menuitem':
			print v
		if isinstance(v,dict):
			printMenuItem(v,pattern)

#executes only one time
with open('jsonfile.json') as fd:
    doc = json.loads(fd.read())

printMenuItem(doc,'menuitem')
