# ############################### Lab 11 ################################
# Pre Lab
import numpy as np

# # Task 1: make following matrix [[ 2.  3.  4.] ,[ 5.  6.  7.],[ 8.  9. 10.]]
# i = j  = 1
# k = 2
# a = np.zeros((3,3))
# for i in range(0,3,1):
#     for j in range(0,3,1):
#         a[i][j] = k
#         k=k+1
#     print("\n")
# print(a)

# # Task 2: write a numpy program to create a null vector of size 10 and update the sixth value to 11
# a = np.zeros(10)
# a[6]= 11
# print(a)

# # Task 3: write a Numpy program to create an 4x4 matrix and fill i with a checkboard pattern
# k = 0
# a = np.zeros((4,4))
# for i in range(0,4,1):
#     for j in range(0,4,1):
#         a[i][j] = k
#         k = int(not(k))
#     k = int(not(k))
#     print("\n")
# print(a)

# # ############################ Lab


# #  Task  1: iterating arrays using nditer()
# # iterating on each scalar element
# arr = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
# arr1 = np.array([[1,2],[5,6]])

# for i in np.nditer(arr):
#     print(i)
# print("\n")


# arr = np.array([1,2,3,4,5,6])
# newarr = np.array_split(arr,3)
# print(newarr)

# #  Task  2:Searching Arrays
# # Find the indexes where the value is 4
# arr = np.array([1,2,3,4,5,4,4])
# x = np.where(arr == 4)
# print(x)
# print("\n")

# # sort function
# arr = np.array([3,2,0,1])
# print(np.sort(arr))

# arr = np.array(['banana','cherry','apple'])
# print(np.sort(arr))
# print("\n")

# Task  3: Numpy save and load arrays as binary file(npy,npz)
# open a binary file in write mode

arr = np.array([[[11,12,13,14],[15,16,17,18]],[[18,19,20,21],[22,23,24,25]]])
file = open("arr","wb")
# save array to the file
np.save(file,arr)
# close the file
file.close


# open the file in read binary mode
file = open("arr","rb")
# read the file to numpy array
arr1 = np.load(file)
print(arr1)
# close the file
file.close


# ##################  Post lab
# # Task 1: extract all odd numbers from arr
# arr = np.array([0,1,2,3,4,5,6,7,8,9]) 
# ar1 = []
# for i in arr:
#     if(arr[i]%2!=0):
#         ar1.append(arr[i]) 
# print(ar1)

# # Task 2: Replace all odd numbers in arr with -1
# arr = np.array([0,1,2,3,4,5,6,7,8,9])
# for i in arr:
#     if(arr[i]%2!=0):
#         arr[i] = -1
# print(arr)

# # Task 3 : Create the following pattern without hardcoding 
# a = np.array([1,2,3])
# a1 = []
# for i in range(0,len(a)):
#     for j in a:
#         a1.append(a[i])
# for i in a:
#     for j in range(0,len(a)):
#         a1.append(a[j])

# print(a1)

