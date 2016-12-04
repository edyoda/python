import xmltodict

#executes only one time
with open('file.xml') as fd:
    print 'hello'
    doc = xmltodict.parse(fd.read())

print doc['mydocument']['and']['many']
print doc['mydocument']['@has']
print doc['mydocument']['plus']['#text']