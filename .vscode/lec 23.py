#lab 22


# Wriet Mode
# Task 1: Open a file for writing and insert some 
f = open('ICT.txt','w')
f.write('PWP\n')
f.write('COA \n')
f.write('ICE\n')
f.write('DMGT\n')
f.write('SS\n')
f.close()


# Task 2: Append COde 
f = open('ICT.txt','a')
f.write('DS\n')
f.close()

# # Task 3: Open the file created for reading and read line(s) using readline()
# f=open('ICT.txt','r')
# print(f.readline())
# print(f.readline())
# print(f.readline())
# f.close()


# # Task 4: Exeption Handling in Files
# try:
#     f=open('ICT.txt','r')
#     g = f.readline() # REad next line into a string
#     print(g) # read all (next) lines into a list of strings
# finally:
#     f.close()

# # Task 5: PRocessing (with statement is equivalent to try-finally start )
# with open('ICT.txt','r') as f:
#     for line in f:
#         line = line.strip() # strip the leading/trailing whitespaces and 
#     # file closed automatically upor exit of with- statement

# # Task 6: Deleting Files
# import os as d
# d.remove("ICT.txt")  


