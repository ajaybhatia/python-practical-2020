'''
Practical 12

Print Geometric and Harmonic means of a series input by the user.

GM = (x1*x2*x3*....*xn)**(1/n)
HM = n / [(1/x1)+(1/x2)+(1/x3)+...+(1/xn)]
'''

from functools import reduce

series = [int(i) for i in input(
    "Enter series (seperate each digit by space): ").split(" ")]

n = len(series)

# Geometric Mean
product = reduce(lambda x, y: x*y, series)
gm = product**(1/n)
print(f"Geometric mean of a series {series} is {gm}")

# Harmonic Mean
sum = reduce(lambda x, y: x+1/y, series, 0)
hm = n / sum
print(f"Harmomic mean of a series {series} is {hm}")
