
def func(args):
    print args
    print 'hello world'
    return args, 77

a = func('hello')
print a

'''
#default arguments
def newFunc(arg='abc',arg1):
    print 'Hello, How are you ',arg, arg1

newFunc(44)
newFunc(55)
newFunc(66,'Awi')


def func(name,age,location):
    print name,age,location

func(age=33,location='mumbai',name='awa')
'''
'''
def func(*vargs):
    print vargs[1] * vargs[3]

func('abc',44,'def',90)
#func('xyz')
'''
#l = [1,2,3,4,5]
'''
def revpacking(name,age,location):
    print name,age,location


l = ['awi',77,'blore']
revpacking(*l)
'''
'''
def fun(name,*subjects):
    print 'hello %s' %name
    res = ''
    for i in subjects:
        res = res + ' ' + str(i)
    print 'thanks for attending subjects,', res 

fun('abc',34,67,23)
fun('def',55,66)
'''
'''
def func(name,age,location):
    print name,age,location

db = {'name':'abc','age':33, 'location':'bangalore'}

func(**db)

def kwargsfunc(**kwargs):
    if 'age' in kwargs:
        print kwargs['age']

kwargsfunc(name='awantik',age=20)
'''
'''
def kfunc(name,*marks,**location):
    print name
    print marks
    print location

#kfunc('awantik', 33,44,55, comp='abc',age=44)
kfunc('awantik', 33,44,55,34,43,56)
'''
'''
print 'a' in 'abcd'
print 'a' in ['a','b','c']
db = {'a':'awantik', 'b':'bawa', 'c':'cat'}
if 'a' in db:
    print 'yess'
else:
    print 'not there'
'''
'''
l = range(10,100,5)
print len(l), max(l), sum(l)

for d in l[5:]:
    print d

for x in range(len(l)):
    l[x] -=2

print l

for idx,data in enumerate(l):
    print idx,data

x = enumerate(l)
print x.next()
print x.next()
'''
'''
def func():
    i = 0
    while True:
        i += 1
        yield i

f = func()
print f
print f.next()
print f.next()
print f.next()
print f.next()
'''

#lambda - Annonymous functions
'''
f = lambda x: x + 5
g = lambda x,y: x + y

print f(8)
print g(9,19)
l = [ ['awa',33], ['bwa',11] ]

print sorted(l,cmp= lambda x,y: cmp(x[0],y[0]))
'''

#Function that generates function

def funGenerator(num):
    return lambda x: x**num

f = funGenerator(2) # lambda x: x**2
g = funGenerator(3) # lambda x: x**3
h = funGenerator(4) #

print f(4)
print g(4)
print h(4)


#Functional Programming
'''
def fun(x):
    return x*2

l = [1,2,3,3,4,4,5,56,9]

print map(float,l)
print map(fun,l)
print map(lambda x:x**2,l)

print filter(lambda x: x%2 ==0,l)

print reduce(lambda x,y: x+y,l)
'''
'''
class Base:
    pass

b = Base()
b.name = 'awantik'
b.gender = 'M'

print b.__dict__
print b.name
'''
'''
class Base:
     
    address = 'abc'

    def __init__(self,name,gender):
        self.__name = name
        self.gender = gender

    def someinfo(self,location):
        #self.location
        print self

    @staticmethod
    def staticSomeInfo(name,age):
        Base.address = name

b = Base('awantik','male')
print b.__dict__

b.someinfo('bangalore')

print b.address

Base.staticSomeInfo('awantik',44)
print b._Base__name

class Derived(Base):
    def Happy(self):
        print 'happy time'


d = Derived('abc',87)
d.Happy()
d.someinfo('bangalore')
'''
'''
class Base:
    def __init__(self,**kwargs):
        for k,v in kwargs.items():
            print k,v
            if k == 'age':
                self.age = v
            if k == 'name':
                self.name = v

b = Base(name='Awantik',age=40)
print b.__dict__
b = Base(name='newguy')
print b.__dict__

class Derived(Base):
    pass

d = Derived()

a = []
if type(a) == list:
    print 'List it is'

print isinstance(d,Base)
'''

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __eq__(self,obj):
        return self.name == obj.name and self.age == obj.age

    def __le__()

p1 = Person('awantik',79)
p2 = Person('awantik',79)

#p2 = p1

print id(p1),  id(p2)

if p1 == p2:
    print 'same'

#print p1.__dict__
#print p2.__dict__



        




