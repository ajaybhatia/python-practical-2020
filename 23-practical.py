'''
Practical 23

Display word after Sorting in alphabetical order.
'''

word = input("Enter a word: ")

word = list(word)
word.sort()
word = "".join(word)

print(word)
