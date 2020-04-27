'''
Ask for name as input and validate it's not less than or equal to 3 characters and not more than 12 characters
using comparison operators
'''

name = input("Enter you name ")
if len(name) <= 3:
    print("Cannot be less than or equal to 3 characters")
elif len(name) >= 12:
    print("Cannot be more than or equal to 12 characters")
else:
    print("you have a valid name")