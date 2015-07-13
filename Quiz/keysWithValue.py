def keysWithValue(aDict,target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    keysWant = []
    for eachKey in aDict.iterkeys():
        if aDict[eachKey] == target:
            keysWant.append(eachKey)
    keysWant.sort()
    return keysWant