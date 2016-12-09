##############################################################LCS Example
#########################################################################


#fancyLCS("m+rawboxenrn%ury", " urawbpreyri iry ")

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

print "Fancy LCS Test: 'm+rawboxenrn%ury vs urawbpreyri iry '"
print fancyLCS("m+rawboxenrn%ury", " urawbpreyri iry ")
print "----------------------------------------------------"

#-recurses to the end
#-if odd, perform upper block until no longer odd or till end
#-calls lower when even
#-stacks results (matches, x, y)

#########################################################Powerset Example
#########################################################################

#powerset([1,2])

def powerset(X):
    if X==[]:
        return [[]]
    temp = powerset(X[1:])
    return temp + map(lambda x: [X[0]] + x, temp)

print "Powerset Test: '1,2'"
print powerset([1,2])
print "----------------------------------------------------"

###############################################################ED Example
#########################################################################

FEDstore = dict()

#fastED("extraordinary", "originality")

def fastED(first, second):
   ''' Returns the edit distance between the strings first and second.'''
   if FEDstore.has_key((first, second)):
       return FEDstore[(first, second)]
   elif first == '':
      FEDstore[(first, second)] = len(second) 
      return len(second)
   elif second == '':
      FEDstore[(first, second)] = len(first)
      return len(first)
   elif first[0] == second[0]:
      tempor = fastED(first[1:], second[1:])
      FEDstore[(first, second)] = tempor
      return tempor
   else:
      substitution = 1 + fastED(first[1:], second[1:])
      deletion = 1 + fastED(first[1:], second)
      insertion = 1 + fastED(first, second[1:])
      FEDstore[(first, second)] = min(substitution, deletion, insertion)
      return min(substitution, deletion, insertion)

#return 1 for no match
#create database for possible recurrences

######################################################Spell Check Example
#########################################################################

words = ["apple", "world", "globe", "trotters", "bus", "running", "eighty",
         "bannana", "how", "later", "mile", "sigh", "nile", "borrow",
         "take", "hello"]

#spellCheck()

def spellCheck():
    print "------------"
    print "-1 to exit"
    print "------------"
    inp=raw_input("Input Word: ")
    if inp == "": return
    if inp == "-1": return "Exiting" 
    L = map(lambda w:(fastED(w,inp), w), words)
    L.sort()
    if 0 == L[0][0]:
        print (inp + " is spelled properly")
        return spellCheck()
    print ("Did you mean " + L[0][1])
    return spellCheck()

print spellCheck()

