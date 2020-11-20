'''
Practical 39

Design a Python program to read first n lines of a text file.
'''

from os import getcwd

filename = "20-practical.py"
n = int(input("Enter number of lines to read: "))
current_line_number = 0

try:
  file = open(filename, "r")
  print(f"The first {n} lines of {filename} are:")
  print("------------------------------------------------------")
  print()
  # Main logic
  for line in file.readlines():
    if n == current_line_number:
      break
    else:
      print(line)
    current_line_number += 1
except FileNotFoundError:
  print(f"'{filename}' do not exists on {getcwd()}")

