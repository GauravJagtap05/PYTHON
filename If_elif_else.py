# Q1
# A file should be processed only if:
# File exists
# Records >0
# Write Python code
# from pywin.idle.PyParse import ch

# File_Exists = True
# records = 2000
#
# if File_Exists:
#
#     if records > 10:
#         print(" load records", records)
# else:
#     print(" file does not exist")

# Q2
# Only execute SQL if:
# Database connection succeeds
# Transaction is active

# Q3
# ADF Pipeline
# Only load Gold Layer if
# Bronze completed
# Silver completed

# Q4
# Databricks
# Run transformation only if
# Cluster is running
# Input file exists

# Write programs to:
# Check whether a student passed; if yes, check whether they got distinction.
#
# marks = int(input(" enter students marks :"))
#
# if marks >35:
#     if marks >= 45 and marks <= 60:
#         print(" Student passed with average marks ", marks)
#
#     if marks > 65:
#         print(" Student passed with distinction", marks)
# else:
#     print("student failed ")
#
# Check whether a person is eligible to vote; if yes, check whether they are a senior citizen.
#
# age = int(input(" enter your age : "))
#
# if age >= 18:
#     print("you are eligible for voting")
#     if age >= 65:
#         print(" senior citizen")
# else:
#     print(" not elegible for vote")
#
# Check whether salary is above ₹50,000; if yes, check whether bonus is above ₹10,000.
#
# salary = int(input(" enter your salary: "))
# bonous = (salary) * 30/100
#
# if salary >= 50000:
#     print("you are eligible for bonous")
#     if bonous > 10000:
#         print("you bonous is : ", bonous)
# else:
#     print("you are NOT eligible for bonous")
#
# # Login system:
# # First check username.
# # Then check password.
#
# user_name = 'Gaurav05'
# password = 'Gaurav@12345'
#
# enter_username = input('Enter your username: ')
# enter_password = input('Enter your password: ')
#
# if user_name == enter_username:
#     print('Valid username')
#     if password == enter_password:
#         print(" logged in")
#     else:
#         print('Invalid password')
# else:
#     print('Invalid username')

# File Processing:
# Check file exists.
# Then check record count.

# ETL Pipeline:
# Check Bronze loaded.
# Then Silver.
# Then Gold.

# Database:
# Check connection.
# Then execute query.

# --------------------LOOPS--------------
# Printing patterns
# Factorial
# Prime numbers
# Fibonacci
# Armstrong numbers
# Palindromes

name = input("enter the string : ")
if name == name[::-1]:
    print(" is palindrome" , name)
else:
    print(" is not palindrome")


# Data processing
# File iteration
# Record validation
# Batch processing in Data Engineering