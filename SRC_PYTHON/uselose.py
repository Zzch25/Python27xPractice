#Zachary Job

print "Input a value then a list of change amounts"

#makeChange(12, [1,2,3,6,12])

def makeChange(L, X):
    print [L, X]
    if L == "" or X == []:
        return "Please input a valid entry"
    if L == 0:
        return 0
    if L < 0:
        return max(X)*2
    useIT = 1 + makeChange(L-X[0], X)
    loseIT = makeChange(L, X[1:])
    return min(useIT, loseIT)

print makeChange(12, [1,2,3,6,12])
        
