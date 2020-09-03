'''
Practical 2

Compute area of following shapes: circle, rectangle, triangle, square, trapezoid and
parallelogram.
'''

# Circle
# PIE * radius**2
from math import pi

radius = float(input("Enter radius of circle: "))
area = pi * radius**2

print(f"Area of circle with radius {radius} is {area}\n")

# Rectangle
# 2 * (length + width)
length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle : "))

print(
    f"Area of rectangle with sides {length} and {width} is {2*(length+width)}\n")

# Triangle
# (base * height) / 2
base = float(input("Enter base of triangle   : "))
height = float(input("Enter height of triangle : "))

print(
    f"Area of triangle with base {base} and height {height} is {(base*height)/2}\n")

# Square
# side**2
side = float(input("Enter side of square : "))

print(f"Area of square with side {side} is {side**2}\n")

# Trapezoid
# (base1 + base2) / 2 * height
base1 = float(input("Enter base1 of trapezoid  : "))
base2 = float(input("Enter base2 of trapezoid  : "))
height = float(input("Enter height of trapezoid : "))

print(
    f"Area of trapezoid with base1 {base1}, base2 {base2} and height {height} is {(base1+base2)/2*height}\n")

# Parallelogram
# base * height
base = float(input("Enter base of parallelogram   : "))
height = float(input("Enter height of parallelogram : "))

print(
    f"Area of parallelogram with base {base} and height {height} is {base*height}")
