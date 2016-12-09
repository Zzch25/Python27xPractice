import math

def inverse(x):
    return 1.0/x
def e(x):
    L = range(1,x+1)
    M = map(math.factorial, L)
    return sum(map(inverse, M))+1
def error(x):
    return abs(math.e - e(x))
def factorial(x):
    L = range(1, x+1)
    return reduce(multiply, L)
def multiply(x, y):
    return x*y
def add(x, y):
    return x+y
def mean(L):
    return reduce(add, L)/len(L)
        
