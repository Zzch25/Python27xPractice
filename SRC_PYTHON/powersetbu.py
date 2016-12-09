def powerset(L):
    if L==[]:
        return [[]]
    else:
        theRest = powerset(L[1:])
        return map(lambda x: [L[0]] + x, theRest) + theRest
