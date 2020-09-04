'''
Practical 5

Print numbers up to N which are not divisible by 3, 6, 9,, e.g., 1, 2, 4, 5, 7,....
'''

n = int(input("Enter limit: "))

for num in range(1, n+1):
    if num % 3 != 0 and num % 6 != 0 and num % 9 != 0:
        print(num, end=", ")
