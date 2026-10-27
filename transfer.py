# =======>   02-10-2026   =======

 # 1. Using break in a while Loop

# numbers = [25, 30, 20, 40, 15, 25]
# sum = 0
# i = 0
# while i < len(numbers):
#     sum += numbers[i]
#     if sum > 100:
#         print("Sum exceeded 100")
#         break
#     i += 1

# 2. Write a Python script that uses a for loop to iterate through numbers from 1 to 600. Print only the odd numbers, skipping the even ones using the continue statement

# for i in range(1, 601):
#     if i % 2 == 0:
#         continue
#     print(i)

# 3. Write a Python script that checks if a number is even or odd. If the number is even, print "Even"; if odd, do nothing using the pass statement.

# num = int(input("Enter a number: "))
# if num%2 == 0:
#     print("Even")
# else:
#     pass

# 4. Write a Python script that iterates through a list of words. If the word is "break," exit the loop using the break statement. If the word is "skip," skip the rest of the code for the current iteration using the continue statement. For any other word, print the word.

# words = ["hello", "python", "skip", "world", "break", "welcome"]
# i = 0
# while i < len(words):
#     word = words[i]
#     if word == "break":
#         break
#     elif word == "skip":
#         i += 1
#         continue
#     else:
#         print(word)
#     i += 1