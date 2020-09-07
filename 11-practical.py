'''
Practical 11

Count occurrence of a digit 5 in a given integer number input by the user.
'''

# Method 1: Hard way
number = int(input("Enter a number: "))
count, temp = 0, number

while temp > 0:
    digit = temp % 10
    if digit == 5:
        count += 1
    temp //= 10


print(f"Occurance of 5 in {number} is {count}")


# Method 2: Easy way (using string)
number = input("\nEnter a number: ")
print(f"Occurance of 5 in {number} is {number.count('5')}")
