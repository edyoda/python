#Take strings from user & print back the ones which start with 'a'
'''
while True:
	data = raw_input('Enter Data ')
	if not data:
		break
	if data.startswith('a'):
		print data
'''

#Take lines from user & print back only those which contains 'the' in it
'''
while True:
	line = raw_input('Enter Data ')
	if not line:
		break
	if 'the' in line:
		print line
'''

#Check if user data is less than 10, between 10-50, greater than 50
'''
while True:
	data = raw_input('Enter Number ')
	if not data:
		break
	if not data.isdigit():
		continue
	num = int(data)
	if num < 10:
		s = 'Num {num} less than 10'
		print s.format(num=num)
	elif num < 50:
		s = 'Num {num} less than 50 greater than 10'
		print s.format(num=num)
	else:
		s = 'Num {num} greater than 50'
		print s.format(num=num)
'''