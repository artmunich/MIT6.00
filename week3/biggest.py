def biggest(aDict):
    
    #Initialization
    temp=0
    bValue=None
    
    for keyEle in aDict.keys():
        if len(aDict[keyEle])>=temp:
            bValue=keyEle
            temp=len(aDict[keyEle])
    return bValue