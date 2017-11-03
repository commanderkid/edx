#Write a procedure called oddTuples, which takes a tuple as input, and returns a new tuple as output, 
#where every other element of the input tuple is copied, starting with the first one. 
#So if test is the tuple ('I', 'am', 'a', 'test', 'tuple'), 
#then evaluating oddTuples on this input would return the tuple ('I', 'a', 'tuple').


#from zero to end of tuple with step of two 
#def oddTuples(aTup):
#    newTup = aTup[0 :: 2]
#    return newTup

# i want to use recursion
def oddTuples(aTup, i = 0, newTup = ()):
    if i < len(aTup):
        newTup += (aTup[i],)
        # so we can use (variable,)
        return oddTuples(aTup, i + 2, newTup)
    else:
        return newTup
