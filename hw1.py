"""
Homework #1 - Simple Calculator
Description: Write a program that takes as input 2 non-zero whole numbers.
Output the result of addition, subtraction, multiplication, normal divison,
floor division, modulo, and exponentiation of those 2 operands.
"""

print("Input 2 non-zero whole numbers")

a = int(input("INPUT THE FIRST NUMBER: "))

b = int(input("INPUT THE SECOND NUMBER: "))

print("Addition:",a+b)
print("Subtraction:",a-b)
print("Multiplication:", a*b)
print("Normal Division:",a/b)
print("Floor Division:",a//b)
print("Modulo:",a%b)
print("Exponentiation:",a**b)
