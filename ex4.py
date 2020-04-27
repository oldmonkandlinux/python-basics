'''
price of a house is 1000, if the buyer has good_credit he has to make a dp of 10% else a dp of 20%
'''

price = 1000
good_credit = False

if good_credit:
    dp = 0.1 * int(price)
    print('down payment is ' + str(dp))
else:
    dp = 0.2 * int(price)
    print('down payment is ' + str(dp))