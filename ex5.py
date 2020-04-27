'''
price of a house is 1000, if the buyer has good_credit he has to make a dp of 10% else a dp of 20%
formatted output
'''

price = 1000
good_credit = True

if good_credit:
    dp = 0.1 * int(price)

else:
    dp = 0.2 * int(price)
print(f"down payment: ${dp}")