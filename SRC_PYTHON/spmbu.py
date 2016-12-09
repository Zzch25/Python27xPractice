#Zachary Job
#9/27/12

##############################################################################
###This revision was made in case of inability to compact into one function###
##############################################################################

Inf = float("inf")

FiveDists  = {("A","A"):0, ("A","B"):1, ("A","C"):3, ("A","D"):7 , ("A","E"):Inf,
               ("B","A"):Inf, ("B","B"):0, ("B","C"):42, ("B","D"):6, ("B","E"):27,
               ("C","A"):Inf, ("C","B"):Inf, ("C","C"):0, ("C","D"):2, ("C","E"):13,
               ("D","A"):Inf, ("D","B"):Inf, ("D","C"):Inf, ("D","D"):0, ("D","E"):5,
               ("E","A"):Inf, ("E","B"):Inf, ("E","C"):Inf, ("E","D"):Inf, ("E","E"):0}

FiveCities = ["A", "B", "C", "D", "E"]

#shortestPath(FiveCities, FiveDists)
#
#Recurse once FiveCities has been looped splicing cities
#map(lambda u: map(lambda e: distances[(u,e)], FiveCities[0:]), cities[0:])   returns the values
#temp = filter(lambda z: z != 0, map(lambda u: map(lambda e: distances[(u,e)], FiveCities[0:]), cities[0:]))
#

def shortestPath(cities, distances):
    temp = map(lambda q: filter(lambda i: i != 0, q), map(lambda u: map(lambda e: distances[(u,e)], FiveCities[0:]), cities[0:])[0:])
    print "temp"
    return min(repl(temp))

#repl([0,1,2,3,4])
#
#Takes filtered list and finds list of paths
#add dis first to (iterate) second position
#A-B(B-C-D, B-D, B-E) A-C(C-D C-E) ETC
#

def repl(x):
    
    

print shortestPath(FiveCities, FiveDists)
               

def shortestPathEX(cities, dists):
    if len(Cities) == 1: return 0
    return min(map(lambda cit: dists[(cities[0],cities[cit])] + shortestPathEX(cities[cit:], dists))"dist to cit + shortest from cit to end",range(1, len(Cities))))
