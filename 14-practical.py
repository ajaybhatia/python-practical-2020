'''
Practical 14

Print all possible combinations of 4, 5, and 6.

456
465
546
564
645
654
'''

from itertools import permutations

number = 456
digits = [str(i) for i in str(number)]

for number in permutations(digits):
    print("".join(number))
