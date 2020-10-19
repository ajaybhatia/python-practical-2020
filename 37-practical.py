'''
Practical 37

Design a Python class to reverse a string ‘word by word’.
'''


class String:
    def __init__(self, str):
        self.str = str

    def reverse_words(self):
        return " ".join([word[::-1] for word in self.str.split(' ')])


string = String("Python is object oriented language")
print(string.reverse_words())
