#lab - 12

import numpy as np
# #to check whether specified values are present in numpy array?
# a=int(input("enter length of array"))
# arr=np.zeros(a)
# b=int(input("enter value you want to check"))
# c=0
# for i in range(0,a,1):
#     arr[i]=int(input("enter value"))
# for i in range(0,a,1):
#     if(arr[i]==b):
#         c=c+1
# if(c>0):
#     print("present")
# else:
#     print("absent")    



# # find the most frequent array in a numpy array
# import numpy as np

# def most_frequent_element(arr):
#     unique_elements, counts = np.unique(arr, return_counts=True)
#     max_count = np.max(counts)
#     most_frequent_elements = unique_elements[counts == max_count]
#     return most_frequent_elements

# arr = np.array([1, 2, 2, 3, 4, 4, 4, 5, 5, 5, 5])
# result = most_frequent_element(arr)
# print("Most frequent element(s):", result)



# reverse a numpy array
# a=int(input("enter length of array"))
# arr=np.zeros(a)
# for i in range(0,a,1):
#     arr[i]=int(input("enter value"))
# arr2=np.zeros(a)
# for j in range(0,a,1):
#     arr2[j]=arr[a-j-1]
# for j in range(0,a,1):
#     print(arr2[j])

# # matrix
# a=np.zeros((3,3))
# for i in range(0,3,1):
#     for j in range(0,3,1):
#         a[i][j]=int(input("enter value"))
# print(a)  
# b=2
# for i in range(0,3,1):
#     for j in range(0,3,1):
#         if(i==j):
#             continue
#         else:
#             a[i][j]=b
#         b=b+1
# print(a) 


f1=np.loadtxt("al.txt",dtype=int)
print(f1)

# f1=np.loadtxt("sk.txt",skiprows=0,dtype=str)
# print(f1)
# f1=np.loadtxt("dj.txt",usecols=1,skiprows=1,dtype=str)
# for i in f1:
#     print(f1)
# f1=np.genfromtxt("fh.txt",dtypr=str,encoding=None,delimiter=",")
# print(f1)

