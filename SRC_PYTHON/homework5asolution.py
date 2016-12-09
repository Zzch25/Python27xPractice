#Zachary Job
#10/11/12

#########################
#########\/HW\/##########
#########################

#numTobTernary(42) // +---0
#

def numTobTernary(X):
    if X == 0: return ""
    if X%3 != 0 and ((X+1)%3) != 0: return numTobTernary(X/3) + "+"
    if ((X+1)%3) == 0: return numTobTernary((X/3)+1) + "-"
    return numTobTernary(X/3) + "0"
    
#bTernaryToNum("+---0") // 42
#

def bTernaryToNum(S):
    if S == "": return 0
    if S[0] == "+": return 3**(len(S)-1) + bTernaryToNum(S[1:]) 
    if S[0] == "-": return -3**(len(S)-1) + bTernaryToNum(S[1:])
    return 0 + bTernaryToNum(S[1:])    


#########################
########\/LAB\/##########
#########################


#numToBinary(12) // 1100
#

def numToBinary(X):
    if X == 0: return ""
    if X%2 != 0: return numToBinary(X/2) + "1"
    return numToBinary(X/2) + "0"

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
    print "-----"
    print X%3
    print X
    print "-----"
    if X == 0: return ""
    return numToTernary(X/3) + str(X%3)

#TernaryToNum("1120") // 42
#

def TernaryToNum(S):
    if S == "": return 0
    if S[0] == "1": return 3**(len(S)-1) + TernaryToNum(S[1:]) 
    if S[0] == "2": return 2*(3**(len(S)-1)) + TernaryToNum(S[1:])
    return 0 + TernaryToNum(S[1:])   



