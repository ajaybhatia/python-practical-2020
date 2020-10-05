'''
Practical 29

Write a Python function that accepts a string and calculates number of upper case letters and lower case letters available in that string.
'''


def count_upper_lower(str):
    lower, upper = 0, 0
    for char in str:
        if char >= 'a' and char <= 'z':
            lower += 1
        elif char >= 'A' and char <= 'Z':
            upper += 1
        else:
            pass
    print(f"No. of lower-case letters are {lower}")
    print(f"No. of upper-case letters are {upper}")


string = "Write a Python function that accepts a string and calculates number of upper case letters and lower case letters available in that string."

count_upper_lower(string)
