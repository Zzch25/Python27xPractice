#Zachary J, Steven N, Wyatt M.
#9/21/2012

#makeChange(12, [1,2,3,6,12])

def makeChange(N, L):
    """returns the amounts of coins required to effectively return cash"""
    if N == "" or L == []:
        return "Please input a valid entry"
    if N == 0:
        return 0
    if N < 0:
        return max(L)*2
    useIT = 1 + makeChange(N-L[0], L)
    loseIT = makeChange(N, L[1:])
    return min(useIT, loseIT)

#coinID(12, [1,2,3,6,12])

def coinID(N, L):
    """returns appropriate values of coins that fufil value efficiently"""
    if N==0:
        return []
    if L == [] and N > 0 or N < 0:
        return list("x"*10000)
    useIT = [L[0]] + coinID(N-L[0], L)
    loseIT = coinID(N, L[1:])
    if len(useIT) < len(loseIT):
        return useIT
    return loseIT

#giveChange(12, [1,2,3,6,12])

def giveChange(N, L):
    """calls both functions to display coin amount"""
    temp = coinID(N,L)
    return [len(temp),temp] 
