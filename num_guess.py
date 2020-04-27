'''
number guessing game with while loop
'''

secret = 10;
i = 0

while i < 3:
    guess = int(input("guess? "))
    i = i + 1
    if guess == secret:
        print("correct")
        break
else:
    print("you failed!!")
