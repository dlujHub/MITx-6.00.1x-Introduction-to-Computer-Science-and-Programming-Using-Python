# Exercise: odd tuples

# (5/5 points)
# ESTIMATED TIME TO COMPLETE: 5 minutes

# Write a procedure called oddTuples, which takes a tuple as input, and returns a new tuple as output, where every other element
# of the input tuple is copied, starting with the first one. So if test is the tuple ('I', 'am', 'a', 'test', 'tuple'), then
# evaluating oddTuples on this input would return the tuple ('I', 'a', 'tuple').

def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''
    i = 0
    ans_tup = ()
    while i < len(aTup):
        ans_tup += aTup[i:i+1]
        i += 2
    return ans_tup

# Correct
