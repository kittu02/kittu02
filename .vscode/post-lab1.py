# # Task 1: Write a program in python to display the factorial of a Number 
# a = int(input("Enter the Number: "))
# fact = 1
# for i in range(1,(a+1)):
#     fact = fact*i
# print("Factorial of the number is ",fact)

# # Task 2: Write a program that appends the square of each number to a new List
# num = [4,7,2,8,5,15,3]
# sqr = []
# for i in num:
#     sqr.append(i*i)
# print("Sqaure list of first list is ")
# print(sqr)

# # Task 3: WAP to seperate positive and negative number from a list.
# num = [44,-74,64,-45,6,-52,39,85,-5,27,-54]
# pos=[]
# neg=[]
# zer=[]
# for i in num:
#     if(i>0):
#         pos.append(i)
#     elif(i<0):
#         neg.append(i)
#     else:
#         zer.append(i)
# print(pos)
# print(neg)
# print(zer)

# # Task 4: WAP to filter Even and odd number from a List.
# num = [44,74,64,45,6,52,39,85,5,27,54]
# even = []
# odd = []
# for i in num:
#     if(i%2==0):
#         even.append(i)
#     else:
#         odd.append(i)
# print(even)
# print(odd)

# # Task 5: WAP to print all even number within the given Range
# a = int(input("Enter the Starting Range: "))
# b = int(input("Enter the ending Range: "))
# ev = []
# for i in range(a,(b+1)):
#     if(i%2==0):
#         ev.append(i)
# print("Even Numbers in given Range are , ", ev)

# # Task 6: WAP to calculate sum of 1 to given number 
# a = int(input("Enter the Last Number to Count: "))
# sum = 0
# for i in range(1,(a+1)):
#     sum += i
# print("sum of given range is ", sum)

# # Task 7: WAP to calculate sum of all Numbers in given range
# a1 = int(input("Enter Initial value of Range: "))
# a2 = int(input("Enter the last value: "))
# sum = 0
# for i in range(a1,(a2+1)):
#     sum += i
# print("Sum of given range is ", sum)

# Task 8: WAP to calculate the sum of all the odd number within given range
# a1 = int(input("Enter Initial value of Range: "))
# a2 = int(input("Enter the last value: "))
# sum = 0
# for i in range(a1,(a2+1)):
#     if(i%2!=0):
#         sum += i
# print("Sum of given range is ", sum)

# # Task 9: WAP to count the total number of digits in a number
# val = int(input("Enter a Number: "))
# a = str(val)
# print("There are ",len(a)," Digits in the Number")

# # Task 10: WAP to check the string is palindrome of not
# str1 = input("Enter the string: ")
# if(str1 == str1[::-1]):
#     print("String is palindrome")
# else:
#     print("String is not palindrome")

# # Task 11: WAP to print factorial number
# a = int(input("Enter a number: "))
# fact = 1
# while(a>0):
#     fact = fact * a
#     a = a-1
# print("Factorial of the number is ",fact)

# Task 12: WAP to count charecters and digits in the given string
s = input("Enter a string : ")
alpha = dig = 0
for i in s:
    if (s.isalpha):
        alpha = alpha + 1
    elif(s.isnumeric):
        dig = dig + 1
print("There are ", alpha," Charecters and ", dig," Digit.")

 


