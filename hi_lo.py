#Create an algorithm that will guess the number in a specified range.

import random

print(2**20)

high = random.randint(10,100000)
low = random.randint(0,10)

print("Think of a number between {} and {}". format(low, high))
input('Hit ENTER to start')
guesses = 0
while True:
    guess = low + (high - low) // 2
    answer = input("Is the number {}? Enter l to guess lower, h to guess higher and c if the answer is correct \n".format(guess)).casefold()

    if answer == 'l':
        high = guess - 1  # Minus one ( - 1) to include the end values of the (low-high) range
        guesses = guesses + 1
    elif answer == "h":
        low = guess + 1  # plus one ( + 1) to include the end values of the (low-high) range
        guesses = guesses + 1
    elif answer == 'c':
        print('You got it in your {} guess'. format(guesses))
        break
    else:
        print('You can only type in l, h or c')

