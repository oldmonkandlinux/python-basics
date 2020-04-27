'''
xx
xx
xx
xx
xx
xxxxx
print "L" using nested for loops
'''

numbers = [2, 2, 2, 2, 2, 5]

for x_count in numbers:
    output = ''
    for item in range(x_count):
        output = output + 'x'
    print(output)