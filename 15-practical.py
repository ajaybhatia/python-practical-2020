'''
Practical 15

Determine prime numbers within a specific range.
'''


def is_prime(number):
    if number == 1:
        return False
    if number == 2 or number == 3:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, int(number**0.5)+1, 2):
        if number % i == 0:
            return False
    return True


rng = input("Enter range: ").split("-")

for i in range(int(rng[0]), int(rng[1])+1):
    if is_prime(i):
        print(i)
