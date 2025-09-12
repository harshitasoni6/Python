# Question 3: Class for Matrix
"""
Implement a Python class named `Matrix` to represent matrices.

Theory:
A matrix is a two-dimensional array of numbers. The class should handle operations
such as addition, subtraction, multiplication, transposition, and determinant calculation.

Operations:
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Transposition: Transpose the matrix
5. Determinant: Calculate the determinant of the matrix

Test Cases:
Test Case 1:
matrix1 = Matrix([[1, 2], [3, 4]])
matrix2 = Matrix([[5, 6], [7, 8]])
assert str(matrix1) == "[[1, 2], [3, 4]]"
assert str(matrix2) == "[[5, 6], [7, 8]]"
assert str(matrix1 + matrix2) == "[[6, 8], [10, 12]]"
assert str(matrix1 - matrix2) == "[[-4, -4], [-4, -4]]"
assert str(matrix1 * matrix2) == "[[19, 22], [43, 50]]"
assert str(matrix1.transpose()) == "[[1, 3], [2, 4]]"
assert matrix1.determinant() == -2

Test Case 2:
matrix3 = Matrix([[1, 2, 3], [4, 5, 6]])
matrix4 = Matrix([[7, 8], [9, 10], [11, 12]])
assert str(matrix3) == "[[1, 2, 3], [4, 5, 6]]"
assert str(matrix4) == "[[7, 8], [9, 10], [11, 12]]"
assert str(matrix3 + matrix4) == "Addition not possible"
assert str(matrix3 - matrix4) == "Subtraction not possible"
assert str(matrix3 * matrix4) == "[[58, 64], [139, 154]]"
assert str(matrix4.transpose()) == "[[7, 9, 11], [8, 10, 12]]"
assert matrix4.determinant() == "Determinant not possible"
"""

class Matrix:
    pass