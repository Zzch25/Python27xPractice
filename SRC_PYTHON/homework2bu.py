def letterScore(letter, scorelist):
    if letter == "" or scorelist == "":
        return 0
    elif letter == returnInL(scorelist,0):
        return returnInL(scorelist, 1);
    else:
        return letterScore(letter, scorelist[1:])

def returnInL(L,X):
    M = L[0]
    return M[0+X]

def wordScore(S, scorelist):
    if S == "" or scorelist == "":
        return 0
    else:
        return letterScore(S[0], scorelist) + wordScore(S[1:],scorelist)

def iNeedAList():
    return [ ["a", 1], ["b", 3], ["c", 3], ["d", 2], ["e", 1], ["f", 4], ["g", 2], ["h", 4], ["i", 1], ["j", 8], ["k", 5], ["l", 1], ["m", 3], ["n", 1], ["o", 1], ["p", 3], ["q", 10], ["r", 1], ["s", 1], ["t", 1], ["u", 1], ["v", 4], ["w", 4], ["x", 8], ["y", 4], ["z", 10] ]
