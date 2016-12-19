# '''
# w = ['abc','def','ghi']
# l = []
# for e in w:
#   l.append(e)
# print set(l)
# '''

# l = [1,2,3]
# m = [4,5,6]
# x = 'abcd'
# l.extend(x)
# for i in l:
#   print i,
'''
class MyStuff:
    
    INFO = 10

    @staticmethod
    def staticfunction():
        print 'This is static function'


MyStuff.staticfunction()
print MyStuff.INFO
'''
'''
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def __eq__(self,obj):
        if self.name == obj.name and self.age == obj.age:
            return True
        else:
            return False

    def __hash__(self):
        return hash(self.name)+hash(self.age)

    def __repr__(self):
        return self.name + ' ' + str(self.age)

s1 = Student('awi',44)
s2 = Student('awi',54)

print s1 == s2
print cmp(s1,s2)


db = {s1:'awi',s2:'bwi'}
print db[s1]

class Info:
    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return self.name

    def __eq__(self,obj):
        if self.name == obj.name:
            return True
        else:
            return False

    def __hash__(self):
        return hash(self.name)

s = set([Info('awi'),Info('awi')])
print s
'''
'''
class Base:
    def __init__(self,name,age):
        self.__name = name
        self._age = age

    def func(self,somename):
        self.__name = somename

b = Base('awantik',44)
b.func('awi')
#print b._Base__name
print b._age
'''
'''
class Base:
    def __init__(self,name):
        self.name = name
        print 'Base'

    def enjoy(self):
        print 'Enjoy in base'


class Derived(Base):
    def __init__(self,name,age):
        self.age = age
        Base.__init__(self,name)
        print 'Derived'

    def enjoy(self):
        #Base.enjoy(self)
        print 'Enjoy in derived'

b = Base('awa')
b = Derived('awi',66)
#print d.__dict__
#d.enjoy()
b.enjoy()
'''

from abc import ABCMeta,abstractmethod

class MyABC:
    __metaclass__ = ABCMeta

    @abstractmethod
    def absmethod(self):
        pass

class DerABC(MyABC):
    def absmethod(self):
        print 'Hello World'

b = DerABC()
b.absmethod()

print type(b) == MyABC
print isinstance(b,MyABC)
print isinstance(b,DerABC)