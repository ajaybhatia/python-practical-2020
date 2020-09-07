'''
Practical 9

Print Fibonacci series up to n numbers e.g. 0 1 1 2 3 5 8 13.....n

Logic upto 10
Untill c > 10

a b c
  a b c
    a b c
      a b c
        a b c
0 1 1 2 3 5 8
'''

a, b, c = 0, 1, 0

n = int(input("Enter value of n: "))

print(f"{a} {b}", end=" ")
while True:
    c = a + b
    if c > n:
        break
    print(c, end=" ")
    a, b = b, c
