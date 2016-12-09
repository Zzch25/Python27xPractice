#Zachary Job
#10/19/2012

######### I originally submitted my assignment on time, but there was an error with addb #########
######### I was hoping that I could possibly get full credit because midterms and all    #########
######### forced me to start this assignment tonight and I really just couldn't move fast#########
######### enough.                                                                        #########


##########################################################################Binary Conversion
###########################################################################################
###########################################################################################

print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
print "+++++++++++++++++++++++Conversion Work+++++++++++++++++++++++++++"
print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"

##########################################################################numToBase

#numToBase(4, 2) //100

def numToBase(X, Y):
    if X == 0: return ""
    return numToBase(X/Y, Y)+str(X%Y)
                
print "Input:(4,2)"
print "=========================numToBase==============================="
print "Result:"+numToBase(4,2)

##########################################################################BaseToNum

#baseToNum("1110", 2)

def baseToNum(X, Y):
    if X=="": return 0
    return (Y**(len(X)-1))*int(X[0])+baseToNum(X[1:], Y)

print "================================================================="                     
print "Input:(1110, 2)"
print "=========================baseToNum==============================="
print "Result:"+str(baseToNum("1110", 2))

#########################################################################baseToBase

#baseToBase(2, 10, "11")

def baseToBase(X,Y,Z):
    if X == "" or Y == "" or Z == "": return "this + midterms... why!?!?!?!"
    return numToBase(baseToNum(Z, X), Y)

print "================================================================="                     
print "Input:(2, 10, 11)"
print "========================baseToBase==============================="
print "Result:"+baseToBase(2, 10, "11")

################################################################################add

#add("011", "100")

def add(X, Y):
    return numToBase(baseToNum(X, 2)+baseToNum(Y, 2), 2)

print "================================================================="                     
print "Input:(011, 100)"
print "============================add=================================="
print "Result:"+add("011", "100")

###############################################################################add2

addeN = 0

#add2("011", "011")

def add2(X, Y):
    global addeN
    if len(X)<len(Y): X = "0"*(len(Y)-len(X))+X
    if len(Y)<len(X): Y = "0"*(len(X)-len(Y))+Y
    if X == "":
        addeN = 0
        return ""
    if addeN == 1:
        if X[-1]!=Y[-1]:
            return add2(X[:-1],Y[:-1]) + "0"
        if X[-1]=="0":
            addeN = 0
            return add2(X[:-1],Y[:-1]) + "1"
        return add2(X[:-1],Y[:-1]) + "1"
    if X[-1]!=Y[-1]:
        return add2(X[:-1],Y[:-1]) + "1"
    if X[-1]=="0":
        return add2(X[:-1],Y[:-1]) + "0"
    addeN = 1
    return add2(X[:-1],Y[:-1]) + "0"


print "================================================================="                     
print "Input:(011, 100)"
print "============================add2================================="
print "Result:"+add2("011", "100")


#########################################################################Binary Compression
###########################################################################################
###########################################################################################

biLen = 8

print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
print "++++++++++++++++++++++Compression Work+++++++++++++++++++++++++++"
print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"

###################################################################################Compress

#compress("0000000000001111111111111000011100000001111000000000011100000000")

def compress(X):
    if X=="":
        return ""
    if X[0]=="0":
        temp = compressNot0(X)
        return longer(numToBinary(temp), biLen) + compress(X[temp:])
    if X[0]=="1":
        temp = compressNot1(X)
        return longer(numToBinary(temp), biLen) + compress(X[temp:])

def longer(X, Y):
    if len(X)<Y:
        return "0"*(Y-len(X))+X
    return X
    
def compressNot0(X):
    if X == "" or X[0]!="0":
        return 0
    return 1 + compressNot0(X[1:])

def compressNot1(X):
    if X == "" or X[0]!="1":
        return 0
    return 1 + compressNot1(X[1:])
    
def numToBinary(X):
    if X == 0: return ""
    if X%2 == 0:
        return numToBinary(X/2) + "0"
    return numToBinary(X/2) + "1"

print "Input:0000000000001111111111111000011100000001111000000000011100000000"
print "==========================compress==============================="
print "Result:"+compress("0000000000001111111111111000011100000001111000000000011100000000")

#################################################################################Uncompress

#uncompress(["000011000000110100000100000000110000011100000100000010100000001100001000"])

def uncompress(X):
    if X == "":
        return ""
    if len(X) > biLen:
        return binaryToNum(X[0:8])*"0"+binaryToNum(X[8:16])*"1"+uncompress(X[16:])
    return binaryToNum(X[0:8])*"0"

def binaryToNum(S):
    if S == "": return 0
    if S[0] == "1":
        return 2**(len(S)-1) + binaryToNum(S[1:])
    return binaryToNum(S[1:])

print "================================================================="
print "Input:000011000000110100000100000000110000011100000100000010100000001100001000"
print "=========================uncompress=============================="
print "Result:"+uncompress("000011000000110100000100000000110000011100000100000010100000001100001000")

################################################################################Compression

#compression("0000000000001111111111111000011100000001111000000000011100000000")

def compression(X):
    return float(len(compress(X)))/float(len(X))

print "================================================================="
print "Input:0000000000001111111111111000011100000001111000000000011100000000"
print "=========================compression============================="
print "Result:"+str(compression("0000000000001111111111111000011100000001111000000000011100000000"))
