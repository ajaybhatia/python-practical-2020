'''
Practical 7

Print multiplication table of a number input by the user.
'''

number = int(input("Enter a number to print table: "))

for i in range(1, 11):
    print(f"{number} X {i} = {number*i}")
