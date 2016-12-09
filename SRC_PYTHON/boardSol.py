#boardSol.py
#
#Zachary Job
#12/11/2012

class board:

    def __init__(self, width=7, height=6):
        """creates 2D list according to inputed or default height and width"""
        self.c4board = []
        for row in range(width):
            self.c4board += [[" "]*height]
        self.width = width
        self.height = height
        
    def __repr__(self):
        """return the 2D array so that it appears to be a connect four board"""
        temp=""
        for row in range(self.height):
            for col in range(self.width):
                temp += "|" + self.c4board[col][row]
            temp += "|"
            temp += "\n"
        temp+="-"*(self.width*2+1) + "\n"
        for row in range(self.width):
            temp+= " " + str(row+1)
        return temp

    def clearBoard(self):
        """clears board when called"""
        for w in range(self.width):
            for h in range(self.height):
                self.delMove(w)
                
    
    def allowsMove(self,col):
        """returns true if the column is open else false"""
        if self.c4board[col-1][0] == " ":
                return True
        return False
    
    def addMove(self,col,ox):
        """add player piece to given column above previous pieces opr at start"""
        for height in range(len(self.c4board[col-1])):
            temp = len(self.c4board[col-1])-1-height
            if self.c4board[col-1][temp] == " ":
                self.c4board[col-1][temp] = ox
                return
    
    def setBoard(self, moveString):
        """a tester utility which inputs a piece at a given position"""
        nextCh = 'X'   # start by playing 'X'
        for colString in moveString:
            col = int(colString)
            if 0 <= col <= self.width:
                self.addMove(col, nextCh)
            if nextCh == 'X': nextCh = 'O'
            else: nextCh = 'X'

    def delMove(self,col):
        """removes a piece from the top of a column"""
        for height in range(len(self.c4board[col-1])):
            if self.c4board[col-1][height] != " ":
                self.c4board[col-1][height] = " "
                return
    
    def winsFor(self, ox):
        """checks if a piece has achieved four in a row"""
        cA=4

        #################V
        
        for h in range(self.height):
            i = 0
            for w in range(self.width):
                if self.c4board[w][h] == ox:
                    i+=1
                else:
                    i=0
                if i == cA:
                    return True
    
        #################H
       
        for w in range(self.width):
            i = 0
            for h in range(self.height):
                if self.c4board[w][h] == ox:
                    i+=1
                else:
                    i=0
                if i == cA:
                    return True   
        
        ##############DBRL

        for w in range(self.width):
            for h in range(self.height):
                if h >= cA and self.width - w >= cA:
                    i = 0
                    for x in range(cA):
                        if self.c4board[w+x][h-x] == ox:
                            i+=1
                        else:
                            i=0
                        if i == cA:
                            return True

        ##############DBLR

        for w in range(self.width):
            for h in range(self.height):
                if self.height - h >= cA and self.width - w >= cA:
                    i = 0
                    for x in range(cA):     
                        if self.c4board[w+x][h+x] == ox:
                            i+=1
                        else:
                            i=0
                        if i == cA:
                            return True

                            
        return False;
    
    def hostGame(self):
        """runs a game of connect four using previous methods"""

        self.clearBoard()
        
        pl()
        print "######Connect  Four###### \nOptions: (#[row]/Q[quit])\n########X  Starts########"
        pl()

        eGame = False
        wGame = False
        turn = 0

        while eGame == False or wGame == False:
            if eGame == False and wGame == False:
                if turn == 0: print "X: "
                else: print "O: "
                uIn = raw_input()
                pl()
                if str(uIn).lower() == "q":
                    eGame = True
                    wGame = True
                else:
                    if uIn.isdigit() == False:
                        print "Invalid Input"
                    elif int(uIn) < 1 or int(uIn) > self.width:
                        print "Invalid Input"
                    else:

                        if self.allowsMove(int(uIn)) == True:
                            if turn == 0:
                                self.addMove(int(uIn), "X")
                                if self.winsFor("X") == True:
                                    wGame = True
                                turn = 1
                            else:
                                self.addMove(int(uIn), "O")
                                if self.winsFor("O") == True:
                                    wGame = True
                                turn = 0
                        else:
                            print "--Unavailable--"

                        print self

                    pl()
            else:
                if turn == 0: print "O Wins"
                else: print "X Wins"
                eGame = True

                pl()
        return

def pl():
    print "-------------------------"

b=board()
b.hostGame()

