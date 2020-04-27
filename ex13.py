'''
find the largest number in a given list
'''

numbers = [1, 15, 2, 3]
max = numbers[0]

for number in numbers:
    if number > max:
        max = number
print(max)