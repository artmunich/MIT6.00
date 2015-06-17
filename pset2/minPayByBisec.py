#minPayByBisec.py
#Using bisection search to make the program faster
balance = 999999
annualInterestRate = 0.18

#----------START FROM HERE-------
low = balance/12
high = balance*(1+annualInterestRate/12)**12/12
monthlyPayment = (low + high)/2.
epsilon = 0.01
initialBalance = balance

while 1:
    for i in range(1,13):
        balance = balance - monthlyPayment
        balance = balance*(1+annualInterestRate/12)
    if abs(balance)<=epsilon:
        break
    elif balance>epsilon:
        low = monthlyPayment
    else:
        high = monthlyPayment
    monthlyPayment = (low+high)/2.
    balance = initialBalance
    
print 'Lowest Payment: ' + str(round(monthlyPayment,2))