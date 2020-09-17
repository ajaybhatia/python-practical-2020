'''
Practical 21

Determine whether a string is palindrome or not.
'''

string = "Able was I ere I saw Elba"
reverse_string = "".join(reversed(string))

if string.lower() == reverse_string.lower():
    print(f"String '{string}' is palindrome")
else:
    print(f"String '{string}' is not palindrome")
