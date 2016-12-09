print "one"
Q = [1,2,3]
print "Q: [1,2,3]"
W = Q[1:]
print "W=Q[1:]"
R=Q
print "R=Q"
R[1] = 5
print "R[1] = 5"
print "Q:" + str(Q)
print "R:" + str(R)
print "W:" + str(W)
print

def one():
    x=0
    for i in range(5):
        x += i
    return x

print "two"
print one()
print

M=[1,2,3]

def two(L):
    for x in range(len(L)):
        L[x] += 1
    return

print "three"
print M
two(M)
print M
print
    
M=[1,2,3]

def three(L):
    temp = []
    for x in range(len(L)):
        temp += [L[x]+1]
    return temp

print "four"
print M
print three(M)
print M
print

def four():
    N = 5
    T = 1
    for x in range(N):
        T = T*(x+1)
    return T

print "five"
print four()
print

def five():
    cur = 1
    i = 1
    prev = 0
    numtm = 5
    while i != numtm:
        print "i,prev,cur " + str(i) + " " + str(prev) + " " + str(cur)
        cur = cur + prev
        prev = cur - prev
        i += 1
    print str(numtm) + " " + str(cur) 

print "six"
print five()
print
