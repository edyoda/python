# try :

# 	f = open("test.txt", "w")
# 	f.write("Hello this is exception example")

# except IOError :
# 	print "Error in writing"

# else :
# 	print "Successfully Written"

# 	f.close()


# try :
# 	f = open("test.txt", "r")
# 	f.write("hello")

# except (IOError , ZeroDivisionError):
# 	print "Error :  cant write into the file"


# else : 
# 	print "Successfully written"
# 	f.close()




# try :
# 	f = open("test.txt", "r")
# 	f.write("hello")
# 	a=5
# 	b=5/0
# except (IOError , ZeroDivisionError):
# 	print "Error :  cant write into the file"
# 	print "Trying to divide by zero"


# else : 
# 	print "Successfully written"
# 	f.close()	




# try :
# 	f = open("test.txt", "r")
# 	f.write("hello")
# 	a=5
# 	b=5/0
# except IOError:
# 	print "Error :  cant write into the file "
# 	print "Trying to divide by zero"
# finally : 
# 	print "Successfully written"
# 	f.close()


# try :
# 	f = open("test.txt", "r")
# 	f.write("hello")
# except IOError, argument  :
# 	print "Error :  cant write into the file :  ", argument
# 	print "Trying to divide by zero"
# finally : 
# 	print "Successfully written"
# 	f.close()



# try :
# 	raise NameError("Hello this is name error exception")
# except NameError:
# 	print "Exception 1"
# 	raise



# class NError (Exception):
# 	def _init_(self, arg):
# 		self.arg=arg

# try :
# 	raise NError(5)

# except NError , e:
	 
# 	print e.arg	


# class MyError(Exception):
#     def __init__(self, value):
#         self.value = value

# try:
#     raise MyError("hello")
# except MyError , e:
#     print 'My exception occurred, value:', e.value




	



