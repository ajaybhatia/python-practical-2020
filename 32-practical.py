'''
Practical 32

Solve the Fibonacci sequence using recursion.

1 2 3 4 5  6  7
1 2 3 5 8 13 21 .....

f(1) = 1
f(2) = 2
f(x) = f(x-1) + f(x-2)
'''


def fib(x):
    if x == 1:
        return 1
    elif x == 2:
        return 2
    else:
        return fib(x-1) + fib(x-2)


for i in range(1, 30):
    print(fib(i))
