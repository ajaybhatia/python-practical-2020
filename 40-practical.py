'''
Practical 40

Construct a Python program to write and append text to a file and display the text.
'''

from os import getcwd

filename = "/tmp/names.txt"
try:
  file = open(filename, "a")
  # Write names in a file "/tmp/names.txt"
  while True:
    name = input("Enter a name: ")
    if name == "0":
      break
    file.write(name + "\n")
  file.close()

  # Read file contents and print them on screen
  print(f"{filename} contains following contents:")
  print("----------------------------------------\n")
  file = open(filename, "r")
  print(file.read())
except FileNotFoundError:
  print(f"'{filename}' do not exists on {getcwd()}")
