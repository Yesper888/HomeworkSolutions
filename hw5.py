"""
Homework #5 - Find Area of geometric objects
Description: Prompt the user for a number of different objects. Ask the user
for the type, color, and size parameters. Then, using a separate file of
Geometric Objects, instantiate each object and output the total area of all
the objects.
"""
from GeometricObject import *

def main():
    n = int(input("How many objects? "))
    shapes = []
    for i in range(1,n+1):
        objectType = input("Input Shape "+str(i)+"'s Type:").lower()
        objectColor = input("Input Shape "+str(i)+"'s Color: ").lower()
        if(objectType=="triangle"):
            sides = input("Enter 3 sides separated by spaces: ").split()
            shapes.append(Triangle(objectColor,
                                   float(sides[0]),
                                   float(sides[1]),
                                   float(sides[2])))
        elif(objectType=="rectangle"):
            length = float(input("Enter length: "))
            width = float(input("Enter width: "))
            shapes.append(Rectangle(objectColor,length,width))
        elif(objectType=="circle"):
            radius = float(input("Enter radius: "))
            shapes.append(Circle(objectColor,radius))
        else:
            print("Invalid Shape Type")
            return
    total = 0
    for shape in shapes:
        total+=shape.getArea()
    print("Total Area:",total)
            

main()
