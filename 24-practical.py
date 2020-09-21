'''
Practical 24

Perform sequential search on a list of given numbers.
'''

numbers = [50, 34, 9, 90, 32, 67, 12, 89, 63, 74]
search_number = 67

# Sequential search without using any method
index, found = 0, False
for number in numbers:
    if number == search_number:
        found = True
        break
    index += 1

if found:
    print(f"{search_number} is present at index {index}")
else:
    print(f"{search_number} is not present in the list")
