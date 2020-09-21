'''
Practical 25

Perform search on ordered list of given numbers.
'''

numbers = [9, 12, 32, 34, 45, 50, 63, 67, 74, 89, 100]
search_number = 67

start, end, found = 0, len(numbers)-1, False

while start <= end:
    mid = (start+end)//2
    if numbers[mid] < search_number:
        start = mid+1
    elif numbers[mid] > search_number:
        end = mid-1
    else:
        found = True
        print(f"{search_number} found at index {mid}")
        break

if not found:
    print(f"{search_number} is not in list")
