################################ Lab 9 ##############################
import numpy as np
# # Numpy Array Function
# # ndim() attribute ca nbe used to find the dimension 

# a = np.array(8)
# b = np.array([1,2,3])
# c = np.array([[1,2,3],[4,5,6]])
# d = np.array([[[1,2,3],[4,5,6]],[[11,22,33],[44,55,66]]])

# print(a.ndim)
# print(b.ndim)
# print(c.ndim)
# print(d.ndim)

# # The itemsize() is used to understand the byte size

# a = np.array([[1,1+2j],[3,4]])
# print(a.itemsize)

# # the dtype attritube to understand the DATA
# a = np.array([[1,2],[3,4]]) 
# print(a.dtype)

# a = np.array([[1,2.0],[3,4]])
# print(a.dtype)

# # slicing is used to extract a range of elements from matrix
# a = np.array([[1,2,3],[4,5,6]])
# print(a[0,1])

# # the random module's rand() method returns a random element
# a = np.random.rand(3,2)
# print(a)


# # the mean() function is used to comlpete the arithmatic operation of mean value
# a = np.array([[1,2],[3,4]])
# b = np.mean(a,axis=0)
# c = np.mean(a,axis=1)
# print(b)
# print(c)

# # The Append function is used to add new value 
# a = np.array([[1,2],[3,4]])
# b = np.array([[7,6],[8,9]])
# c = np.append(a,b)
# print(c)

# # The insert() funtion inserts the values in the given index

# a = np.array([[1,2],[3,4],[5,6]])
# print(np.insert(a,2,[5,9],axis=0))
# print('\n')
# print(np.insert(a,2,[5],axis=1))
# print("\n")


# # number mathematical operations
# x = np.array([[1,2],[3,4]], dtype= np.float64)
# y = np.array([[5,6],[7,8]], dtype= np.float64)


# # Elementwise Sum
# print(x+y)
# print(np.add(x,y))
# print("\n")

# # Elementwise Subtraction
# print(x-y)
# print(np.subtract(x,y))
# print("\n")

# # Elementwise Multiplication
# print(x*y)
# print(np.multiply(x,y))
# print("\n")

# # Elementwise Division
# print(x/y)
# print(np.divide(x,y))
# print("\n")



# # Broadcasting
# # In Numpy, we can perform mathematical operations on array
# # create 1-D array

# a1 = np.array([1,2,3])
# a2 = np.array([[1],[2],[3]]) 
# # Add arrays of different dimentions
# sum = a1 + a2
# print(sum,"\n")

# # Broadcasting with scalars
# a1 = np.array([1,2,3])
# num = 5
# sum  = a1 + num
# print(sum,"\n")

# # Numpy matrix operation in Numpy (real Matrix Multiplication)
# mt1 = np.array([[1,2],[3,4]])
# mt2 = np.array([[5,6],[7,8]])

# result = np.dot(mt1,mt2)
# print(result,"\n")


# # Transpose
# mt1 = np.array([[1,2],[3,4]])
# result = np.transpose(mt1)
# print(result,"\n")

# # Inverse
# mat1 = np.array([[1,2,3],[2,3,1],[4,3,1]])
# result = np.invert(mat1)
# print(result)
# mat2 = np.array([[1,0,0],[0,1,1],[0,1,1]])
# print(np.linalg.inv(mat2))

