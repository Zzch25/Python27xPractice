#Zachary Job
#11/15/2012

from cs5png import *

def whitespace():
    print "======================="
    for x in range(3): print
    return

def mult(c,n):
    u = c
    for x in range(n-1):
        c += u
    return c

print "MULT==================="
print "TEST 6*7 | 42"
print mult(6, 7)
print "TEST 1.5*28 | 42.0"
print mult(1.5, 28)
print "TEST 5*5 | 25"
print mult(5, 5)
whitespace()

def update(c,n):
    z = 0
    for x in range(n):
        z = z**2 + c
    return z

print "UPDATE================="
print "TEST 1@3x | 5"
print update(1,3)
print "TEST -1@3x | -1"
print update(-1,3)
print "TEST 1@10x | +#^"
print update(1,10)
print "TEST -1@10x | 0"
print update(-1,10)
whitespace()

def inMSet(c,n):
    z = 0
    for x in range(n):
        if abs(z)>2: # 2 is limit
            return False
        else: z = z**2+c
    return True

print "INMSET================="
print "TEST ((0+0j),25) | TRUE"
print inMSet((0+0j),25)
print "TEST ((3+4j),25) | FALSE"
print inMSet((3+4j),25)
print "TEST ((0.3j+-0.5j),25) | TRUE"
print inMSet((0.3j+-0.5j),25)
print "TEST ((-0.7+0.3j),25) | FALSE"
print inMSet((-0.7+0.3j),25)
print "TEST ((0.42+0.2j),25) | TRUE"
print inMSet((0.42+0.2j),25)
print "TEST ((0.42+0.2j),25) | FALSE"
print inMSet((0.42+0.2j),50)
whitespace()


######################################EXAMPLE CODE
##################################################

def weWantThisPixel( col, row ):
    """ a function that returns True if we want
         the pixel at col, row and False otherwise
    """
    if col%10 == 0  or  row%10 == 0:
        return True
    else:
        return False

def test():
    """ a function to demonstrate how
        to create and save a png image
    """
    width = 300
    height = 200
    image = PNGImage(width, height)
    # create a loop in order to draw some pixels
    for col in range(width):
        for row in range(height):
            if weWantThisPixel( col, row ) == True:
                image.plotPoint(col, row)
    # we looped through every image pixel; we now write the file
    image.saveFile("test.png")

print "PRINTING EXAMPLE======="
test()
print "FINISHED"
whitespace()

##################################################
##################################################

def scale(pix, pixMax, floatMin, floatMax):
    n = abs(floatMin)+abs(floatMax)
    return floatMin + n*(pix*1.0/pixMax*1.0)

print "SCALE=================="
print "(100, 200, -2.0, 1.0) | -0.5"
print scale(100, 200, -2.0, 1.0)
print "(100, 200, -1.5, 1.5) | 0.0"
print scale(100, 200, -1.5, 1.5)
print "(100, 300, -2.0, 1.0) | -1.0"
print scale(100, 300, -2.0, 1.0)
print "(25, 300, -2.0, 1.0) | -1.75"
print scale(25, 300, -2.0, 1.0)
print "(299, 300, -2.0, 1.0) | 0.99..."
print scale(299, 300, -2.0, 1.0)
whitespace()


##############################################MSET
##################################################

def mset(width, height):
    image = PNGImage(width, height)
    for col in range(width):
        for row in range(height):
            if weWantThisPixel( col, row ) == True:
                image.plotPoint(col, row)
    image.saveFile("mset.png")

def nicePixel(col,row):
    return True #because I can

print "PRINTING MSET=========="
mset(200, 300)
print "FINISHED"
whitespace()


