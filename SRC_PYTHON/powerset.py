#Zachary Job
#10/19/2012

#powerset([1,2])
def powerset(X):
    if X==[]:
        return [[]]
    temp = powerset(X[1:])
    return temp + map(lambda x: [X[0]] + x, temp)

print powerset([1,2])
