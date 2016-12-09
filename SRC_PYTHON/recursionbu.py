def dot(L,K):
    if L == []:
        return 0
    else:
        return L[0] * K[0] + dot(L[1:], K[1:])

def explode(L):
    if L == "":
        return []
    else:
        return [L[0]] + explode(L[1:])

def ind(e,L):
    if L==[]:
        return "null"
    elif e==L[0]:
        return 0
    else:
        return 1 + ind(e, L[1:])

def removeAll(e,L):
    if L==[]:
        return []
    elif(e==L[0]):
        return [] + removeAll(e, L[1:]) 
    else:
        return [L[0]]+ removeAll(e,L[1:])

def deepReverse(L):
    if L==[]:
        return []
    elif len(L[0])>1:
        return deepReverse(L[0])
    else:
        return [len(L)-1]+deepReverse(L[:-1])

def isList(L):
    ?

        
