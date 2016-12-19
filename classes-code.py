#Class is user defined data-type
#Creating an empty class
#Class doesn't occupy memory
'''
class Student:
	pass

	def __init__(self):
		print 'Calling now'

#s1 is ab object of empty class
s1 = Student()
s1.name = "awantik"
print s1
s2 = Student()
print s2
s2.age = 99
print s1.__dict__
print s2.__dict__
'''

class Student:
	pass

	def __init__(self,loc,age):
		self.loc = loc
		self.age = age
		print 'Calling now'

#s1 is ab object of empty class
s1 = Student('Delhi',88)
print s1
s2 = Student('Mumbai',99)
print s2
print s1.__dict__
print s2.__dict__

