#6\. Shape Area Calculator (Polymorphism)
#A graphics application needs to calculate the area of different shapes. Create classes Circle, Rectangle, and Triangle, each having an area() method. Demonstrate
#polymorphism by calling the same method for different objects.



import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 8)]

for shape in shapes:
    print("Area:", shape.area())
