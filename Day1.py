print ('hello world')
#Dynamically Typed Programming language
a = 1
b = 2

print (type(a))

a = 'hello'

print (type(a))

a = 9381902389183109831823091830912839012 * 7281273192738127391827318973
print (a)

a = 100
b = 20

print (a/b)
print (a**b)

s = 'hello world'
print (s+s)
print ('\n\n')
print (s * 5)
print (s[-1])

print (s[2:6])
print (s[::-1])


s = 'the great hello great world'

### String Functions
print (s.count('o'))

print (s.capitalize())

print (s.center(100))

print (s.count(' '))

print (s.endswith('d'))

print (s.startswith('t'))

print (s.find('great',5))

print (s.index('great',8))

s = 'Mr/Mrs {name}, Congrats for getting {percent}% hike'
print (s.format(name='abc',percent=2))
print (s.format(name='asamkeerth',percent=422))