'''
Practical 10

Compute factorial of a given number
'''

from functools import reduce

n = int(input("Value of n: "))

# Method 1: Using Iterative Approach


def factorial1(n):
    prod = 1
    for i in range(1, n+1):
        prod *= i
    return prod


print(f"Factorial of {n} is {factorial1(n)}")


# Method 2: Using Recursion
def factorial2(n):
    if n == 1:
        return 1
    else:
        return n * factorial2(n-1)


print(f"Factorial of {n} is {factorial2(n)}")

# Method 3: Using reduce functool method
print(
    f"Factorial of {n} is {reduce(lambda x, y: x*y, [i for i in range(1, n+1)])}")
