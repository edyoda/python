class ClassName:
	'Optional description'
	var1 = 0

	def __init__(self, name, id):
		self.name = name
		self.id= id

	def method1(self):
		
		print 'this is method 1'
		

obj1 = ClassName("ABC", 2)
obj1.method1()
print ClassName.var1


obj1.age = 4
obj1.address= 'street'
del obj1.age

del ClassName.var1

print (hasattr(obj1, 'age'))
print getattr(obj1, 'address')
setattr(obj1, 'age', 'xyz')
delattr(obj1, 'age')
print (hasattr(obj1, 'age'))

print ClassName.__doc__
print ClassName.__name__
print ClassName.__bases__
print ClassName.__dict__
print ClassName.__module__

class ChildClass (ClassName):
	'Inheriting class ClassName'
	var2 = 5
	__secretNum = 6
	def __init__(self):

		print ' this is child class constructor'

	def method2(self, name):
		print name

	def method1(self):
		print 'this is child class method1'	

	
			

c = ChildClass()
c.method2("XYZ")
c.method1()
print c._ChildClass__secretNum



class Vehicle :

	def calcSpeed(self) :    

		print 'hi'


c= Vehicle()
c.calcSpeed()





























