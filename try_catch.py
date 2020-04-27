try:
    age = int(input("age?: "))
    income = 2000
    risk = income/age
    print(age)

except ValueError:
    print("enter a numerical value")
except ZeroDivisionError:
    print("division by zero is not possible")
