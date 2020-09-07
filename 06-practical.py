'''
Practical 6

Write a program to determine whether a triangle is isosceles or not?
'''

side1 = float(input("Enter side 1: "))
side2 = float(input("Enter side 2: "))
side3 = float(input("Enter side 3: "))

if side1 == side2 or side1 == side3 or side2 == side3:
    print("Triangle is isosceles")
else:
    print("Triangle is not isosceles")
