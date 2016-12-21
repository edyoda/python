'''
x = lambda y : y + y 

def fun(x):
    return x + x

print x(7)

y = lambda x,y: x+y

print y(4,6)
'''

#Function which returns a function
'''
def funcGenerator(x):
	return lambda y: y**x

f = funcGenerator(3) # f is a function which takes one arg & returns cube of it
g = funcGenerator(4) # g is a function which takes one arg & return ^4 of it

print f(5)
print g(5)
'''
'''
l = [ [4,32], [1,2], [33,1] ]
print sorted(l,key=lambda x: x[1])
print sorted(l, cmp=(lambda x,y:cmp(x[0],y[0])))
'''
#List Compreshension
l = [ x*2 for x in range(5) if x%2 == 0]
print l