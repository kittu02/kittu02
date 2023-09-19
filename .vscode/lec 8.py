#Lab - 7

# i = 1
# while i<5:
#     print(i)
#     i = i+1

# # break and continue in While Loop
# i = 0
# while i<9:
#     i += 1
#     if i==3:
#         continue
#     elif i == 7:
#         break
#     print(i)
# print("\n")

# # pass in While loop
# i = 0
# while i<9:
#     i += 1
#     if i==3:
#         pass
#     print(i)

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==> Functions <-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# def first_print():
#     print(" Welcome  to PWP lab ...")

# first_print()


# # parameter define
# def my_name(name):
#     print("My name is " + name)

# my_name("Kirtan")


# # value inside function
# def fin_val():
#     a = 5
#     print(a)        #inside the function scope
#     print("\n")
# a=10
# fin_val()
# print(a)        #outside the funtion scope


# a = int(input(" Enter a Number: "))
# def square_print():
#     b = a**2
#     return b
# c = square_print()
# print(c)


# # Nested Function
# def out_function():
#     print(" Outer Function ")
#     def in_function():
#         print(" Inner function ")
#     in_function()

# out_function()    


# # Example of lambda vs Reguler function 

# t = lambda x:x*3
# print(t(5))

# x = 3
# def tripler(x):
#     return x*3
# print(tripler(x))

