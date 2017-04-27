"""
Homework #2 - High Low Game
"""

import random

x = random.randrange(1,100)
guess = 0
tries = 0

while(guess != x):
    guess = int(input("Guess a number: "))
    tries += 1
    if(guess < x):
        print("Too low")
    elif(guess > x):
        print("Too high")

print("Congratulations! You got the number in",tries,"tries!")
