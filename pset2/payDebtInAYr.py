#PayDebtInAYr.py
balance = 999999
annualInterestRate = 0.18

#-------------START FROM HERE------
monthlyPayment = 10.0
initialBalance = balance
while 1:
    for i in range(1,13):
        balance = balance - monthlyPayment
        balance = balance*(1+annualInterestRate/12)
    if balance <= 0:
        break
    else:
        monthlyPayment = monthlyPayment + 0.01
        balance = initialBalance
print 'Lowest Payment: ' + str(monthlyPayment)