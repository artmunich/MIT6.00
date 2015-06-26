def gcdIter(a,b):
    temp=min(a,b)
    while temp>0:
        if a%temp==0 and b%temp ==0:
            return temp
        temp -= 1