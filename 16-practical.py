'''
Practical 16

Count number of persons of age above 60 and below 90.
'''

persons = [12, 5, 56, 87, 61, 90, 43, 81, 73, 79, 65, 69, 21, 25, 19]

# Method 1
count = 0
for age in persons:
    if age > 60 and age < 90:
        count += 1

print(f"Number of persons having age above 60 and below 90 are {count}")

# Method 2
count = len(list(filter(lambda age: age > 60 and age < 90, persons)))
print(f"Number of persons having age above 60 and below 90 are {count}")
