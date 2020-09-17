'''
Practical 19

Count occurrence of vowels (a, e, i, o, u).
'''

count = 0

string = "Welcome to the Python Wiki, a user-editable compendium of knowledge based around the Python programming language. Some pages are protected against casual editing."

# Using in-built function (count)
for vowel in ['a', 'e', 'i', 'o', 'u']:
    count += string.count(vowel)

print(f"Total vowels present in the given text is {count}")


# Using if statement
count = 0
for c in string:
    if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
        count += 1

print(f"Total vowels present in the given text is {count}")
