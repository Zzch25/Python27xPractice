# CS 115 Homework 4
# Zachary Job
# 9/23/2012

###################################################################################
# PROBLEM 1 
###################################################################################

# Define fancyLCS, the function described in the first part of this page:
# https://www.cs.hmc.edu/twiki/bin/view/ModularCX/SequenceAlignment!       


#!!!!!!!!!!!!!!!!Tried to the best of my ability to compress this into one function to no avail!!!!!!!!!!!!!!!!

#fancyLCS("3 3 t6 v>y>/bob.l0r@", "3 } w25vk;y+&bob11001{}")
#fancyLCS("m+rawboxenrn%ury", " urawbpreyri iry ")
#fancyLCS("hello", "hilly")

def fancyLCS(X, Y):
    """instantly runs"""
    if X == "" or Y == "":
        if(len(X) > 0):
            return [0, '#'*len(X), '']
        return [0,'','#'*len(Y)]
    m = fancyLCS(X[1:], Y[1:])
    if X[0] != Y[0]:
        return (m[0], "#" + m[1], "#" + m[2])
    return (1+m[0], X[0] + m[1], Y[0] + m[2])        

###################################################################################
# PROBLEM 2
###################################################################################

# Implement wordsWithScore() which is specified below.
# Hints: Use map.  And use some of the functions you did for
# homework 3 (Scrabble Scoring).  As always, include any helper
# functions in this file, so we can test it.

# Here's the list of letter values and a small dictionary to use.

scrabbleScores = [ ["a", 1], ["b", 3], ["c", 3], ["d", 2], ["e", 1], ["f", 4], ["g", 2], ["h", 4], ["i", 1], ["j", 8], ["k", 5], ["l", 1], ["m", 3], ["n", 1], ["o", 1], ["p", 3], ["q", 10], ["r", 1], ["s", 1], ["t", 1], ["u", 1], ["v", 4], ["w", 4], ["x", 8], ["y", 4], ["z", 10] ]

aDictionary = ["a", "am", "at", "apple", "bat", "bar", "babble", "can", "foo", "spam", "spammy", "zzyzva"]

X = [1,2,3,4,5,6,7,8]

def wordsWithScore(dict, scores):
    '''Assume dict is a list of words and scores is a list of [letter,number] pairs.
    return the dictionary annotated so each word is paired with its value.
    For example, wordsWithScore(scrabbleScores, aDictionary) should return
    [["a", 1], ["am", 4], ["at", 2] ...etc... ]'''
    if len(dict) > 1:
        return [[dict[0], wordScore(dict[0], scores)]] + wordsWithScore(dict[1:], scores)
    return [[dict[0], wordScore(dict[0], scores)]]

def wordScore(S, scores):
    if S == "" or scores == "":
        return 0
    return letterScore(S[0], scores) + wordScore(S[1:],scores)

def letterScore(letter, scorelist):
    """checks for individual letter score"""
    if letter == (scorelist[0])[0]:
        return (scorelist[0])[1];
    return letterScore(letter, scorelist[1:])

print "Testing wordsWithScore"
print wordsWithScore(aDictionary,scrabbleScores)

###################################################################################
# PROBLEM 3
###################################################################################

# For the sake of an exercise, we will implement a function
# that does a kind of slice.  You must use recursion for this
# one.  Your code is allowed to refer to list index L[0] and
# also use slice notation L[1:] but no other slices.

def take(n, L):
    if L == []:
        return ""
    if n > 1:
        return [L[0]] + take(n-1, L[1:])
    elif n == 1: return [L[0]]
    return []

# Code to use for testing
def testTake(n,L):
    '''computes L[0:n] using the function above and checks the answer'''
    if take(n,L)==L[0:n]:
        print "test ok"
    else: print "my test didn't fail, but it didn't feel like working"

testTake(0, ["not", "it", "works", "!"])
testTake(2, ["not", "it", "works", "!"])
testTake(4, ["not", "it", "works", "!"])


###################################################################################
# PROBLEM 4
###################################################################################

# Similar to problem 3, will implement another function
# that does a kind of slice.  You must use recursion for this
# one.  Your code is allowed to refer to list index L[0] and
# also use slice notation L[1:] but no other slices.
    
def drop(n, L):
    if L == []:
        return ""
    if n < len(L)-1:
        return [L[n]] + drop(n+1, L)
    elif n == len(L)-1: return [L[n]]
    return []

def testDrop(n,L):
    '''computes L[n:] using the function above and checks the answer'''
    if drop(n,L)==L[n:]:
        print "test ok"
    else: print "my test failed"

testDrop(0, ["I", "am", "nearly", "done"])
testDrop(1, ["I", "am", "nearly", "done"])
testDrop(3, ["I", "am", "nearly", "done"])




