"""
Homework #3 - Fibonacci Counter
*Done naively
Description: Prompt a user for the a number n. Output the first n fibonacci
numbers. Solution must be done with some kind of recursion.
"""

def fib(n):
    if(n<3):
        return 1
    else:
        return fib(n-1)+fib(n-2)

def main():
    print("Input a number and I will count that many fibonacci numbers")
    print("Try to limit to under 30")
    x = int(input("Input: "))
    for i in range(x):
        print(fib(i))

main()
