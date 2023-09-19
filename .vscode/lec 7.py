#lab - 6
# # Task 1 : for Loop example 
# a = "KiRTAN" 
# for i in a:
#     print(i)
# # Task 2 : 
# a = "KiRTAN" 
# for i in a:
#     print(i,end="")
# # Task 3 : use of loop in list
# l1 = ["A","B","C"]
# for iter in l1:
#     print(iter)

# # Task 4 : Find the average sum of Numbers
# list1 = [35, 43, 35, 55, 33, 45]
# print(list1)
# sum = 0
# for i in list1:
#     sum += i
# print("Average of the List is :- ",sum/len(list1))  

# # Task 5 : For loop using Tuple
# tup1 = (45, 32, 34, 86, 55, 94 )
# sum = 0 
# for i in tup1:
#     sum += i
# print("Sum of the Tuple is :- ",sum)

# # Task 6 : For loop using the Range
# for i in range(2,12):   
#     print(i)

# # Task 7: write a python code to calculate factorial of given number
# a = int(input("Enter the Number: "))
# fact = 1
# for i in range(1,(a+1)):
#     fact = fact*i
# print("Factorial of the number is ", fact)

# # Task 8: Create a Table using Loop
# a = int(input("Enter th Number"))
# for i in range(1,11):
#     print(a," * ",i," = ",(a*i))

# # Task 9: For loop using Range and len function
# li1 = ["C++","Python","Java","R","PHP"]
# for i in range(len(li1)):
#     print("PL",li1[i])
# #loop which skips the element
# for i in range(0,len(li1),2):
#     print("PL",li1[i])

# # Task 10: Nested for Loop
# com = ["Google", "Apple", "PWC", "Uber"]
# for i in com:
#     print("Display each letter of "+i)
#     for letter in i:
#         print(letter)

# # Task 11: For loop with else close
# for i in range(0,10,1):
#     print(i)
# else:
#         print("The loop has Completed")

# # Task 12: for loop using break statement 
# for i in range(1,10):
#     if(i==7):
#         break
#     print(i)

# Task 13: for loop using continue statement (skip) 
for i in range(1,10):
    if(i==3):
        continue
    print(i)