'''
Practical 28

Check whether a number is in a given range using functions.
'''


def check_in_range(start, end, num):
    return num >= start and num <= end


start, end, num = 1, 100, 81

print(f"Is {num} in range {start}-{end}? {check_in_range(start, end, num)}")
