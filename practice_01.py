
# String
# - simple sequence of char
# - string are immutable


# s = 'gaurav jagtap'
# print(s)
#
# s1 = 'gaurav'
# print(s1[0])
# print(s1[-1])
# print(s1[0:6]) --- string slicing
# print(s1[-1]) -- slicing from revers
# print(s1[::]) -- whole string
# print(s1[::-1]) # reverse string

# display all characters using for loop

# string is defined
# s = 'assignment string'
# for i in s:
#     print(i,end= '\t')

# string using input
# s = input('enter a string')
# for i in s:
#     print(i,end= '\t')

# write a program to read a string and print only vowels
# str = 'string vowels'
# for i in str:
#     if i in 'aeiou':
#         print(i, end='\t')

# write a program and print only lower case characters

# str = 'GauRaV JAgTap'
#
# # for i in str:
# #     if i>='a' and i<='z':
# #         print(i,end='\t')
#
# for i in str:
#     if 'A'<=i<='Z':
#         print(i,end='\t')

# write a program to read a string and read only symbols:

# str1 = '$g#a^rV g*r@ou&p'
#
# for i in str1:
#     if not('a'<=i<='z' or 'A'<=i<='Z' or '0'<=i<='9' or i==''):
#         print(i,end='\t')
# -----------------------------------------------
# METHODS:
# upper() -- to convert into upper case
# lower() -- to convert into lower case

# str = "gaurav jagtap"
# str1 = str.upper()
# str2 = str.lower()
# print(str1)
# print(str2)
# ------------------------------------------
## value comparision

# 1-- using ==
# 2-- using startswith() method
# 3 -- 2-- using endswith() method
# ---------------------------------------------
# NOTE :--
# 1- to compare COMPLETE STRING -- USE -- ==
# 2- to compare STARTING PART OF STRING  -- USE -- startswith()
# 3 - to compare ENDING PART OF STRING -- USE -- endswith()

# code = '1122'
# ht = '1122CSE001'
# if(ht.startswith(code)):
#     print('belongs to our college')
#
# emailid = input('enter your google id : ')
# if (emailid.endswith('@gmail.com')):
#     print('valid google id')
# else:
#     print('invalid id :')

# 5 - INDEX() - GET INDEX OF A GIVEN CHARACTERS
# 6 - COUNT() - COUNT NO. of occurence of a given character
# ---------------------------------------------------------------
# s1 = 'gaurav jagtap'
# characters = input('input any characters')
# A = s1.index(characters)
# print(A)

# s1 = 'gaurav jagtap'
# characters = input('input any characters :')
# A = s1.find(characters) != -1
# print(A)

# s1 = 'gaurav jagtap'
# characters = input('input any characters : ')
# A = s1.find(characters)
# print(A)

# characters = input('input any characters : ')
# A = s1.index(characters)
# print(A)

# 7. replace()
# used to replace existing char/string  with NEW char/string
# s1 = 'gaurav jagtap'
# s2 = s1.replace('gaurav' , 'shweta')
# print(s2)

#8. split()
# used to divide a given string into multiple parts based on given char
# incase user dosent specify any char then it will split based on spaces

# s1 = 'core python and adv python both are important for begineers'
# s2 = s1.split()
# s3 = s2.index('python')
# print(s2)
# print(s3)

#9. strip()
# remove all the spaces before and after the string

# s1 ='   avd   group  '
# s2 ='gaurav jagtap '
# s3 ='  bhavna wadaskar '
# s4 ='s wh eta b ho wat e r' --- this will remain same
# s5 = s1.strip()
# s6 = s2.strip()
# s7 = s3.strip()
# s8 = s4.strip()
# print(s5)
# print(s6)
# print(s7)
# print(s8)

#10. join -- use to jon the string

# words1 = ['Data' , 'Engineer']
# words2 = ['1','2','3']
# print(''.join(words1))
# print(''.join(words2))
#
# #11. format() -- used to insert values into a string dynamically
#
# name = input('enter the username : ')
# age = input('enter the age : ')
# log = ' user : {} | age : {}'.format(name,age)
# print(log)

# 12 isupper() - string in upper or not
# 13 islower() - string in lower or not
# 14 isdigit() - given string is digit or not
# 15 isalnum() - string may alphabet or digit

# 16 len() -- to find len of string

# sq = 'gaurav jagtap'
# print(len(sq))


# ---------------------------------------------------------
# === Assignment ===
# ---------------------------------------------------------

# Taks 01 -
# data = " 101 , Kiranjeet , 50000 "
#Expected: ['101', 'Kiranjeet', '50000']

# #Data = " 101 , Kiranjeet , 50000 "
# s2 = Data.split(',')
# print(s2)

# ------------------------------------------

# Task 02 - Email Validation
# # check valid or not
# email = "test@gmail.com"

# inputemail = input('enter your google emialid')
# if inputemail.endswith('@gmail.com'):
#     print('valid email id')
# else:
#     print('invalid email id')

# ------------------------------------------

# Task 03 Salary Extraction
# data = "Rishi-50000"
# # Extract name and salary

# data = "Rishi-50000"
# name,salary= data.split("-")
# print('Name : {}'.format(name))
# print('Salary : {}'.format(salary))

#---------------------------------------------

# Task 4 - Remove Duplicates Words
# text = "data data engineer engineer"
# Output: "data engineer"

# text = "data data engineer engineer"
#
# words = text.split()
# result = []
#
# for word in words:
#     if word not in result:
#         result.append(word)
#
# output = " ".join(result)
#
# print(output)

# ----------------------------------------------

#Task 5 Extract File Extension
# file = "data.csv"
# # Output: csv
#
# file2= file.split(".")
# print(file2[1])

# --------------------------------------------------
# Task 6 Filter Only CSV Files
# files = ["data.csv", "report.txt", "sales.csv"]
# Output: ["data.csv", "sales.csv"]
#
# for i in files:
#     if i.endswith('.csv'):
#         print(i)

# -----------------------------------------------

# Task 7 Mask Sensitive Data
phone = "9876543210"
# # Output: "987****210"

for i in range(10):






# -------------------------------------------------
# Task 8 Convert CSV into Scentence
