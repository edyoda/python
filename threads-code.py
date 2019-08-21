# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import threading

db = {}

def sayHello():
    return "Hello"

def sayHey():
    return "Hey"

def thread_function(idx,info):
    print ('Function {name} {info}'.format(name=idx, info=info))

    db[idx] = True

    if idx % 2 == 0:
        print (sayHello())
    else:
        print (sayHey())
        
        
def other_thread_functions(idx,info):
    print ('Some other functions')
    db[idx] = True

if __name__ == "__main__":

    threads = []

    for i in range(5):
        x = threading.Thread(target=thread_function, args=(i,"Information"))
        threads.append(x)
        
    for i in range(5,8):
        x = threading.Thread(target=other_thread_functions, args=(i,"Information"))
        threads.append(x)

    
    for thread in threads:
        thread.start()
        thread.join()

    print (db)