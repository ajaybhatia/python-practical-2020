'''
Practical 33

Get the factorial of a non-negative integer using recursion.
'''


def fact(x):
    if x == 0:
        return 1
    else:
        return x * fact(x-1)


n = int(input("Enter a number: "))

if (n >= 0):
    print(f"Factorial of {n} is {fact(n)}")
else:
    print(f"No factorial of {n} because {n} is a negative number")
