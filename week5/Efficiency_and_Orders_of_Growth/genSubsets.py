def genSubsets(L):
    if len(L) == 0:
        return [[]]
    smaller = genSubsets(L[:-1])
    print "Smaller:",smaller
    lastElement = L[-1:]
    new = []
    for small in smaller:
        new.append(small+lastElement)
        print new
    return smaller+new