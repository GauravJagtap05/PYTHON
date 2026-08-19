# == Functions ==
# def withdrawal():
#     print('hai')
# withdrawal()
# print('thank you')
from os import name

# withdrawal()
# def withdrawal():
#     print('hai')
# print('thank you')

# def f1():
#     print('hai')
# def f2():
#     print('hello')
#
# def f1():
#     f2()
#     print

# def withdrawal(amt):
#     print(amt)
# # withdrawal(500)

# def calsquare(n):
#     sq = n*n
#     print(sq)
# a = int(input('enter the number'))
# calsquare(a)


# ## call any function 3 points:
# 1. function name
# 2. no. of parameters
# 3. return keyword


# def CheckBig(a,b):
#     if a>b:
#         return a
#     else:
#         return b
# big = checkBig(a,b)
# print(f" big number is : {big}")

# Assignment 07
# -------------
# 1. create a function to find monthly salary of an employ by taking annual salary as a parameter

# def annual_salary_function(annual_salary):
#     salary_monthly = annual_salary / 12
#     return salary_monthly
#
# annual_salary = int(input('enter annual CTC : '))
# salary_monthly = annual_salary_function(annual_salary)
# print('monthly_salary :',salary_monthly)

# 2. create a function to return biggest number by taking a,b as parameters

# def big_number(a,b):
#     if a >b:
#         return a
#     else:
#         return b
# a = int(input('enter first number: '))
# b = int(input('enter second number: '))
# big = big_number(a,b)
# print(f'big number is : {big}')

# 3. create a function to find given number is even or odd by taking n as parameter:

# def func_EvenorOdd(n):
#     if n%2==0:
#         print('even :', n)
#         return n
#     else :
#         print('odd :', n)
#         return n
#
# n = int(input('enter a number : '))
# even_odd = func_EvenorOdd(n)

# 4. create a function to find smallest number by taking array as parameter:

# def main_array(arr):
#     big = arr[0]
#     for i in arr:
#         if i >big:
#             big = i
#     return big
#
# a =( int(input('Enter a number: ')),
# int(input('Enter a number: ')),)

# 5: create a function to given string is palindrome or not by taking string as parameter:

# def is_pal(text):
#     if text == text[::-1]:
#         return True
#     else:
#         return False
#
# word = input(' Enter a word : ')
#
# if is_pal(word):
#     print('Is palindrom', word)
# else:
#     print(' Not a Paliondrom', word)

# 6: create a function to find sum of all elements by taking arry as parameter

# def array_sum(arr):
#     total=arr[0]
#     for a in arr:
#         total+=a
#     return total
#
# numbers =[1,2,3,4,5,6,7,8,9]
# print(array_sum(numbers))

# -------------------
## FACTORIAL OF N :-
#--------------------

#  ## n = n*(n-1)
#
# def factorial(n):
#     fact =1
#     for i in range(1,n+1):
#         fact = fact * i
#     return fact
#
# f = factorial(5)
# print(f)

# NOTE =========================================
# IN RANGE FUNCTION THE N IS EXCLUDED FROM (1,N)
# THE RANGE WILL BE (1, N-1 )TO
# GET THAT NTH VALUE WE GIVE (1,N+1)
# TO INCLUDE THE NTH VALUE.
# ==================================================

# FUNCTIONS -- RECURSIVE FUNCTIONS -- LAMBDA FUNCTIONS
#
# LAMBDA FUNCTIONS:
#
# -- lambda functions are called as anonymous functions
# they are mname less functions
#
# -- functions are declared using lambda function
#
# -- if logic is smal lthen go for lambda functions dont
#     go for comples logics
#
# example:
#
# def calsquare(n):
#     sq = n*n
#     return sq
#
# s= calsquare(5)
# print(s)
#
# lambda functions :

# some variable to store = lambda parameter required: logic

# result = lambda n:n*n
# print(result(5)) -- to call the function

# result = lambda n,m:n+m
# print(result(n,m))

# a>b:
# result = lambda a,b: a if a>b else b
# print(result(7,9))
#
# odd even
# result = lambda n: 'even' if n%2 ==0 else "odd"
# print(result(5))
#
# a>b>c
# result = lambda a,b,c:a if a>b and a>c else b if a>c else c

# map function
# in lambda there is map function if you want to perform
# some operation on group of list tuple or set
#
# map takes 2 input
# 1- lambda function
# 2- your list

## -- MAP():-
# sal = [1,2,3,4,5]
# newsal = list(map(lambda a: a+ 6, sal))
# print(newsal)

## -- FILTER() :-
# sal = [1,2,3,4,5]
# newsal = list(filter(lambda a : a<2, sal))
# print(newsal)

## -- REDUCE() :-
# it takes list and keep combining 2 items at a time
# until you get a final result
# it is available in functions tools module -- (functools)

# from functools import reduce
# a = [5,12,7,8,10]
# result = reduce(lambda x,y: x+y, a)
# print(result)