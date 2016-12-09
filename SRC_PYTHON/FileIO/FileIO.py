# fileIO
# Zachary Job
# 11/26/2012

##########################################FOR-MY-EYES-ONLY!!
############################################################

"""DOCSTRINGS"""
""" for var = var = x #: blah """
""" for func = def blah 'enter' """""" """

"""python will compare words alphabetically"""

########################################################MAIN
############################################################

#NOTE: ", ".join() was used in the textbook so I assume it is appropriate

def main():
    """Runs all program components in a looped print interface"""
    loop = False #: queues quit/run for loop
    global users # make user data accessable everywhere

    print "Loading Users..."
    users = readPrefsPrintUsers(PATH) # open existing data
    
    while loop == False: # main menu loop
        printMenu()
        X = raw_input() # option input
        printBreak()
        if str(X).lower() == "q": # if q quit and save
            loop = True
            print "Exiting and Saving..."
            writePrefs() # save
        elif functionSelect1(str(X).lower()) == False: # invalid option selected! Also runs fselect 
            printBreak()
    return

def main2():
    """Runs all program components in a looped print interface"""
    loop = False #: queues quit/run for loop
    
    while loop == False: # main menu loop
        printMenu2()
        X = raw_input() # option input
        printBreak()
        if str(X).lower() == "q": # if q quit and save
            loop = True
            print "Back To Main"
        elif functionSelect2(str(X).lower()) == False: # invalid option selected! Also runs fselect 
            printBreak()
    return

def functionSelect1(X):
    """Takes String: Executes an appropriate function based on a lowercase letter"""
    if X == "e":
        print "Manage Preferences Selected"
        printBreak()
        main2()
        return
    if uAm() > 1: # users exist
        if X == "r":
            print "Get Recommendations Selected"
            printBreak()
            space()
            getRec()
            return
        if X == "p":
            print "Show Most Popular Artists Selected"
            printBreak()
            space()
            showPop()
            return
        if X == "h":
            print "How Popular is the Most Popular Selected"
            printBreak()
            space()
            howPop()
            return
        if X == "m":
            print "Which User Has The Most Likes Selected"
            printBreak()
            space()
            mostLikes()
            return
    else:
        print "Not enough users"
        return False
    print "Invalid Input"
    return False # an invalid option was input, return trigger for main

def functionSelect2(X):
    """Takes String: Executes an appropriate function based on a lowercase letter"""
    if X == "1":
        print "Add User Selected"
        printBreak()
        space()
        new()
        return
    if len(users) != 0:
        if X == "2":
            print "Delete User Selected"
            printBreak()
            space()
            delete()
            return
        if X == "3":
            print "Show All Selected Selected"
            printBreak()
            space()
            showall()
            return
        if X == "4":
            print "Privacy Selected"
            printBreak()
            space()
            privacy()
            return
    else:
        print "No users available"
        return False
    print "Invalid Input"
    return False # an invalid option was input, return trigger for main

###################################################FUNCTIONS
############################################################

#===================================================GET-RECS
def getRec():
    """Returns Recommendations For X User"""
    print "Recommendations - Enter A User \n$ Not Needed"
    printBreak()
    X = raw_input() # assign user name to X
    printBreak()

    if users.has_key((X+"$")) == True: X += "$" # modify in if private enabled
    if users.has_key(X) == True:
        score = 0 # used to keep track of the highest user match
        resultAm = -3 # how many peopel to draw from
        result = [] # Takes possible suggestions 
        fList = [] # list for suggestions
        fLsub = [] # temp for flist

        for key in users: # iterate each user 
            if key != X and checkOmit(key) != True: # if the name exists and is not the same as the comparator
                temp = str(matches(users[X],users[key])[-1]) + key
                if temp[0] != "0":
                    result += [temp] # assign value of x person in relation to comparator
            result = sortList(result)

        if len(result) <= 2: resultAm = len(result)*-1 # safety in case of fewer than expected matches
        temp = map(lambda i: users[i[1:]], result[resultAm:])
        
        for x in temp: # catenates
            fLsub += x
        
        fLsub = popByNumb(popByNumbSub(sortList(fLsub)) + users[X] + users[X]) # use popByNum to see which suggestions should be ommited
        
        for x in range(len(fLsub)): #iterate list of artists and their occurences
            if fLsub[x-1][1] == 1: # if no recurrences
                fList += [fLsub[x-1][0]] # add to fList
                
        if fList != users[X] and fList != []: # suggestions found
            print ", ".join(fList)
        else: # no suggestions
            print "We couldn't find any matches that move to your groove!"
            print "Try the most popular artist(s) available: " + ", ".join(popSub()[:-1])
        printBreak()
    else: # null or non-matching entry
        print "Invalid Entry"
    return

def matches(l1,l2):
    """Takes Two Sorted Lists - Checks and Scores Matches By Catenating Comparators"""
    splice = l2
    score = 0
    scores = []

    for X in range(len(l1)): # iterates comparator
        loop = False # loop quit queue
        scores += [[l1[X],0]]
        while loop == False: # count matches of artists
            if splice == []: # catch block
                loop = True
            elif splice[0] < l1[X]: # impossible for match to occur then on 
                splice = splice[1:]
            elif splice[0] == l1[X]: # match
                score += 1
                scores[X][1] += 1
                splice = splice[1:]
            else:
                loop = True
                
    return scores + [score]
    
#=================================================POPULARITY


def showPop(): ## menu opt
    """Returns the Most Popular Artist"""
    print "The Most Popular Artist(s)"
    printBreak()
    print ", ".join(popSub()[:-1]) # print most popular minus added pop value
    printBreak()
    return

def howPop(): ## menu opt
    """Returns How Many Like These Popular Guys and Gals"""
    print "The Most Popular Artist(s) With Numbers!!!"
    printBreak()
    temp = popSub() # call greatest once to a temp value to conserve
    print ", ".join(temp[:-1]) + " With " + str(temp[-1]) + " Subscriptions" # print most popular with subscriptions
    printBreak()
    return

def popSub():
    """Returns List of Most Popular Artist(s)"""
    input = []
    
    for X in range(len(users)): #this for setup generates the artist list, tried to incorporate map, but had amind block
        if checkOmit(users.keys()[X]) != True: # omit private
            arts = users.values()[X]
            for blah in arts:
                input += [blah]
    return  greatest(popByNumb(input)) # set X to artists + popularity 

def greatest(L):
    """Takes List: Returns the Greatest Valued Keys"""
    win = 0 # int to take greatest found value
    wL = [] # list to take highest scoring keys
    
    for elmn in range(len(L)): # iterate list of keys and scores
        if L[elmn][1] > win: # new high score
            win = L[elmn][1] # win just gives up and accepts the value its given
            wL = [L[elmn][0]] # wL is reset as there is a new higher and more supreme power
        elif L[elmn][1] == win: # if another match for the same score is found
            wL += [L[elmn][0]] # add this to wL with existing key
            
    return wL + [str(win)] # return key(s) with (their/its) score attached

def popByNumb(L):
    """Takes List: Returns Artists and How Many Times They Are Subscribed"""
    L = sortList(L) # alphabetizing rules!
    result = matches(popByNumbSub(L),L)[:-1] #get amount of recurrences per artist
    return result

def popByNumbSub(X): 
    """Takes List: Removes Duplicates"""
    i = 0
    while len(X[i:]) > 1:
        if X[i] == X[i+1]:
            X = X[:i] + X[(i+1):]
        else:
            i += 1
    return X

#============================================USER-MOST-LIKES
def mostLikes():
    """Who in This List Loves The Most Artists... Brown Nosing I Say"""
    highest = 0 # set base comparator to first dict item
    listODict = [] # set list to hold valid dictionary keys
    
    print "User(s) Subscribed to the Most Artist(s)"
    printBreak()
    
    for key in users: # iterate users
        if checkOmit(key) != True: # if user has opted out
            temp = len(users[key]) # finds length of current key's list
            if highest == temp: # if another user has the same amount
                listODict += [key] # add other user
            if highest < temp: # if new user has more likes
                highest = temp # reset X to higher value
                listODict = [key] # reset Y for obvs more important peps than like previously
                
    if listODict == []: # if no users are available or have opted out
        print "No Available Users For This Option"
    else:
        for i in list(listODict): # print out all people found to have had the highest subscriptions
            print "User " + i + " Who Subcribed To " + ", ".join(users[i])
    printBreak()
    return

#========================================================NEW
def new():
    """Enter A New or Edit A New User and List"""  
    loop = False
    listOfArtists = []
    userN = "" 
    
    print "Enter A User \nBlank Entry to Quit \nAdd $ to end for privacy"
    printBreak()
    userN = raw_input() # set name to input
    printBreak()
    print "Enter Artists - Blank+Enter to Quit"
    printBreak()

    
    while loop == False: # add artists loop
        inp = raw_input() # cumulate input for artist(s)
        if inp == "": # exit trigger
            printBreak()
            loop = True # end loop
            if listOfArtists == [] or userN == "": # null entry
                print "No Changes Will Be Made - Null Entry"
            else: # entries where made
                listOfArtists = sortList(listOfArtists) # alphabetize
                users[userN] = listOfArtists # add to data
                print "Changes Applied"
            printBreak()
        else: # continue to add artists
            listOfArtists += [inp]
    return

#=====================================================DELETE
def delete():
    """Delete A User"""
    print "Enter An Entry To Delete \n$ Not Required \nBlank+Enter to Quit"
    printBreak()
    userN = raw_input() # set name to input
    printBreak()
    if users.has_key(userN):
        del users[userN]
        print "Removal Succeded"
    elif users.has_key(userN+"$"):
        del users[userN+"$"]
        print "Removal Succeded"
    else:
        print "Invalid Key"
    printBreak()
    return
    
#===================================================SHOW-ALL
def showall():
    """Print All Users and Prefs."""
    print "All Entries"
    printBreak()
    for keys in users.items(): 
        print keys[0] + ": " + str(keys[1])
    printBreak()
    return

#====================================================PRIVACY

def privacy():
    """Enable/Disable Privacy Prefs."""
    print "Toggle Privacy By Typing A Name \nBlank>Enter To Quit \nDon't Enter $ At End"
    printBreak()
    ID = raw_input() # set name to id
    printBreak()
    if users.has_key(ID) == True: # if exists and is not private
        users[ID+"$"] = users[ID] 
        del users[ID]
        print "User Made Private"
    elif users.has_key(ID+"$") == True: # if exists and is private
        users[ID] = users[ID+"$"]
        del users[ID+"$"]
        print "User Privacy Removed"
    else:
        print "No Such User"
    printBreak()
    return

#####################################################SORTING
############################################################

def sortList(L):
    """Takes List: swaps minimum value of to the front of the current splice of a list"""
    
    for start in range(len(L)): # loop each time splicing apart the sorted and unsorted values
        minPos = getMinPos(L,start) # minimum of the unsorted
        L = switch(L,start,minPos) # move the minimum to the front of the unsorted
        
    return L

def getMinPos(L,startPos):
    """Takes List, Int: finds the minimum value of a list"""
    minPos = startPos # start with a base comparator
    
    for x in range(startPos,len(L)): # iterate list for minimum
        if L[x] < L[minPos]: # if lesser value than minpos found
            minPos = x
            
    return minPos 

def switch(L,X,Y):
    """Takes List, Int, Int: places a select value at a given position"""
    t1 = L[X] # X for later
    L[X] = L[Y] # X to Y
    L[Y] = t1 # Y to X
    # L[Sorted] + L[Unsorted with swap of min with the first value] 
    return L
######################################################CHECKS
############################################################

def checkOmit(X):
    """X is a string user: Return whether user is private"""
    if X[-1] == "$":
        return True
    return False

def uAm():
    """return user amount"""
    temp = 0
    for key in users:
        if checkOmit(key) != True: # omit private users
            temp += 1
    return temp

##################################################READ-WRITE
############################################################

PATH = "musicrecPlus.txt" # File path, currently defaulted to the file folder

def readPrefsPrintUsers(fname): 
    '''Takes Path: Assume fname is path to an existing file in the format above.
        Print all the user names.'''
    xFile = open(fname, 'r')   # access to read the file
    uDict = {}
    
    for line in xFile: # get one line at a time
        [pers, artists] = line.split(':') # remove artists and user
        artistL = sortList(map(lambda x: x.strip(), artists.split(","))) # sort, strip, and create a list of artists
        uDict[pers.strip()] = artistL # create a dictionary of a username and their artists 
        print pers.strip() + " Loaded" #super duper print statement because Racecar
        
    xFile.close()  # important because the text book yelled at me to know so
    return uDict #return all users and their artists in a dictionary

def writePrefs():
    """Open existing or new file named fname. Write exampleFile to it."""
    xFile = open(PATH, 'w') # access a file to command and conquer its data
    
    for key in users: # for each key of dictionary user aka user and artist data
        save = key + ": " + ", ".join(users[key]) + "\n" # format dictionary entries for text
        xFile.write(save) # Add line of text assigned to save
        
    xFile.close() # Again the text book yelled at me and said this was important
    return

#######################################################PRINT
############################################################
        
def printMenu():
    """Prints Text Interface Options"""
    space()
    print "Enter a letter to choose an option:"
    printBreak()
    print "E - Manage Preferences"
    print "R - Get Recommendations"
    print "P - Show Most Popular Artists"   
    print "H - How Popular is the Most Popular"
    print "M - Which User has the Most Likes"
    print "Q - Save and Quit"
    printBreak()
    return

def printMenu2():
    """Prints Text Interface Options"""
    space()
    print "Enter a letter to choose an option:"
    printBreak()
    print "1 - New Preferences"
    print "2 - Delete Preferences"
    print "3 - Show All"
    print "4 - Privacy"
    print "Q - To Go Back"
    printBreak()
    return

def printBreak():
    """Prints A line break"""
    print "==================================="

def space(): # space spaaaaace space spaaaaaaaaaace
    """Prints A Space"""
    print
    print
    return
    
#########################################################RUN
############################################################

printBreak()
print "-Welcome to the music recommender-"
printBreak()
space()
print "<><><><><><><><><><><><><><><><><><><><><><><><><><><>"
print "NOTE: All Names and Artists ARE Case Sensitive"
print "NOTE: name + $ Will omit user excluding Manage>Show"
print "<><><><><><><><><><><><><><><><><><><><><><><><><><><>"
space()
main() # initiate!!!

############################################################
############################################################
