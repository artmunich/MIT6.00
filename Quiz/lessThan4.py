def lessThan4(aList):
    '''
    aList: a list of strings
    '''
    result = []
    for chars in aList:
        if len(chars)<4:
            result.append(chars)
    return result