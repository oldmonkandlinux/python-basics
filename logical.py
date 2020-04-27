'''
Demonstrating logical operators
'''

has_high_income = False
has_good_credit = True
has_criminal_record = False

'''
AND
'''
if has_high_income and has_good_credit:
    print("eligible for loan...AND")

'''
OR
'''
if has_high_income or has_good_credit:
    print("eligible for loan...OR")

'''
NOT
'''
if has_good_credit and not has_criminal_record:
    print("eligible for loan...NOT")