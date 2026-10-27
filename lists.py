#======= 02-10-2026 ========

# Task 1: Reverse List

my_list=[10,20,30,40,50,11]
my_list.reverse()
print(my_list)

# Task 2:  Common Elements

list1=[1,2,3,4,5]
list2=[4,5,6,7,8]
common=set(list1)&set(list2)
print(common)

#Task-3: Unique Elements

original_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(set(original_list))
print(unique_list)

#Task-4 : Remove Duplicates

duplicated_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(set(duplicated_list))
print(unique_list)

# Exercise-1
#List Concatenation

list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = list1 + list2
print(result)

# Exercise-2
# List Repetition

my_list = [1, 2, 3]
result = my_list * 3
print(result)


#Exercise-3
#List Remove

my_list = [10, 20, 30, 40, 50, 60]
result = my_list[1::2]
print(result)

#Exercise-4
#List Insertion

my_list = [20, 30, 40, 50]
my_list.insert(0, 10)
my_list.insert(1, 11)
my_list.insert(2, 12)
print(my_list)


#=======  LIST COMPREHENSIONS   =======

#1. Square Numbers 

squares =[i*i for i in range(1, 11)]
print(squares)

# 2. Even Numbers:

even_numbers=[i for i in range(1, 21) if i % 2 == 0]
print(even_numbers)

# 3. Words Length

words = ["apple", "banana", "cherry", "date"]
length=[len(word)for word in words]
print(length)