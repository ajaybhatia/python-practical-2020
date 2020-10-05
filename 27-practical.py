'''
Practical 27

Perform following operations on dictionary
  1) Insert 2) delete 3) change
'''

book = {
    1: "Compute sum, subtraction, multiplication, division and exponent of given variables input by the user.",
    2: "Compute area of following shapes: circle, rectangle, triangle, square, trapezoid and parallelogram.",
    3: "Compute volume of following 3D shapes: cube, cylinder, cone and sphere.",
    4: "Compute and print roots of quadratic equation ax 2 +bx+c=0, where the values of a, b, and c are input by the user.",
    5: "Print numbers up to N which are not divisible by 3, 6, 9,, e.g., 1, 2, 4, 5, 7,....",
    6: "Write a program to determine whether a triangle is isosceles or not?",
    7: "Print multiplication table of a number input by the user.",
    8: "Compute sum of natural numbers from one to n number.",
    9: "Print Fibonacci series up to n numbers e.g. 0 1 1 2 3 5 8 13.....n",
    10: "Compute factorial of a given number."
}

# Insert
print("Insertion...")
book[11] = "Count occurrence of a digit 5 in a given integer number input by the user."
print(book, end="\n\n")

# Delete
print("Deletion...")
book.pop(4)
print(book, end="\n\n")

# Update
print("Updation...")
book[8] = "Compute product of natural numbers from one to n number."
print(book)
