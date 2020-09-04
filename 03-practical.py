'''
Practical 3

Compute volume of following 3D shapes: cube, cylinder, cone and sphere.
'''

from math import pi

height = float(input("Enter height of 3D shape: "))
radius = float(input("Enter radius of 3D shape: "))

# Cube
# side**3
print(f"Volume of cube with side {height} is {height**3}")

# Cylinder
# PIE * radius**2 * height
print(
    f"Volume of cylinder with radius {radius} and height {height} is {pi*radius**2*height}")

# Cone
# PIE * radius**2 * (height/3)
print(
    f"Volume of cone with radius {radius} and height {height} is {pi*radius**2*(height/3)}")

# Sphere
# 4/3 * PIE * radius**3
print(
    f"Volume of sphere with radius {radius} is {(4/3)*pi*radius**3}")
