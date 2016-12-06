'''
from string import maketrans
s = 'hello world this is a nice place'

mapping = maketrans('aeiou',' '*5)
print s.translate(mapping)
'''
'''
l = [ [1,2,3], 3, [4,2,3], [3,2,1], [4,5,6], 3, [7,8,9] ,5]

c = 0
search = 3

for k in l:
    if isinstance(k,list):
        c += k.count(search)
    if isinstance(k,int) and k == search:
        c += 1
print c
'''
'''
l = [ [1,'great',2], [9,'hello',4], 'great']
'''

#Dictionary
#1. 
'''
db = {'a':1,'b':2,'c':3}
for k,v in db.items():
    print k,v

print db.values()
print db.keys()
'''
'''
l = [1,2,3,3,1,1,4]

for e in l:
    if e % 2 == 0:
        print e
'''
'''
### Find count of 3 among all sublists
s = 0
l = [ [1,2],3, [4,3,5,6], [7,8,3,9] ]
for e in l:
    if isinstance(e,list):
        s += e.count(3)
    if e == 3:
        s += 1
print s
'''
'''
###Break the list into two lists, one containing 0th element & other 1st
l = [ ['a',44], ['b',22], ['c',66]]

l1 =[]
l2 = []

for e in l:
    l1.append(e[0])
    l2.append(e[1])
print l1
print l2
'''
'''
###Create a list with max of each sublist
maxlist = []
l = [ [-1,3,1,222], [7,99,3], [55,11,74,3,99,3,3,3,3] ]
for e in l:
    maxlist.append(max(e))
print maxlist

'''
###Remove all the words starting with #
'''
s = "this is a #great world but i m not #sure of staying here for #long, don't know about u"
l = s.split()
for word in l:
    if word.startswith('#'):
        l.remove(word)

print l
'''
###Accessing list by index
'''
l = [1,2,3,3,3,3]
for i in range(len(l)):
    l[i] += l[i]
print l
'''
###Copy list - Deep Copy, Shallow Copy
'''
l = [3,4,5]
m = l #shallow copy - l & m points to same memory
#l[0] = 999
print m 

g = list(l) # deep copy - seperate copy
l[0] = 999
print g,m
'''
'''
l = [1,2,3, [2,3,4]] 
m = list(l)
print m
l[-1][-1] = 'zzzz'
print m,l
'''
'''
###Deep copy for list of lists - deep copy donot copy directly
l = [ [1,2,3], [4,5,6], [7,8,9] ]

m = []
for e in l:
    m.append(list(e))

print m
l [1][1] = 'zzz'
print 'L: ', l
print 'M: ', m

'''

