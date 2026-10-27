# =======   06-10-2026   =========

#Coding Exercise

#Task-1 Create a Tuple

my_tuple = ("Padmasri", 22, "Black")
print(my_tuple)

#Task-2  Access Tuple Elements

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print(days[2])

#Task-3  Tuple Concatenation

tuple1=(1,3,5)
tuple2=(2,4,6)
obj=tuple1+tuple2
print(obj)

#Task-4  Tuple Unpacking

dimensions = (10, 5)
length, width = dimensions
area = length * width
print(area)

#Task-5   Check if an Element Exists

colors = ("pink", "black", "white")
is_color_present = "black" in colors
print(is_color_present)



#Task-6    
#  Write a Python program to generate a bill for a supermarket purchase. 
# The program should store the items and their prices in a list of tuples.
#  It should then iterate over this list to print out each item along with its price.
#  Finally, calculate and print the total cost of all the items.

items = [("soap", 35.0), ("Shampoo", 120.0), ("Biscuits", 30.0)]
print(f"Item\tPrice")
print("-" * 20)
total = 0.0
for i, j in items:
    print(f"{i}\t{j}")
    total += j
print("-" * 20)
print(f"Total\t{total}")