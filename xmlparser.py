import xmltodict

def findKeyInfo(db,pattern):
    for k,v in db.items():
            if k == pattern:
                print v
            if isinstance(v,dict):
                findKeyInfo(v,pattern)


pattern = 'many'

#executes only one time
with open('file.xml') as fd:
    doc = xmltodict.parse(fd.read())

findKeyInfo(doc,pattern)