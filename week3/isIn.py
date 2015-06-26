def isIn(char,aStr):
    midLen = len(aStr)/2
    if aStr=='':
        return False
    if len(aStr)==1:
        return char==aStr
    if char==aStr[midLen]:
        return True
    if char<aStr[midLen]:
        return isIn(char,aStr[0:midLen])
    if char>aStr[midLen]:
        return isIn(char,aStr[midLen+1:])
        