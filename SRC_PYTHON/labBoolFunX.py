# Zachary Job

# labBoolFun 15 oct 2012

# Step 1. 

# Implement the following.  

def combs(n):
    if n == 1:
        return [[0],[1]]
    else:
        return map(lambda i: i+[0], combs(n-1))+map(lambda i: i+[1], combs(n-1))

def func0(x,y,z):
    return x and (y or z)

def func0table():
    return map(lambda x: (x, func0(x[0], x[1], x[2])), combs(3))

def showTable(lst):
    if lst == []: return None
    else:
        print lst[0][0], lst[0][1]
        showTable(lst[1:])

def func0alt(x,y,z):
    return ( (x and not y and z)
             or (x and y and not z)
             or (x and y and z) )

def func0test():
    m= map(lambda x: (x, func0(x[0], x[1], x[2])), combs(3))
    n= map(lambda x: (x, func0alt(x[0], x[1], x[2])), combs(3))
    if m != n: return False
    return True

def func1(x,y):
    return x or (y and x)

def func1table():
    return showTable(map(lambda x: (x, func1(x[0], x[1])), combs(2)))

def func1alt(x,y):
    return ((x and not y) or (x and y))

def func1test():
    m= map(lambda x: (x, func1(x[0], x[1])), combs(2))
    n= map(lambda x: (x, func1alt(x[0], x[1])), combs(2))
    if m != n: return False
    return True

