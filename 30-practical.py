'''
Practical 30

To find the Max of three numbers using functions.
'''


def max_of_2(a, b):
    if a > b:
        return a
    else:
        return b


def max_of_3(a, b, c):
    return max_of_2(max_of_2(a, b), max_of_2(b, c))


x, y, z = 3, 5, 4

print(f"Max among {x}, {y} and {z} is {max_of_3(x, y, z)}")
