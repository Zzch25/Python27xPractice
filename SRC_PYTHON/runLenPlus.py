# runLenPlus - lab exercise for fancy version of run length encoding
# D. Naumann, 23 Oct 2012

import math

# GOAL: compress/uncompress binary strings using adaptive run-length encoding.

# We will work with binary strings like '0110'.
# The goal is to define functions compressA and uncompressA,
# using run length encoding in an 'adaptive' way.  The possible
# run lengths are based on analysis of the string to be compressed;
# this determines how many bits are used to represent each run length.
# That number must be included in the compressed data, so it can
# be used when un-compressing.

# The compressed format, which I call RLE+, looks like this:
#       bbbwxwxwxwx...
# - bbb is three bits, which represent a number runBits, 0 < runBits < 8
# - each w is runBits bits and encodes the length of a run of 0s
# - each x is runBits bits and encodes the length of a run of 1s
# Note that the wxwxw... part is basic Run Length Encoding (RLE) as in hw 6.

# For example, 010 10 10 01 10  (but without spaces)
#              bbb w  x  w  x
# encodes the string 001101.

# The compressA function should first scan the input string to determine
# how long is the average run length, avgLen, and then choose a sensible
# number of bits to use for encoding run lengths.
# Here is a specific suggestion for that: Let runBits be one more than 
# the log of avgLen, but at most 7.  This means we compress using runs
# of length less than 2**runBits.
# More precisely: 
# let n = math.ceil(math.log(m,2)) + 1 and runBits = min(n,7).

# If runBits is 1, compression is pointless, but we'll do it anyway.

########
# Step 0
# Before working on adaptive RLE, have a look at the code below
# which provides basic RLE.  (A solution for homework 6, using 4-bit
# numbers for run lengths.)
########

def numToBinary(n):
    '''String with the binary representation of non-negative integer n; 
        but empty string if n is 0'''
    if n==0:
        return ''
    elif n % 2 != 0:
        return numToBinary(n/2) + '1'
    else:
        return numToBinary(n/2) + '0'

def binaryToNum(s):
    '''assuming s is a non-empty string of 0s and 1s, return the number that s is a
        binary representation of; the empty string represents 0.'''
    if s == '':
        return 0
    else:
        return 2 * binaryToNum(s[:-1]) + int(s[-1])

def numToBinPadded(n, runBits):
    '''Assume 0 <= n < 2**runBits.  Return binary rep of n
        padded with leading 0s to have length runBits.
        For example, numToBinPadded(3, 4) is '0011'. '''

    s = numToBinary(n)
    pad = '0'*(runBits - len(s))
    return pad + s

def prefixLen(s):
    '''Assume s is a non-empty string; return n such that s begins with n
        copies of s[0].  For example, prefixLen('010') = 1, prefixLen('1110') = 3.'''
    if len(s) == 1: return 1
    elif s[1]==s[0]: return 1 + prefixLen(s[1:])
    else: return 1

def compressX(s, b, runBits):
    '''Assume s is string and b is 0 or 1.  Return RLE of s starting with the
        num of b's at start of s (which may be none).  
        Each run length is encoded using exactly runBits bits.'''
    if s=='':
        return ''
    elif s[0] != chr(b + ord('0')):  # doesn't begin with b?
        return numToBinPadded(0, runBits) + compressX(s, 1-b, runBits)
    else:                            # does begin with b
        maxRunLen = 2**runBits - 1
        plen = min(prefixLen(s),  # number of bs at start of s; at least 1, at most maxRunLen
                   maxRunLen)
        return numToBinPadded(plen, runBits) + compressX(s[plen:], 1-b, runBits)

def compress(s):
    '''Return the basic RLE of s using 4-bit run lengths.'''
    return compressX(s, 0, 4)

def uncompressX(s, b, runBits):
    '''Assume s is in wxwx... or xwxw... format, depending on whether
    b is 0 or 1. Return the string that s encodes.'''
    if s=='': return ''
    else:
        n = binaryToNum(s[:runBits])
        prefix = n * chr(b + ord('0'))
        return prefix + uncompressX(s[runBits:], 1-b, runBits)

def uncompress(s):
    '''Return the string that s encodes, assuming basic RLE with 4-bit run lengths.'''
    return uncompressX(s, 0, 4)

########
# Step 1
# Complete the following definition.
# It uses the accumulator technique introduced in class.
########

L0 = '1110001111001010' # runBits will be 2
L1 = '1'                # runBits will be 1
L2 = '111111110101010101010101010101010101010101' # runBits 1
L3 = '110011001100'     # runBits 2
L4 = '000111000111'     # runBits 3 (is this ideal?)
L5 = '0000111100001111' # runBits 3

#listOfRunLengths(L0)

def listOfRunLengths(s):
    if s=="":
        return []
    def lORL(s, result, curCount, curVal):
        if s=="": return result
        if s[0]==curVal: 
            return lORL(s[1:], result, curCount+1, curVal)
        result += [str(curCount)]
        if curVal==1: curVal = 0
        else: curVal = 1
        return lORL(s[1:], result, 1, curVal)           
    return lORL(s[1:], [], 1, s[0]) # first run begins with s[0] and has length 1 so far

########
# Step 2
# Complete the following definition.
########

def findRunBits(s):
    '''Returns the number of bits to use for compressing string s.
        Assume s is a nonempty string.
        Specifically, returns n where n is the log of the average
        run length, but at most 7, as described at the beginning of this file.
        The maximum n is 7 because only three bits are available
        for it (the bbb in the compressed format).'''
    
    return None # TO DO

########
# Step 3 
# Here are compressA and uncompressA using the preceding functions.
# Test them.
########

def compressA(s):
    '''Returns compressed form of s using RLE+ format.'''
    runBits = findRunBits(s) # expect 0 < runBits < 8
    bbb = numToBinPadded(runBits, 3)
    return bbb + compressX(s, 0, runBits)

def uncompressA(s):
    '''Assume s is a string of 0s and 1s in the RLE+ format above.
    Return the string that it encodes.'''
    bbb = s[0:3]
    runBits = binaryToNum(bbb)
    wxs = s[3:]
    return uncompressX(wxs, 0, runBits)



        


