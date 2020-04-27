'''
xxxxx
xx
xxxxx
xx
xx

print the above pattern

'''

numbers = [5, 2, 5, 2, 2]

for item in numbers:
    print("x" * item)


'''
without the "*" feature
'''

for x_count in numbers:
    output = ''
    for count in range(x_count):
        output = output + 'x'
    print(output)