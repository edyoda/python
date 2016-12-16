'''
def fun(l):
    h = 0
    try:
        #Try doing things here, if unsuccessful go to except
        print h
        print l[1]
        return
    except Exception as e:
        print e
    finally:
        print 'Finally here'

    print 'hello'

fun("jsd")
'''
'''
def func(d):
    try:
        print d.index('d')
    except:
        print 'Cant doing'

func("abc")
'''
'''
def func(d):
    print d.index('d')

func("abc")
'''


