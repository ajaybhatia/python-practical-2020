'''
Practical 20

Count total number of vowels in a word.
'''


def count_vowels(word):
    count = 0
    for vowel in ['a', 'e', 'i', 'o', 'u']:
        count += word.count(vowel)
    return count


string = "Welcome to the Python Wiki, a user-editable compendium of knowledge based around the Python programming language. Some pages are protected against casual editing."

for word in string.split(" "):
    print(f"Vowels in '{word}' are {count_vowels(word)}")
