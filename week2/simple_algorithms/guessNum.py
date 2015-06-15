#To guess number
print "Please think of a number between 0 and 100! "

strIn = 'N'
low = 0
high = 100
guessNum = (low+high)/2
while strIn != 'c':
    print "Is your secret number "+str(guessNum)+"?"
    print "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low.",
    print "Enter 'c' to indicate I guessed correctly."
    strIn = str(raw_input())
    if strIn == 'l':
        low = guessNum
    elif strIn == 'h':
        high = guessNum
    elif strIn == 'c':
        break
    else:
        print "Sorry, I did not understand your input!"
    guessNum = (low+high)/2
print "Game over.",
print "Your secret number was: "+str(guessNum)
        