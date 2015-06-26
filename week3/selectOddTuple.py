def oddTuples(aTup):
    temp=() # the empty tuple
    for i in range(len(aTup)):
        if i%2==0:
            temp = temp+ (aTup[i],)
    return temp
    