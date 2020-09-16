'''
Practical 18:

Perform following operations on two matrices.
  1) Addition 2) Subtraction 3) Multiplication
'''


def print_matrix(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            print(matrix[row][col], end=" ")
        print()


def matrix_addition(a, b):
    if len(a[0]) == len(b[0]) and len(a) == len(b):
        new_matrix = []
        for r in range(len(a)):
            row_ = []
            for c in range(len(a[0])):
                row_.append(a[r][c]+b[r][c])
            new_matrix.append(row_)
        return new_matrix
    else:
        print("Matrices are not equal")


def matrix_subtraction(a, b):
    if len(a[0]) == len(b[0]) and len(a) == len(b):
        new_matrix = []
        for r in range(len(a)):
            row_ = []
            for c in range(len(a[0])):
                row_.append(a[r][c]-b[r][c])
            new_matrix.append(row_)
        return new_matrix
    else:
        print("Matrices are not equal")


def matrix_multiplication(a, b):
    if len(a[0]) == len(b):
        new_matrix = []
        for r in range(len(a)):
            row_ = []
            for c in range(len(b[0])):
                sum = 0
                for k in range(len(a[0])):
                    sum += a[r][k]*b[k][c]
                row_.append(sum)
            new_matrix.append(row_)
        return new_matrix
    else:
        print("Matrices row and col are not equal")


matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]

print("Addition Resultant: ")
print_matrix(matrix_addition(matrix1, matrix2))

print("Subtraction Resultant: ")
print_matrix(matrix_subtraction(matrix1, matrix2))

print("Multiplication Resultant: ")
print_matrix(matrix_multiplication(matrix1, matrix2))
