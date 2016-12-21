import json

def printMenuItem(db):
	print db



with open('file.json') as fd:
	doc = json.loads(fd.read())

printMenuItem(doc)