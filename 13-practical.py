'''
Practical 13

Evaluate the following expressions:
a. x-x**2/2!+x**3/3!- x**4/4!+... x**n/n!
b. x-x**3/3!+x**5/5!- x**7/7!+... x**n/n!
'''


def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)


x = int(input("Enter value of x: "))
n = int(input("Enter value of n: "))

# a. x-x**2/2!+x**3/3!- x**4/4!+... x**n/n!
sum = 0
for i in range(1, n+1):
    if x % 2 == 0:
        sum -= (x**i)/fact(i)
    else:
        sum += (x**i)/fact(i)

print(f"Sum of series (a) is {sum}")

# b. x-x**3/3!+x**5/5!- x**7/7!+... x**n/n!
sum, step = 0, 1
for i in range(1, n+1, 2):
    if step % 2 == 0:
        sum -= (x**i)/fact(i)
    else:
        sum += (x**i)/fact(i)
    step += 1

print(f"Sum of series (b) is {sum}")
