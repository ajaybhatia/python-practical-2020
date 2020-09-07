'''
Practical 8

Compute sum of natural numbers from one to n number.
'''

from functools import reduce
n = int(input("Enter value of n: "))

# Method 1
total = 0
for i in range(1, n+1):
    total += i  # total = total + i

print(f"Sum of first {n} natural numbers is {total}")

# Method 2
print(f"Sum of first {n} natural numbers is {sum([i for i in range(1, n+1)])}")

# Method 3
print(
    f"Sum of first {n} natural numbers is {reduce(lambda x, y: x + y, [i for i in range(1, n+1)])}")
