'''
Ask for weight from the user and also ask them if it's in pounds or kgs
if it's in pounds convert to kg and vice-versa
'''

weight = input("Enter your weight: ")
unit = input("L(lbs)/K(kgs): ")

if unit == 'l' or unit == 'L' :
    your_weight = int(weight) * 0.45
    print("your weight is: " + str(your_weight) + " kgs")
elif unit == 'k' or unit == 'K' :
    your_weight = int(weight) / 0.45
    print("your weight is: " + str(your_weight) + " pounds")
