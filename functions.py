'''
#Multiple returns
def func(a,b):
	return a + b, a * b

a,b = func(5,10)
print 'hello',a,'world',b
print 'hello %d great %d string %s' % (a,b,'great')

#Packing or Variable arguments function
def vargsFunc(*args):
	for a in args:
		print a,

vargsFunc(1,2,2,'hello',[1,2,2,2])
'''
'''
#default arguments
def func(age,loc='Bangalore',name='Awantik'):
	print age,loc,name

func(87)
'''
'''
#UnPacking
l = ['awantik','zekelabs','python']

def packFunc(name,company,subject):
	print name,company,subject

packFunc(*l)
'''

#Key words based Arguments
'''
def fun(name,address,place):
	print name,address,place

fun(place='bangalore',name='awi',address='office')
'''
'''
db = {'name':'awi','age':90}
def func(name,age):
	print name,age

func(**db)

'''

def func(**kwargs):
	print kwargs

func(name='awi',age=40)
func(loc='bangalore',price=700)