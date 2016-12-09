# hwImperSol.py 
# Zachary Job
# 11/17/12

#########################################################################################
# Debugging Note
# Note: All functions will execute before and after Test call. Test Results located at
# the bottom, but more detailed results are viewable.
#########################################################################################

tL = ["test1", "test2", "test3"] #test list used for functions requiring lists
tW = "Hello" #test word used for functions requiring words

def space(): #called to print spacing between print outputs for each excercise
    for x in range(2):
        print "##########################"
    return

def space2(): #called to print spacing between print outputs for each excercise
    for y in range(1):
        print "--------------------------"
    return

#########################################################################################
# Exercise 0
#########################################################################################

def questify(strs):
    ''' Assume strs is a list of strings.  Return a list of
        the same strings but with ? suffixed to each.'''
    def addQuestmark(str):
        '''add question mark mark to a string'''
        return str + '?'
    return map(addQuestmark, strs)

# performs function of questify ##########################
def questifyAlt(strs):
    m = [] #creates blank list
    for x in list(strs): #iterates each string
        m += [x + "?"] #adds question mark
    return m
##########################################################

print "E0"
print "questify: " + str(questify(tL))
print "questifyAlt: " + str(questifyAlt(tL))
space()

#########################################################################################
# Exercise 1
#########################################################################################

def leppard(inputString):
    ''' Mystery.'''
    outputString = ""
    for symbol in inputString:    
        if symbol == "o":
           outputString = outputString + "ooo"
        else:
           outputString = outputString + symbol
    print outputString

def leppardIndex(inputString):
    ''' Same as leppard(), but using an integer index rather than directly
        referring to elements of the input string.'''
    outputString = ""
    for i in range(len(inputString)):
        if inputString[i] == "o":
           outputString = outputString + "ooo"
        else:
           outputString = outputString + inputString[i]
    print outputString

def catenate(strs):
    ''' Assume strs is a list of strings.  Return a single string, their catenation.'''
    if strs == []:
       return ""
    else:
       return reduce(lambda s, t: s + t,   strs)

# performs function of catenate with loops ###############
def catenateLoop(strs):
    m = "" # sets up a blank string
    for x in list(strs): # loops through each list element
        m += x # element catenator, adds to m
    return m
##########################################################

def catenateTest():
    ''' Test consistency between two versions of catenate.'''
    test0 = ["one ", "test ", "case"]
    test1 = []
    test2 = ["", "xxx", "", "yyy"]
    for t in [test0, test1, test2]:  
        print "Test case", t, "is ok?", catenate(t) == catenateLoop(t)

print "E1"
print "leppard: "
leppard(tW)
print "leppardIndex: "
leppardIndex(tW)
print "catenate: " + str(catenate(tL))
print "catenateLoop: " + str(catenateLoop(tL))
catenateTest()
space()

#########################################################################################
# Exercise 2
#########################################################################################

scrabbleScores = [ ["a", 1], ["b", 3], ["c", 3], ["d", 2], ["e", 1], ["f", 4], ["g", 2], ["h", 4], ["i", 1], ["j", 8], ["k", 5], ["l", 1], ["m", 3], ["n", 1], ["o", 1], ["p", 3], ["q", 10], ["r", 1], ["s", 1], ["t", 1], ["u", 1], ["v", 4], ["w", 4], ["x", 8], ["y", 4], ["z", 10] ]

aDictionary = ["a", "am", "at", "apple", "bat", "bar", "babble", "can", "foo", "spam", "spammy", "zzyzva"]

def letterScore(letter, scorelist): 
    if scorelist == []: return 0 #<<<<<<<<<<<<<<<<<<<<<<<<<# added missing catch block
    if letter == scorelist[0][0]:
        return scorelist[0][1]
    return letterScore(letter, scorelist[1:])

# performs function of letterScore #######################
def letterScoreLoop(letter, scoreList):
    m = 0 # set new zeroed integer
    for x in list(scoreList): # iterate scorelist via each number letter pair
        if x[0] == letter: # if letter match occurs with letter of pair and letter variable
            m += x[1] # add numerical value of pair to m if match occurs
    return m
##########################################################
    
def letterScoreTest():
    ''' Test consistency between two versions of letterScore.'''

    for ltr in ['a', 'b', 'x']:  
        print "Test case", ltr, "is ok?", letterScore(ltr, scrabbleScores) == letterScoreLoop(ltr, scrabbleScores)

print "E2"
print "letterScore: " + str(letterScore("b", scrabbleScores))
print "letterScoreLoop: " + str(letterScoreLoop("b", scrabbleScores))
letterScoreTest()
space()

#########################################################################################
# Exercise 3
#########################################################################################

def wordScore(S, scorelist):   
    ''' Assume S is a string and scorelist is in the format above and 
        includes every letter in S.  Return the scrabble score of that string.'''
    if S == '': 
        return 0
    else:
        return letterScore(S[0], scorelist) + wordScore(S[1:], scorelist)

# performs function of wordScore #########################
def wordScoreLoop(S, scorelist): 
    m = 0 # create new zeroed integer
    for x in str(S): # for each letter in word
        m += letterScore(x, scorelist) # add value of letter to m
    return m
##########################################################

def wordScoreTest():
    ''' Test consistency between two versions of wordScore.'''
    for word in ['ok', 'brilliant', 'splendid']:  
        print "Test case", word, "is ok?", wordScore(word, scrabbleScores) == wordScoreLoop(word, scrabbleScores)

print "E3"
print "wordScore: " + str(wordScore(tW, scrabbleScores))
print "wordScoreLoop: " + str(wordScoreLoop(tW, scrabbleScores))
wordScoreTest()
space()

#########################################################################################
# Exercise 4
#########################################################################################

def wordsWithScore(dict, scores):
    '''Assume dict is a list of words and scores is a list of [letter,number] pairs.
    return a copy of the dictionary, annotated so each word is paired with its value.
    For example, wordsWithScore(scrabbleScores, aDictionary) should return
    [["a", 1], ["am", 4], ["at", 2] ...etc... ]'''
    def scoreWord(wrd):
      return [ wrd, wordScore(wrd, scores) ]        
    return map(scoreWord, dict)

# performs function of wordsWithScore ####################
def wordsWithScoreLambda(dict, scores):
    return map(lambda x: [x,wordScore(x, scores)], dict) #maps wordScore over every word in the dictionary and returns a list of words with their scores
##########################################################

print "E4"
print "wordsWithScore: " + str(wordsWithScore(aDictionary, scrabbleScores))
print "wordsWithScoreLambda: " + str(wordsWithScoreLambda(aDictionary, scrabbleScores))
space()

#########################################################################################
# Exercise 5  
#########################################################################################

# performs function of wordsWithScore ####################
def wordsWithScoreLoop(dict, scores):
    m = [] # creates a blank list
    for x in list(dict): # for each word in dict
        m += [[x,wordScore(x, scores)]] # add each word and its score to m
    return m
##########################################################
    
def wordsWithScoreTest():
    L = wordsWithScore(aDictionary, scrabbleScores)
    M = wordsWithScoreLambda(aDictionary, scrabbleScores)
    N = wordsWithScoreLoop(aDictionary, scrabbleScores)
    print 'Lambda version, on aDictionary', M == L
    print 'Loop version, on aDictionary', N == L

print "E5"
print "wordsWithScoreLoop: " + str(wordsWithScoreLoop(aDictionary, scrabbleScores))
wordsWithScoreTest()
space()
space()

#########################################################################################
# Main test
#########################################################################################

def testAll():
    print ":::CATENATE:::"
    catenateTest() #test
    space2()
    print ":::LETTERSCORE:::"
    letterScoreTest() #test
    space2()
    print ":::WORDSCORE:::"
    wordScoreTest() #test
    space2()
    print ":::WORDSWITHSCORE:::"
    wordsWithScoreTest() #test
    space2()

print "TESTING FUNCTIONS"
space2()
testAll()



        
        

