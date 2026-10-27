#  ======>   09-10-2026    ======

#Task-1

# Write a Python function square_all(numbers) that takes a list of numbers as input and returns a new list containing the square of each number in the input list.
# Use the map() function with a lambda function to implement this.
 
list1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
result=map(lambda a:a**2,list1)
print(list(result))

#Task-2

#Write a Python function filter_positive(numbers) that takes a list of numbers as input and returns a new list containing only the positive numbers from the
# input list. Use the filter()function with a lambda function to implement this

list1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
result=filter(lambda a:a%2==0,list1)
print(list(result))

#Task-3
#Write a Python function calculate_factorial(n)that calculates the factorial of a given number n. 
# Use the reduce() function with an appropriate lambda function to implement this.

from functools import reduce
def calculate_factorial(n):
    result = reduce(lambda a, b: a * b, range(1, n + 1))
    return result
n = int(input("Enter a number: "))
print("Factorial:", calculate_factorial(n))


#Task-4

#Write a Python function count_vowels(string) that takes a string as input and returns the count of vowels (a, e, i, o, u) in the input string.
#  Use the reduce()function with an appropriate lambda function to implement this.

from functools import reduce
def count_vowels(string):
    return reduce(lambda a, b: a + 1 if b in "aeiouAEIOU" else a, string, 0)
string = input("Enter a string: ")
print(count_vowels(string))



