# CS 115 Homework 2 
# ...your name...
# ...date created or revised...

# Implement the following functions using map and reduce.
# You will probably need to write additional functions to help.


def shriek(strs):
    """Assume strs is a non-empty list of strings.  Return a list of
    the same strings but with ! suffix.  See example below."""
    return map(strAdd, strs)

def catenate(strs):
    """Assume strs is a list of strings.  Return a single string of their catenation"""
    return ''.join(strs)

def catSpace(strs):
    """Assume strs is a list of strings.  Return their catenation, but with one space between each one."""
    return ' '.join(strs)

def strAdd(x):
    return '!'+x

