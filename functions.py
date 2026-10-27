
# ======>   08-10-2026    ======

# Task 1: Add Function
# Write a Python function named add that takes two arguments a and b and returns their sum.

def add(a,b):
    return a+b
obj=add(10,5)
print(obj)

# Task 2: Square Function
# Write a Python function named square that takes a number as input and returns its square

def square(num):
    return num * num
obj = square(5)
print(obj)

# Task 3: Factorial Function
# Write a Python function named factorial that takes a positive integer n as input and returns its factorial.

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact
print(factorial(5))

# Task 4: Maximum Function
# Write a Python function named maximum that takes a list of numbers as input and returns the maximum value in the list.

def maximum(numbers):
    return max(numbers)
numbers = [10, 13, 1, 16, 7]
print(maximum(numbers))

# Task 5: Reverse Function
# Write a Python function named reverse that takes a string s as input and returns its reverse.

def reverse(s):
    return s[::-1]
print(reverse("padhu"))

# Task 6: Check Prime Function
# Write a Python function named is_prime that takes a positive integer n as input and returns True if n is prime, otherwise False

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
print(is_prime(7))

# Task 7: Fibonacci Function
# Write a Python function named fibonacci that takes a positive integer n as input and returns the n-th Fibonacci number.

def fibonacci(n):
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    a, b = 0, 1
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b
print(fibonacci(6))

# Task 8: Palindrome Function
# Write a Python function named is_palindrome that takes a string s as input and returns True if s is a palindrome, otherwise False

def is_palindrome(s):
       s = str(s).lower()
       return s == s[::-1]
print(is_palindrome("madam"))

# Task 9: Sum of Squares Function
# Write a Python function named sum_of_squares that takes a list of numbers as input and returns the sum of the squares of those numbers.

def sum_of_squares(numbers):
    return sum(x**2 for x in numbers)
print(sum_of_squares([1, 2, 3, 4]))

# Task 10: Average Function
# Write a Python function named average that takes a list of numbers as input and returns the average value.

def average(numbers):
        if not numbers:
            return 0
        return sum(numbers) / len(numbers)
print(average([10, 20, 30, 40]))