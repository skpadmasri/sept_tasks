# =====15-10-2026 ======

#Error Handling or Exception Handling

#syntax errors
#print(10+10

#runtime errors

# num_1=int(input("Enter the num_1:"))
# num_2=int(input("Enter the num_2:"))
# print(num_1+num_2)
# print(num_1-num_2)
# print(num_1*num_2)
# print(num_1/num_2)
# print(num_1+num_2)
# print(num_1-num_2)

#logical errors

# num_1=10
# num_2=5
# print(num_1+num_2)

#Else

# num_1=int(input("Enter the num_1:"))
# num_2=int(input("Enter the num_2:"))
# print(num_1+num_2)
# print(num_1-num_2)
# try:
#     print(num_1/num_2)
# except:
#     print(f"error occured")
# else:
#     print(num_1*num_2)
#     print(num_1+num_2)
#     print(num_1-num_2)
# finally:
#     print("regardless statement")

#value error

# num_1=int(input("Enter the num1:"))
# num_2=int(input("Enter the num2:"))
# except ValueError as e:
# print(e)
# else:
# print(num_1+num_2)

#Index error

# list_1=[1,2,3,4]
# print(list_1[1])
# try:
#       print(list_1[6])
# except IndexError as e:
#       print(e)
# else:
#       print(list_1[3])

#Key error

# sample={
#     1:"padhu",
#     2:"ammu",
# }
# print(sample.get(5))
# try:
#     print(sample[5])
# except KeyError as e:
#     print(e)

# FileNotFoundError

# try:
#     file = open("abc.txt", mode="r")
#     print(file.read())
#     file.close()
# except FileNotFoundError as e:
#     print(e)

# ZeroDivisionError

# try:
#     a = 10
#     b = 0
#     print(a / b)
# except ZeroDivisionError as e:
#     print(e)

# AttributeError

# sample = "padhu"

# try:
#     sample.append("ammu")
# except AttributeError as e:
#     print(e)

# OverflowError

# import math

# try:
#     print(math.exp(1000))
# except OverflowError as e:
#     print(e)

# OSError

# try:
#     with open("abc.txt", mode="r") as file:
#         print(file.read())
# except OSError as e:
#     print(e)

