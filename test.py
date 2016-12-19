#!/usr/bin/python
import ctypes
import os

def main():
    d = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    library_path = 'C:\Users\ZekeLabs\Documents\Visual Studio 2015\Projects\MathLibraryAndClient\Debug\MathLibrary.dll'
    lib = ctypes.cdll.LoadLibrary(library_path)

    restype = ctypes.c_int
    argtypes = [ ctypes.c_int ]
    fibonacci_prototype = ctypes.CFUNCTYPE(restype, *argtypes)
    #print lib._FuncPtr
    fibonacci_function = fibonacci_prototype(lib.Fibonacci)

    # term = 10
    # nf = fibonacci_function(term)
    # print('The {}th Fibonacci number is {}'.format(term, nf))


if __name__ == '__main__':
    main()
