def f(s):
    return 'a' in s

def satisfiesF(L):
    '''
    L is a list of strings;
    '''
    while 1:
        temp = []
        for each in L:
            temp.append(f(each))
            if f(each)==0:
                L.remove(each)
        if (0 in temp)==0:
            break
    return len(L)