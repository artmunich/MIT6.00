#find square root

##test0
#x = 23
#epsilon = 0.01
#step = 0.1
#guess = 0.0
#guessCnt = 0
#
#while guess <= x:
#    if abs(guess**2-x)<epsilon:
#        break
#    else:
#        guess += step
#        guessCnt += 1
#
#if abs(guess**2-x)>=epsilon:
#    print 'failed'
#else:
#    print 'succeeded: ' + str(guess)
#print guessCnt

#test 1
x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while guess <= x:
    print guess
    if abs(guess**2 -x) >= epsilon:
        guess += step
        print guess

if abs(guess**2 - x) >= epsilon:
    print 'failed'
else:
    print 'succeeded: ' + str(guess)


#test 2
#x = 23
#epsilon = 0.01
#step = 0.1
#guess = 0.0
#
#while abs(guess**2-x) >= epsilon:
#    if guess <= x:
#        guess += step
#    else:
#        break
#
#if abs(guess**2 - x) >= epsilon:
#    print 'failed'
#else:
#    print 'succeeded: ' + str(guess)