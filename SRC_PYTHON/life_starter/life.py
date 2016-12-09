# life.py - Game of Life lab
# Zachary Job
# 11/29/2012

import random
import sys

def printBoard( A ):
    """ this function prints the 2d list-of-lists
        A without spaces (using sys.stdout.write)
    """
    for row in A:
        for col in row:
            sys.stdout.write( str(col) )
        sys.stdout.write( '\n' )

def createOneRow(width):
    """ returns one row of zeros of width "width"...  
         You should use this in your
         createBoard(width, height) function """
    row = []
    for col in range(width):
        row += [0]
    return row

		
def createBoard(width, height):
    """ returns a 2d array with "height" rows and "width" cols """
    A = []
    for row in range(height):
        A += [[0]*width]   # What do you need to add a whole row here?
    return A

def diagonalize(width,height):
    """ creates an empty board and then modifies it
        so that it has a diagonal strip of "on" cells.
    """
    A = createBoard( width, height )
    
    for row in range(height):
        for col in range(width):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0     

    return A

def innerCells(width,height):
    
    A = createBoard(width,height)
    
    for row in range(height):
        for col in range(width):
            if row == 0 or row == height-1 or col == 0 or col == width-1:
                A[row][col] = 0
            else:
                A[row][col] = 1

    return A

def randomCells(width,height):
    
    A = createBoard(width,height)
    
    for row in range(height):
        for col in range(width):
            if row == 0 or row == height-1 or col == 0 or col == width-1:
                A[row][col] = 0
            else:
                A[row][col] = random.choice([0,1])

    return A

def copy(A):
    height = len(A)
    width = len(A[0])
    L = createBoard(width,height)
    
    for row in range(height):
        for col in range(width):
            L[row][col] = A[row][col]

    return L

def innerReverse(L):
    A = copy(L)  
    height = len(L)
    width = len(L[0])
    
    for row in range(height):
        for col in range(width):
            if  row == 0 or row == height-1 or col == 0 or col == width-1:
                A[row][col] = 0
            else:
                if A[row][col] == 0:
                    A[row][col] = 1
                else:
                    A[row][col] = 0
            
    return A

def next_life_generation(L):
    A = copy(L)
    height = len(A)
    width = len(A[0])

    for row in range(height):
        for col in range(width):
            if row == 0 or row == height-1 or col == 0 or col == width-1:
                A[row][col] = 0
            else:
                temp = neighboorLoveMe(A,row,col)
                if temp < 2:
                    A[row][col] = 0
                elif temp == 3:
                    A[row][col] = 1
                else:
                    A[row][col] = 0
                                 
    return A

def neighboorLoveMe(L,X,Y): ###prob
    count = 0

    for row in range(Y-1,Y+2):
        for col in range(X-1,X+2):
            print "col " + str(col) + " " + "row " + str(row)
            if col == X and row == Y:
                count += 0
            else:
                if L[row][col] == 1:
                    print "go"
                    count += 1   
    return count
    
print "Createboard"
printBoard(createBoard(5, 5))
print "Diagonalize"
printBoard(diagonalize(5, 5))
print "Inner Cells"
printBoard(innerCells(5, 5))
print "Random Cells"
printBoard(randomCells(5, 5))
print "Copy"
printBoard(copy(createBoard(5, 3)))
print "Inner Reverse"
printBoard(innerReverse(createBoard(5, 4)))



