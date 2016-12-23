"""
about:
This code was written by Mostafa El-Marzouki @iSuperMostafa
------------------------------------------------------------
summery:
this project contains these methods to manipulate a matrix:
- TransposeMatrix
- FlipHorizontally
- FlipVertically
- Rotate90Clockwise
- Rotate90CounterClockwise
- Rotate180Clockwise
- Rotate180CounterClockwise
input: Matrix
output: manipulated matrix
"""
import MatrixTransformations

Manage = MatrixTransformations.MatrixTranformations()

Matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Matrix:")
for row in Matrix:
    print(row)
print("----------")
print("Transpose Matrix:")
Matrix = Manage.TransposeMatrix(Matrix)
for row in Matrix:
    print(row)
print("----------")
print("Flip Matrix Horizontally: ")
Matrix = Manage.FlipHorizontally(Matrix)
for row in Matrix:
    print(row)
print("----------")
print("Flip Matrix Vertically: ")
Matrix = Manage.FlipVertically(Matrix)
for row in Matrix:
    print(row)
print("----------")
print("Rotate Matrix 90 Clockwise: ")
Matrix = Manage.Rotate90Clockwise(Matrix)
for row in Matrix:
    print(row)
print("----------")
print("Rotate Matrix 90 Counter-Clockwise: ")
Matrix = Manage.Rotate90CounterClockwise(Matrix)
for row in Matrix:
    print(row)
print("----------")
print("Rotate Matrix 180 Clockwise: ")
Matrix = Manage.Rotate180Clockwise(Matrix)
for row in Matrix:
    print(row)
print("----------")
print("Rotate Matrix 180 Counter-Clockwise: ")
Matrix = Manage.Rotate180CounterClockwise(Matrix)
for row in Matrix:
    print(row)
