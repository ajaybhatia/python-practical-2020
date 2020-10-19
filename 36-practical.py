'''
Practical 36

Design a Python class named Circle constructed by a radius and two methods which
will compute the area and the perimeter of a circle.
'''

from math import pi


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return 2*pi*self.radius

    def area(self):
        return pi*self.radius**2


c1 = Circle(10)
print(f"Perimeter of circle object c1 is {c1.perimeter()}")
print(f"Area of circle object c1 is {c1.area()}")

c2 = Circle(5)
print(f"Perimeter of circle object c2 is {c2.perimeter()}")
print(f"Area of circle object c2 is {c2.area()}")
