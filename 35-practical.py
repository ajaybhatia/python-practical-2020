'''
Practical 35

Design a Python class named Rectangle, constructed by a length & width, also design
a method which will compute the area of a rectangle.
'''


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length*self.width


rec1 = Rectangle(5.6, 9.3)
print(f"Area of rectangle 1 is {rec1.area()}")

rec2 = Rectangle(5, 9)
print(f"Area of rectangle 2 is {rec2.area()}")
