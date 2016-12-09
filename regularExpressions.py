import re

s = 'h peeeeeeellloooo heeeeee'

var = re.search (r'h\s*\w\w\w', s)

if var :
	print var.group()



# str = 'an example word:cat!!'
# match = re.search(r'word:\w\w\w', str)
# # If-statement after search() tests if it succeeded
# if match:                      
#     print 'found', match.group() ## 'found word:cat'
# else:
#     print 'did not find'


# str = 'an example word:cat!!'
# match1 = re.match(r"word:\w\w\w!!", "hello")
# # If-statement after search() tests if it succeeded
# if match1:                      
#     print 'found', match1.group() ## 'found word:cat'
# else:
#     print 'did not find'