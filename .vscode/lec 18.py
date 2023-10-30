# # lab 17
import numpy as np
import pandas as pd

# # Basic data structures in pandas
# # Series:- One dimentional labeled array, Dataframe two dimentional , for Multidimentional labeled array

# # Task 1: Object creation using Series
# s = pd.Series([1,2,3,np.nan,7])
# print(s) 

# # Task 2: Object creation using DataFrame
dates = pd.date_range("20230926",periods=4)
# print(dates)
df = pd.DataFrame(np.array([[1,2],[3,4],[5,6],[7,8]]), index=dates, columns = list("AB"))
# print(df)


# # Task 3: DataFrame passing a dictionary of objects
# dic1 = {"A":100,"B":200,"C":500,"D":pd.Series(30,index=list(range(3)))}
# dic2 = {"A":100,"B":200,"C":500,"D":[1,2,3,4]}
# df1= pd.DataFrame(dic1,dtype="float32")
# df2= pd.DataFrame(dic2,dtype="float32")
# print(df1)
# print(df2)

# # Task 4: Viewing Data
# print(df.head(2))
# print(df.tail(2))
# print(df.index)
# print(df.columns)


# #################### Post Lab ############################

# # Task 1: NumPy representation of the underlying data with DataFrame.to_numpy()
# d1 = pd.DataFrame({"A": [1, 2], "B": [3.0, 4.5]},dtype="float32")
# arr1 = d1.to_numpy()
# print(arr1)

# # Task 2: describe() shows a quick statistic summary of your data
# s = pd.Series([10, 20, 30, 40])
# k1 = s.describe()
# print(k1)
# print(k1.dtype)
# print("\n")
# s = pd.Series([ np.datetime64("2000-01-01"), np.datetime64("2010-01-01"), np.datetime64("2010-01-01")])
# d1 = s.describe()
# print(d1)


# # Task 3: Transposing your data
# df = pd.DataFrame({"A": [1, 2], "B": [3.0, 4.5]},dtype="float32")
# d1 = df.transpose()
# arr2 = d1.to_numpy()
# print(arr2)


# # Task 4: 

# df = pd.DataFrame([1, 2, 3, 4, 5], index=[100, 29, 234, 1, 150],columns=['A'])
# a3 = df.sort_index()
# print(a3)
# a2 = df.sort_index(ascending=False)
# print(a2)
# df = pd.DataFrame({"a": [1, 2, 3, 4]}, index=['A', 'b', 'C', 'd'])
# a1=df.sort_index(key=lambda x: x.str.lower())
# print(a1)


# Task 5: Selection (getitem[],slice:,label, position) 
df = pd.DataFrame([1, 2, 3, 4, 5],columns=['A'])
print(df)
s = pd.Series([10, 20, 30, 40, 50, 60, 70, 80, 90])
print(s[1:5])
print(s[8])