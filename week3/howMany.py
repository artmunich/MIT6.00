def howMany(aDict):
    sumAll=0
    for keyEle in aDict.key():
        sumAll = sumAll + len(aDict[keyEle])
    return sumAll