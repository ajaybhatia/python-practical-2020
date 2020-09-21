'''
Practical 22

Perform following operations on a list of numbers:
  1) Insert an element 2) delete an element 3) sort the list 4) delete entire list
'''

numbers = [50, 34, 9, 90, 32, 67, 12, 89, 63, 74]
print(numbers)

# Insert an element to the end of the list
numbers.append(45)
print(numbers)

# Insert an element at specific index
numbers.insert(4, 100)
print(numbers)

# Delete an element
numbers.remove(90)
print(numbers)

# Sort the list
numbers.sort()
print(numbers)

# Clear entire list
numbers.clear()
print(numbers)

# Delete entire list
del numbers
