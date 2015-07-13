def myLog(x,b):
    for i in range(x):
        if b**i==x:
            return i
        elif b**i>x:
            return i-1