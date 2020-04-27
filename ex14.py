'''
remove duplicates
'''

numbers = [1, 1, 5, 3, 2]
second_numbers = []

for number in numbers:
    if number not in second_numbers:
        second_numbers.append(number)
print(second_numbers)