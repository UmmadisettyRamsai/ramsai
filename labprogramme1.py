#A program to write the dot product of a vector 
#A program to perform the matrix operation
# Python Program illustrating
# numpy.dot() method
 
import numpy as np
 
# Scalars
product = np.dot(5, 4)
print("Dot Product of scalar values  : ", product)
 
# 1D array
vector_a = 2 + 3j
vector_b = 4 + 5j
 
product = np.dot(vector_a, vector_b)
print("Dot Product  : ", product)
 
A = np.array([[6, 1, 1],
              [4, -2, 5],
              [2, 8, 7]])
 
# Rank of a matrix
print("Rank of A:", np.linalg.matrix_rank(A))
 
# Trace of matrix A
print("\nTrace of A:", np.trace(A))
 
# Determinant of a matrix
print("\nDeterminant of A:", np.linalg.det(A))
 
# Inverse of matrix A
print("\nInverse of A:\n", np.linalg.inv(A))
 
print("\nMatrix A raised to power 3:\n",
           np.linalg.matrix_power(A, 3))
