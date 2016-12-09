#Zachary Job
#10/11/12

#numToBinary(12) // 1100
#

def numToBinary(X):
    if X == 0: return ""
    if X%2 == 0:
        return numToBinary(X/2) + "0"
    return numToBinary(X/2) + "1"

#binaryToNum("1100") // 12
#

def binaryToNum(S):
    if S == "": return 0
    if S[0] == "1":
        return 2**(len(S)-1) + binaryToNum(S[1:])
    return binaryToNum(S[1:])

#increment("1100") // 12
#

def increment(X):
    M = numToBinary(binaryToNum(X)+1)
    return "0"*(len(X) - len(M))+M

#count("00000000", 4)
#

def count(X, Y):
    if Y == 0:
        return X
    print X
    q = increment(X)
    return count(q, Y-1)

#numToTernary(42) // 1120
#

def numToTernary(X):
    return "blah"

#TernaryToNum("1120") // 42
#

def TernaryToNum(S):
    return "blah"





    
