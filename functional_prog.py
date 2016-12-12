'''
#pass function to function
def my_func(f,data):
	return f(data)

print my_func(lambda x: x*2, 5)

#Sort list based on number
l = [ ('awi',33), ('zwi',22), ('bqi',11) ]
print sorted(l, key=lambda x: x[1])
print sorted(l, cmp=lambda x,y: cmp(x[0],y[0]))
'''
'''
l = [1,2,3,4,5,65,7,7]
print map(lambda x: x*x, l)

l = [ ('awi',33), ('zwi',22), ('bqi',11) ]
print map( lambda x: x[0], l)

db = {'a':1,'b':2,'c':3,'d':4}
print db.values()
print map(lambda x:x[1], db.items())

s = '1 2 3 4 5'
print map( int ,s.split())
'''
l = [ (1,2), (4,6), (2,9), (5,9), (2,3) ]

#print filter(lambda x: x[0] > 5 or x[1] > 5, l)  
#print filter(lambda x: max(x) > 5, l)

m = [1,2,3,4]
def fun(x,y):
	print x,y


print reduce(lambda x,y: (x[0] +y[0], x[1]+y[1]),l)
#print reduce(fun,l)


