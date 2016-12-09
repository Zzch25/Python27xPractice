#Zachary Job - 9/17/2012
#sample code included to individually test functions
#fucntions listed in order of use
#Sorry for the large volume of code, originally I thought the assignment was to filter a single dictionary with
#entries like so [[x,1],[dog,4]... 

#PREconditions: A string is entered, Dictionary follows given format and is 2+ lists long
#POSTconditions: Will function as commented

dictionary = ["a", "am", "at", "apple", "bat", "bar", "babble", "can", "foo", "spam", "spammy", "zzyzva"] 
scrabbleScores = [ ["a", 1], ["b", 3], ["c", 3], ["d", 2], ["e", 1], ["f", 4], ["g", 2], ["h", 4], ["i", 1], ["j", 8], ["k", 5], ["l", 1], ["m", 3], ["n", 1], ["o", 1], ["p", 3], ["q", 10], ["r", 1], ["s", 1], ["t", 1], ["u", 1], ["v", 4], ["w", 4], ["x", 8], ["y", 4], ["z", 10] ]

#Main Block

#bestWord(["a","b","c","t"])

print "Enter a non empty string filter (list)"

def bestWord(rack):
    """Will find the best result possible for points upon recieving letters"""
    if rack == []:
        return []
    return reduce(lambda n, y: isGreater(n, y), scoreList(rack)[0:])

#isGreater(["hey", 1],["heyo", 3])

def isGreater(L1, L2):
    """Will compare scores of two dictionary entries"""
    if L1[1] > L2[1]:
        return L1
    return L2

#scoreList(["a","b","c","t"])

def scoreList(rack):
    """Calls manage to input rack as the user definition"""
    if rack == []:
        return []
    return theBoss(manage(rack, dictionary), scrabbleScores)

###############################

#Score Block

def theBoss(X, S):
    """filters translation of rack into viable entries to be processed"""
    if len(X) > 1:
        return [[X[0], wordScore(X[0], S)]] + theBoss(X[1:], S)
    return [[X[0], wordScore(X[0], S)]]

#wordScore("lol", [["a,1"],["l",2]])

def wordScore(S, scorelist):
    """iterates through words to input individually to letterScore"""
    if S == "" or scorelist == "":
        return 0
    return letterScore(S[0], scorelist) + wordScore(S[1:],scorelist)

#letterScore("l", [["a,1"],["l",2]])

def letterScore(letter, scorelist):
    """checks for individual letter score"""
    if letter == (scorelist[0])[0]:
        return (scorelist[0])[1];
    return letterScore(letter, scorelist[1:])

###############################

#Filter Block
        
#manage(["h","w"], ["x", "hw", "herro", "hww"])

def manage(L, X):
    """Returns all valid possibilities"""
    if len(X) > 1:
        if runCM(L, X[0]) == "":
            return [X[0]] + manage(L, X[1:])
        return manage(L, X[1:])
    elif runCM(L, X[0]) == "":
        return [X[0]]
    return []


#runCM(["h","w"], "aijdidjwfhhw")
    
def runCM(L, X):
    """Manages checkMatch by iterating the filter list"""
    if L == "":
        return ""
    elif len(L) > 1:
        return runCM(L[1:], checkMatch(L[0],X))
    return checkMatch(L[0],X)
    
#checkMatch("h","x") 
    
def checkMatch(L, X):
    """Filters any matches from a word""" 
    if L == [] or X == "":
        return ""
    elif X[0] != L:
        return X[0] + checkMatch(L, X[1:])
    return "" + X[1:]



