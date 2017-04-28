"""
Separate File for Geometric Objects
"""
import math
class GeometricObject:
    count = 0
    def __init__(self,color):
        self._color = color
        GeometricObject.count+=1

    def __str__(self):
        return "Geometric Object with color "+self._color

    def getArea(self):
        pass

    @staticmethod
    def number():
        return GeometricObject.count

class Triangle(GeometricObject):
    def __init__(self,color,s1,s2,s3):
        super().__init__(color)
        self._s1 = s1
        self._s2 = s2
        self._s3 = s3

    def getArea(self): #Heron's Formula
        p = (self._s1+self._s2+self._s3)/2
        return math.sqrt(p*(p-self._s1)*(p-self._s2)*(p-self._s3))

class Rectangle(GeometricObject):
    def __init__(self,color,length,width):
        super().__init__(color)
        self._length = length
        self._width = width

    def getArea(self):
        return self._length*self._width

class Circle(GeometricObject):
    def __init__(self,color,radius):
        super().__init__(color)
        self._radius = radius

    def getArea(self):
         return self._radius*self._radius*math.pi
