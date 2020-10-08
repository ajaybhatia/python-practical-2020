'''
Practical 31

Multiply all the numbers in a list using functions.
'''

from functools import reduce

# Function 1


def multiply_1(numbers):
    prod = 1
    for number in numbers:
        prod *= number
    return prod


# Function 2
def multiply_2(numbers):
    return reduce(lambda number, prod: number*prod, numbers)


print(multiply_1([2, 4, 6, 10]))
print(multiply_2([2, 4, 6, 10]))
