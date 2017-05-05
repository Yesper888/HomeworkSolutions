"""
Homework #2 - High Low Game
Description: Generate a random number.(1-100) In a loop, prompt the user
to guess the number. If the number is too big, output "Too high" and continue
the loop. If the number is too small, output "Too low" and continue the loop.
If the user guesses right, end the loop and output the number of tries it took.
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
