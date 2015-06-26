def factI(n):
    """assumes that n is an int > 0
       returns n!
       Iterative version"""
    res = 1
    while n > 1:
        res = res * n
        n -= 1
    return res

def factR(n):
    """assumes that n is an int > 0
       returns n!
       Recursive version"""
    if n == 1:
        return n
    return n*factR(n-1)
