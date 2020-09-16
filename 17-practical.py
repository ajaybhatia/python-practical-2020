'''
Practical 17

Compute transpose of a matrix (array of arrays).

Example Matrix (3 X 3)

1, 2, 3
4, 5, 6
7, 8, 9

'''


def print_matrix(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            print(matrix[row][col], end=" ")
        print()


def matrix_transpose(matrix):
    new_matrix = []
    for row in range(len(matrix[0])):
        row_ = []
        for col in range(len(matrix)):
            row_.append(matrix[col][row])
        new_matrix.append(row_)
    return new_matrix


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
print("Original matrix is: ")
print_matrix(matrix)

new_matric = matrix_transpose(matrix)
print("Transpose of a matrix is: ")
print_matrix(new_matric)
