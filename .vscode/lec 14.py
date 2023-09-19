#lab - 13
import matplotlib
import numpy as np
print(matplotlib.__version__)
from matplotlib import pyplot
import matplotlib.pyplot as plt

# # matplotlib is a python 2D plotting library which produces 
# # task 1 plot line
# plt.plot([1,2,3],[1,2,3])
# plt.show()

# x = np.arange(10) # including zero it will give range of 0-9
# print(x)
# y = 2*x+4
# plt.plot(x,y)
# plt.show()

# # task 2 draw two line
# x = [1,2,3]
# y = [2,10,5]
# plt.plot(x,y)
# plt.title("Line")
# plt.ylabel('Y axis')
# plt.xlabel('X axis')
# plt.show()

# # task 3 window size 
# plt.plot([1,2,3],[4,2,3])
# plt.figure(figsize=(50,50))
# plt.show()

# # Task 4 sbuplots
# plt.subplot(1,2,1)
# plt.plot([1,2,3],[3,2,1])
# plt.title('First Part')
# plt.subplot(1,2,2)
# plt.plot([2,4,6],[1,2,3],"r")
# plt.title('second part')
# plt.show()


# Task 5 Important types of plots
# 1. Baar graphs
# 2. Histograms
# 3. Scatter plots
# 4. Sine plots


# # 1. Bar graphs
# plot = plt.figure()
# chars = ['A','B','C']
# values = [7,9,3]
# plt.bar(chars,values)
# plt.show()

# # 2. Histogram

# x = [20,40,60,90,50,20,70,20,20,10,90]
# num = 4
# plt.hist(x,num)
# plt.show()


# # 3. Scatter plot
# a1 = [44,56,73,89,45,31]
# a2 = [10,20,30,50,40,30]

# fig = plt.figure()
# plt.scatter(a2,a1,color='b')
# plt.show()

# # 4. Sine plots 
# v = np.arange(0,2*np.pi,0.2)
# g = np.sin(v)
# plt.title("Sine wave")
# plt.plot(v,g)
# plt.show()

# # Subplot function

v = np.arange(0,2*np.pi,0.2)
g_sin = np.sin(v)
g_cos = np.cos(v)

plt.subplot(2,1,1)
plt.title("Sin wave")
plt.plot(v,g_sin,color='g')
plt.subplot(2,1,2)
plt.title("Cos wave")
plt.plot(v,g_cos,color='r',linestyle=':')
plt.show()

# # bar plot
# x = [5,8,10]
# y = [12,16,6]

# x2 = [6,9,11]

