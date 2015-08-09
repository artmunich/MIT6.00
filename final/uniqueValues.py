def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''
    result = []
    valFreqDic = {}
    
    #get frequency of each value of aDict
    for ival in aDict.itervalues():
        valFreqDic[ival] = valFreqDic.get(ival,0) + 1
    
    #get keys corresponding to unique values
    for ikey in valFreqDic.iterkeys():
        if valFreqDic[ikey] == 1:
            for it in aDict.iteritems():
                if ikey == it[-1]:
                    result.append(it[0])
    
    #sort in increasing order
    swapFlag = True
    while swapFlag:
        swapFlag = False
        for i in range(len(result)-1):
            if result[i]>result[i+1]:
                temp = result[i+1]
                result[i+1] = result[i]
                result[i] = temp
                swapFlag = True
    
    return result