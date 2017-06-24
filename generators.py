#Function having yield returns generator
#Using a generator we can iterate through iterable data structure
'''
def gen_func():
    i = 0
    while True:
        #return i
        yield i
        i += 1

f = gen_func() #Return spl. object

print f.next()
print f.next()
print f.next()
print f.next()

for i in range(10):
    print f.next()
'''

#list Comprehension
'''
l = [x*x for x in range(10)]
print l
'''
'''
import random

#random.randint(0,len(m)-1) 

m = ['a','b','c','d','e']
data = [ m[random.randint(0,len(m)-1)] for i in range(100)]
print data
'''

##Decorators
def awi(f):
    print f
    # print func
    # def wrap():
    #     func('Good')

    #wrap('Lord')

@awi("name")
def hello():
    print 'hello '

hello()


