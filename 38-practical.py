'''
Practical 38

Write a Python program to read an entire text file.
'''

from os import getcwd

filename = "20-practical.py"

try:
  file = open(filename, "r")
  print("The file contents are:")
  print("======================")
  print()
  print(file.read())
except FileNotFoundError:
  print(f"'{filename}' do not exists on {getcwd()}")
