'''
Ask for name as input and validate it's not less than or equal to 3 characters and not more than 12 characters
using logical operators
'''

name = input("Enter you name ")
if (len(name) <= 3) or (len(name) >= 12):
    print("Name should be between 4 to 12 characters")
else:
    print("you have a valid name")