# # Task 1: 
# a = int(input(" Enter the Number: "))
# for i in range(1,(a+1)):
#     for j in range(1,(a+1)):
#         print("#",end="")
#     print()

# # Task 2: 
# odt = 0
# evt = 0
# for i in range(1,101):
#     if(i%2==0):
#         evt = evt + i
#     else:
#         odt = odt + i
# print("even total = ",evt)
# print("odd total = ",odt)

# # Task 3:

# for i in range(10,301,10):
#     print(i,", ",end="") 

# # Task 4:
# i = 105
# while(i>6):
#     print(i,", ",end="")
#     i = i-7

# # Task 5:
# i = num = int(input(" Enter a Number to check : "))
# k=True
# while(i>1):
#     if(num%i==0):
#         k=False
#     i = i-1
# if(k==False):
#     print(" Number is not prime number") 
# else:  
#     print(" Numberb is prime Number ")

# # Task 6:

# num = input(" Enter a Number")
# print(num[::-1])

# Task 7:

bin_num = input("Enter a Number in Binary")
n = len(bin_num)
total = 0
ind = 0

while(n>0):

    total = total + ((2**n)*bin_num[ind])
    n = n-1
    i = i+1

print(total)
