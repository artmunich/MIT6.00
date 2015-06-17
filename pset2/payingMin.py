#payingMin.py
balance =4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
print 'balance = ' + str(balance)
print 'annualInterestRate = ' + str(annualInterestRate)
print 'monthlyPaymentRate = ' + str(monthlyPaymentRate)
#---------------STRAT FROM HERE---------------
totalPaid = 0.0
for i in range(1,13):
    monthlyPayment = balance * monthlyPaymentRate
    totalPaid = totalPaid + monthlyPayment
    balance = balance - monthlyPayment
    balance = balance + balance * (annualInterestRate/12)
    print 'Month: ' + str(i)
    print 'Minum monthly payment: ' + str(round(monthlyPayment,2))
    print 'Remaining balance: ' + str(round(balance,2))
print 'Total paid: ' + str(round(totalPaid,2))
print 'Remaining balance: ' + str(round(balance,2))