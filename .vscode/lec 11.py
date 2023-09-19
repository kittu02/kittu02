############################ Lab 10 #########################
import numpy as np


# Task 1: Matrix Inverse
mat1 = np.array([[1,2,3],[2,3,1],[4,3,1]])
result = np.linalg.inv(mat1)
result = np.invert(mat1)
print(result)
# when determinant is zero it will give excepltion in below code
mat2 = np.array([[1,0,0],[0,1,1],[0,1,1]])
print(np.linalg.inv(mat2))


# Task 2: Find determinant of matrix
result = np.linalg.det(mat1)
print(result)


# Task 3: Flatten matrix in NumPy
ma1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
ma2 = np.array([[1],[2],[3]])
result = ma1.flatten()
print(result)

# Task 4: Numpy array Iterating
arr = np.array([1,2,3])
for x in arr:
    print(x)
print("\n")

# Task 5: Iterating 2-D arrays
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
for x in arr:
    print(x)
print("\n")

arr = np.array([[1,2,3],[4,5,6]])
for x in arr:
    for y in x:
        print(y)
print("\n")

# Task 6: Submatrix in a matrix with numpy
a1 = np.array([1,2,3])
a2 = np.array([[1,2,3]])
print(a1)
print(a2)