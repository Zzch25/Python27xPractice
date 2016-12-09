FEDstore = {(3): 'we'}

#ED("spam", "xsam")

def ED(first, second):
   ''' Returns the edit distance between the strings first and second.'''
   if first == '': 
      return len(second)
   elif second == '':
      return len(first)
   elif first[0] == second[0]:
      return ED(first[1:], second[1:])
   else:
      substitution = 1 + ED(first[1:], second[1:])
      deletion = 1 + ED(first[1:], second)
      insertion = 1 + ED(first, second[1:])
      return min(substitution, deletion, insertion)

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
      FEDstore[(first, second)] = fastED(first[1:], second[1:])
      return fastED(first[1:], second[1:])
   else:
      substitution = 1 + fastED(first[1:], second[1:])
      deletion = 1 + fastED(first[1:], second)
      insertion = 1 + fastED(first, second[1:])
      FEDstore[(first, second)] = min(substitution, deletion, insertion)
      return min(substitution, deletion, insertion)
   
