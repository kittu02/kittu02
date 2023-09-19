# #Lab 8

import numpy as np

# #1D and 2D array 
# n1 = np.array([10,20,30,40])
# print(n1)
# n2 = np.array([[10,20,30],[90,80,70]])
# print(n2)

# # Initializing Numpy array with Zero
# n3 = np.zeros((1,2))
# print(n3)

# n4 = np.zeros((5,5))
# print(n4)

# # Initializing Numpy with same number
# n5 = np.full((2,2),10)
# print(n5)

# # Initializing numpyarray within a range
# n6 = np.arange(10,20)
# print(n6)


# n7 = np.arange(10,50,5)
# print(n7)

# # Initializing numpy array with random numbers
# n8 = np.random.randint(1,100,5)
# print(n8)

# #checking the shape of Numpy arrays
# n9 = np.array([[1,2,3],[4,5,6]])
# print(n9)
# print(n9.shape)
# n9.shape = (3,2)
# print(n9)

# # Joining numpy arrays
# #vstack(), hstack(), column_stack()

# n10 = np.array([10,20,30])
# n11 = np.array([40,50,60])

# print(np.vstack((n10,n11)))
# print(np.hstack((n10,n11)))
# print(np.column_stack((n10,n11)))

# # Numpy Intersection & difference

# n12 = np.array([10,20,30,40,50])
# n13 = np.array([50,60,70,80])

# print(np.intersect1d(n12,n13))
# print(np.setdiff1d(n12,n13))

# Addition of Numpy Arrays

n14 = np.array([10,20])
n15 = np.array([30,40])

print(np.sum([n14,n15]))
print(np.sum([n14,n15],axis=0))
print(np.sum([n14,n15],axis=1))

# Numpy Array basic mathematic

n16 = np.array([10,20,30])

print(n16+1)
print(n16-1)
print(n16*2)
print(n16/2)
print(n16**3)


