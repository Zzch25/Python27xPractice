# hwImperSol.py 
# D. Naumann Nov 2012
 
# Objectives: get familiar with imperative style and for- and while-loops.

# Instructions: Submit a copy of this file, with the incomplete functions completed.
# To find those, search for "TO DO".
# Of course put your name in place of mine at the top of the file.
# Do NOT change the functions # that are already implemented.  

# As always, feel free to define additional functions as needed, and do more 
# thorough tests.

############
# Exercise 0
# Study function questify().  Then implement questifyAlt() so that it 
# gives the same results as questify(), using map and lambda but no helping function.
# Hint: adapt the body of addQuestmark().
############

def questify(strs):
    ''' Assume strs is a list of strings.  Return a list of
        the same strings but with ? suffixed to each.'''
    def addQuestmark(str):
        '''add question mark mark to a string'''
        return str + '?'

    return map(addQuestmark, strs)

def questifyAlt(strs):
    ''' Same as questify.'''
    return None # TO DO


############
# Exercise 1
# Study functions leppard() and catenate().  Implement catenateLoop(), without
# using recursion or reduce or any built-in Python function.  Instead, use a 
# loop.  In some ways your code will resemble the body of leppard() (below).
# If you prefer, you can follow the style of leppardIndex() but I suggest not.
############

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

def catenateLoop(strs):
    ''' same as catenate'''
    return None # TO DO

def catenateTest():
    ''' Test consistency between two versions of catenate.'''
    test0 = ["one ", "test ", "case"]
    test1 = []
    test2 = ["", "xxx", "", "yyy"]
    for t in [test0, test1, test2]:  
        print "Test case", t, "is ok?", catenate(t) == catenateLoop(t)
        

############
# Exercise 2
# Implement letterScoreLoop using --you guessed it-- a loop instead of recursion.  
# Also, do not use map or reduce.
############

scrabbleScores = [ ["a", 1], ["b", 3], ["c", 3], ["d", 2], ["e", 1], ["f", 4], ["g", 2], ["h", 4], ["i", 1], ["j", 8], ["k", 5], ["l", 1], ["m", 3], ["n", 1], ["o", 1], ["p", 3], ["q", 10], ["r", 1], ["s", 1], ["t", 1], ["u", 1], ["v", 4], ["w", 4], ["x", 8], ["y", 4], ["z", 10] ]

aDictionary = ["a", "am", "at", "apple", "bat", "bar", "babble", "can", "foo", "spam", "spammy", "zzyzva"]

def letterScore(letter, scorelist): 
    ''' Assume scorelist is a list of lists [ltr,val] where ltr is a single letter and val is a
        natural number.  Assume letter is a single letter string, that occurs in scorelist.
        Return the associated value.'''
    if letter == scorelist[0][0]:
        return scorelist[0][1]
    else:
        return letterScore(letter, scorelist[1:])

def letterScoreLoop(letter, scoreList):
    ''' Same as letterScore'''
    # HINTS: You can rely on the assumption that letter occurs in scorelist.
    # It may be helpful to use an if-statement without an else.

    return None # TO DO

def letterScoreTest():
    ''' Test consistency between two versions of letterScore.'''

    for ltr in ['a', 'b', 'x']:  
        print "Test case", ltr, "is ok?", letterScore(ltr, scrabbleScores) == letterScoreLoop(ltr, scrabbleScores)


############
# Exercise 3
# Implement wordScoreLoop using a loop instead of recursion.  (And don't
# use map or reduce.)
# Use letterScore() or letterScoreLoop(), it shouldn't matter which one.
############

def wordScore(S, scorelist):   
    ''' Assume S is a string and scorelist is in the format above and 
        includes every letter in S.  Return the scrabble score of that string.'''
    if S == '': 
        return 0
    else:
        return letterScore(S[0], scorelist) + wordScore(S[1:], scorelist)

def wordScoreLoop(S, scorelist): 
    ''' same as wordScore'''
    return None # TO DO

def wordScoreTest():
    ''' Test consistency between two versions of wordScore.'''
    for word in ['ok', 'brilliant', 'splendid']:  
        print "Test case", word, "is ok?", wordScore(word, scrabbleScores) == wordScoreLoop(word, scrabbleScores)


############
# Exercise 4
# Implement wordsWithScoreLambda using a lambda instead of the helper scoreWord.
############

def wordsWithScore(dict, scores):
    '''Assume dict is a list of words and scores is a list of [letter,number] pairs.
    return a copy of the dictionary, annotated so each word is paired with its value.
    For example, wordsWithScore(scrabbleScores, aDictionary) should return
    [["a", 1], ["am", 4], ["at", 2] ...etc... ]'''

    def scoreWord(wrd):
      return [ wrd, wordScore(wrd, scores) ]
        
    return map(scoreWord, dict)

def wordsWithScoreLambda(dict, scores):
    ''' same as wordsWithScore'''
    return None # TO DO


############
# Exercise 5
# Implement wordsWithScoreLoop using a loop instead of map or recursion.
# Be careful NOT to change the dictionary.  
############

def wordsWithScoreLoop(dict, scores):
    '''Same as wordsWithScore''' 
    return None # TO DO

def wordsWithScoreTest():
    L = wordsWithScore(aDictionary, scrabbleScores)
    M = wordsWithScoreLambda(aDictionary, scrabbleScores)
    N = wordsWithScoreLoop(aDictionary, scrabbleScores)
    print 'Lambda version, on aDictionary', M == L
    print 'Loop version, on aDictionary', N == L

###########
# Main test
###########

def testAll():
    catenateTest()
    letterScoreTest()
    wordScoreTest()
    wordsWithScoreTest()
        
        

