def p_decorate(func):
   
   #Function inside a function
   def func_wrapper(name):
       print func('Mac')
       return "Great Stuff - p"

   return func_wrapper

def q_decorate(func):
   
   #Function inside a function
   def func_wrapper(name):
       print func('Mac')
       return "Great Stuff - q"

   return func_wrapper

@p_decorate
@q_decorate
def get_text(name):
   return "Hello World " + name

print get_text("John")