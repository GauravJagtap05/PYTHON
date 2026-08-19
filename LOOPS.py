# Teneray operator:

# even odd
# number = int(input(" enter number : "))
# print( " even" if number %2 ==0 else "odd")

# voting
# age = int(input(" enter your age : "))
# print("elegible" if age>=18 else "not elegible")
#
# Positive or negative
# number = int(input(" enter the number : "))
# print("positive" if number > 0 and number !=0 else "negative")
#
# greater number
# number1 = int(input(" enter the number : "))
# number2 = int(input(" enter the number : "))
# print('number1' if number1>number2 else 'number2')
#
# PASS or FAIL
# marks = int(input(" enter the marks : "))
# print( 'pass' if marks >= 35 else 'fail')

# Assign "Adult" or "Minor" to a variable.
# age = int(input(" enter your age : "))
# print("Adult" if age>=18 else "not Minor")

# ETL: Print "Process File" if records > 0, otherwise "Empty File".
# records = 2000
# print("proccess file" if records > 0 else 'Empty file')

# Database: Print "Connected" if connection == True, otherwise "Connection Failed".
# connection = True
# print("True" if connection == 1 else "False")

# ------------LOOPS-------------------------------

# Practice Programs
# Write programs to:

#Print numbers from 1 to 10.
# for i in range(1,11):
#     print(i)

# Print numbers from 10 to 1.
# for i in range(10,0, -1):
#     print(i)

# Print even numbers from 1 to 20.
# for i in range(1,21):
#     if i%2 == 0:
#         print(i)

# Print odd numbers from 1 to 20.
# for i in range(1,21):
#     if i%2 != 0:
#         print(i)

# Print your name 5 times.
# for i in range(5):
#     print("Gaurav")

# Print the square of numbers from 1 to 10.
# for i in range(1,11):
#     print(f"SQUARE {i} : {i**2}")

# Print the cube of numbers from 1 to 10.
# for i in range(1,11):
#     print(f"CUBE {i} : {i**3}")

# Print numbers divisible by 5 between 1 and 50.
# for i in range(1,51):
#     if i%5 == 0:
#         print(i)

#  ----------------------------------STRING ITERATIONS -----------------------------------------

# Practice Programs
# Write programs to:
# String

# Print every character of "Python".
# charaters = 'python'
# for ch in charaters:
#     print(ch)

# # Print every character of your name.
# name = 'GAURAV'
# for ch in name:
#     print(name)

# Count how many characters are in your name (without using len()).
# name = input("Enter your name: ")
# count = 0

# for i in name:
#     count +=1
# print(count)

# Print only vowels from a string.
# name = 'i love python'
# for ch in name:
#     name1 = name.split()
# print(len(name1))

# Print only uppercase letters from a string.
# name = 'GaUrAv JagTaP'
# for ch in name:
#     if ch in (name.upper()):
#         print(ch)

# ----------------------- List ------------------------------------------

# Print all numbers from a list.
# numbers = [10,20,30,40,50]
# for i in numbers:
#     print(i)

# Print the square of every number in a list.
# numbers = [10,20,30,40,50]
# for ch in numbers:
#     square = ch**2
#     print(square)

# Find the sum of all numbers in a list.

# numbers = [93,45,67,84,10,20,30,40,50,1,2,3,4,5,6,7]
# total = 0
#
# for ch in numbers:
#     total += ch
# print(total)

# Print only even numbers from a list.
# numbers = [93,45,67,84,10,20,30,40,50,1,2,3,4,5,6,7]
# for ch in numbers:
#     if ch % 2 ==0:
#         print(ch)

# Print only numbers greater than 50.
# numbers = [93,45,67,84,10,20,30,40,50,1,2,3,4,5,6,7]
# for ch in numbers:
#     if ch > 50:
#         print(ch)

# ------------------ Frequently Asked Interview Questions ---------------------------------

# Find the sum of all numbers in a list.
# This is one of the first coding questions in Python interviews.

# Find the largest number in a list.
# We'll cover this next.

# Find the smallest number in a list.
# Very common.

# Count even and odd numbers in a list.
# Frequently asked.

# Find the average of numbers in a list.
# Uses the same logic as sum, plus a count.

# ------------------------------------------------------------------------------------------
# items : [ [1122, 850], [1123, 1200], [1124, 900] ]
# products = {}
# for i in items:
#     key,value = i
#     products[key] = value
# print(products)
# pid = int(input(" enter pid : "))
# print(f" cost is {products[pid]} ")