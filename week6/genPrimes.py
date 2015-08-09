def getOdd():
    a = 1
    while True:
        yield a
        a = a +2

#Another version        
def genPrimes():
    p = []
    x = 1
    while True:
        x = x + 1
        pLen = len(p)
        testLen = 0
        for each in p:
            if x%each != 0:
                testLen += 1
        if pLen == testLen:
            p.append(x)
            yield x