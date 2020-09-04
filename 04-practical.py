'''
Practical 4

Compute and print roots of quadratic equation ax**2 +bx+c=0, where the values of a, b,
and c are input by the user.
'''

a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
c = int(input("Enter value of c: "))

discriminant = b**2 - 4*a*c

if discriminant < 0:
    print("No real roots of x")
elif discriminant == 0:
    x = -b / (2*a)
    print(f"Root of eqaution is {x}")
else:
    x1 = (-b + discriminant) / (2*a)
    x2 = (-b - discriminant) / (2*a)
    print(f"Root 1 of equation is {x1}")
    print(f"Root 2 of equation is {x2}")
