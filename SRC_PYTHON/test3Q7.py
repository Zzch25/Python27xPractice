# Test 3, Fall 2012, Question 7

# YOUR NAME

########################################################################
# Question 7 = 20points
#
# Implement function insert(), using a while-loop.
# Do NOT use recursion, map, or reduce.  
# HINTS: Use function swap().  Check that the given tests work correctly.
# Example:
#   For the list L1 = [2,4,6,7,3,1], the call insert(L0, 4) should
#   shuffle the value 3 leftwards, through the following steps:
#     [2,4,6,7,3,1]
#     [2,4,6,3,7,1]
#     [2,4,3,6,7,1]
#     [2,3,4,6,7,1]
########################################################################

"""def insert(L,i):
    ''' Assume 0 < i and i < len(L) and L[0:i] is sorted.  Modify
    L in place to make L[0:i+1] sorted, by shifting some elements up
    until L[i] ends up in the right place.'''
    temp = len(L[0:i])
    for start in range(temp):
        varI = L[temp - start]
        varB = L[temp - start - 1]
        varA = L[temp - start + 1]
        if varI <= varA and varI >= varB or varI >= varB and varI >= varA:
            return
        elif varI < varB:
            swap(L, temp - start, temp - start - 1)
        elif temp:
            print L
            swap(L, temp + start, temp + start + 1)
    return"""

def insert(L,i):
    ''' Assume 0 < i and i < len(L) and L[0:i] is sorted.  Modify
    L in place to make L[0:i+1] sorted, by shifting some elements up
    until L[i] ends up in the right place.'''
    temp = len(L)
    idx = i
    idxMO = idx-1
    if idx > 1:
        while L[idx] < L[idxMO] and idx != 0:
            swap(L, idx, idx-1)
            idx = idx-1
            idxMO = idx-1
    return

def swap(L, i, j):
    ''' Changes L by swapping the elements at positions i and j.
        Assumes that i and j are in range(0,len(L)).'''
    temp = L[i]
    L[i] = L[j]
    L[j] = temp
        
# tests

L0 = [2,4,6,7,0,1]
insert(L0, 4)
print L0, "should be [0,2,4,6,7,1]"

L1 = [2,4,6,7,3,1]
insert(L1, 4)
print L1, "should be [2,3,4,6,7,1]"

L2 = [2,4,6,7,8,1]
insert(L2, 4)
print L2, "should be [2,4,6,7,8,1]"


########################################################################

