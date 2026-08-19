
# FOR LOOP
#----------
# loop based on group of elements
#--------------------------------

# a =[8,5,15,12,9]
# for i in a:
#     print(i)
# print('Thank You')

# Even Numbers
# a =[8,5,15,12,9]
# for i in a:
#     if i%2 ==0:
#         print('The number is even', i)
# print('Thank You')

# # Sum Of All Numbers
# a =[8,5,15,12,9]
# Sum =0
# for i in a:
#     Sum += i
# print(Sum)

# Sum of even and odd Numbers
# a =[8,5,15,12,9]
# Sumeven = 0
# Sumodd = 0
# for i in a:
#     if i%2==0:
#         Sumeven = Sumeven +i
#     else:
#         Sumodd = Sumodd +i
# print('Even Sum =',Sumeven)
# print('Odd Sum =',Sumodd)

# Range Function
#----------------
# range(start,stop,step)

# wap to print 1-10 numbers

# for i in range(1,10,1):
#     print(i)

# for i in range(10,1,-1):
#     print(i)


# for i in range(-20,-50,-3):
#     print(i)

# for i in range(-10,100,5):
#     print(i)

# for i in range(-20,-50,-3):
#     print(i, end='\t')

# wap to read n value then print numbers from 1 to n
# n = int(input('enter any number: '))
# for i in range(0,n+1,1):
#     print(i, end='\t')

# wap to read n values and then print sum of all even numbers b/w n
# n = int(input(" enter any number : "))
# sum = 0
# for i in range(1,n+1):
#     if i % 2 == 0:
#         sum = sum + i
# print('sum of even number is : ',sum)

# Factorial - product from 1 to n OR n to 1 of given number
# n = int(input('Enter Number : '))
# Factorial = 1
# for i in range(1,n+1):
#     Factorial = Factorial * i
# print(' Factorial is : ',Factorial)

# w.a.p to read n value then print
# all divisible for that number
# num = int(input('Enter the number : '))
# count =0
# for i in range(1, num+1):
#     if num % i ==0:
#         print(i,'\t')

# wap to check weather the number is prime or not:
# any number that is divisible 1 and itself it is called
# as prime number.
# n = int(input(' enter the number :'))
# count =0
# for i in range(1,n+1):
#     if n%i ==0:
#         count += 1
# if count == 2:
#     print(' the number is Prime : ',)
# else:
#     print('number is not Prime')

# NESTED LOOP
# LOOP INSIDE LOOP
#  WAP TO PRINT FOLLOWING SERIES


# for r in range(1,5):
#     for c in range(1,6):
#         print(c,end="\t ")
#     print()


# for r in range(1,5):
#     for c in range(1,r+1):
#         print(c,end="\t ")
#     print()

# wap to check given number is prime or not
# if it is then print that value other wise dont print value

# n = int(input(' Enter the Number : '))
# count = 0
# for i in range(1,n+1):
#     if n%i ==0:
#         count +=1
# if count ==2:
#         print(n)

# wap to print prime numbers between 1 to 100:
# for n in range(1,101):
#     count = 0
#     for i in range(1,n+1):
#         if n%i ==0:
#             count += 1
#     if count ==2:
#         print(n,end='\t')

# wap to read multiple values from user then find sum
# sum = 0
# ch = 'y'
# while ch=='y':
#     n = int(input('enter any number: '))
#     sum = sum+n
#     ch = input('do you want to continue (y/n): ')
# print('sum is : ', sum)

#wap to read multiple numbers from user
#then find sum of even numbers only
# sum= 0
# ch='y'
# while ch=='y':
#     n = int(input('enter any number: '))
#     if n%2==0:
#         sum = sum+n
#         ch = input('do you want to continue (y/n): ')
# print(" sum is : ",sum)

# TRANSFER STATEMENT
# To move control from one place to another place
# we need to use transfer statement.

# 1= BREAK    - when break occured then control
# iterations then goes outside loop.

# 2= CONTINUE - when continue occured then it stops current iteration then
# continue for next iteration.

# == BREAK EXAMPLE ==
# a =[5,9,12,8,10]
# n = int(input('enter any number : '))
# c=0
# for i in a:
#     if i==n:
#         c+= 1
#         break
# if c==0:
#     print('sorry number is not available')
# else:
#     print('number is available')

# == CONTINUE EXAMPLE ==
# a =[5,9,12,8,10]
# b =[10,13,56,23,46]
# n = int(input('enter any number : '))
# c=0
# for i in a:
#     if i==n:
#         c+= 1
#         continue
# for i in b:
#     if i==n:
#         c+= 1
#         break
# if c==0:
#     print('sorry number is not available')
# else:
#     print('number is available')

# FOR - ELSE:

# a =[5,9,12,8,10]
# n = int(input('enter any number'))
# for i in a:
#     if i==n:
#         print(f' {n} available')
#         break
# else:
#     print(f' {n} not available')

# CHECK IF DATA FILES CONTAINS ERRORS OR NOT:

# data = [10,20,30,-5,40]
#
# for value in data:
#     if value <0:
#         print(' invalid data found:',value)
#         break
# else:
#     print('all data is valid')


# age = '26'
# print(type(age))
#
# x = True
# y= False
# print(type(x))

# # data = none
# data1 = None
# # data2 = NONE

# # print(type(data))
# print(type(data1))
# # print(type(data2))

# a = 10
#
# b = float(a)
#
# print(b)
# print(type(b))

# salary = 55000.75
# print(int(salary))

# age = 25
#
# age_str = str(age)
#
# print(age_str)
# print(type(age_str))
#
# age = '25'
# print(type(age_str))
#
# num = "100"
# print(type(num))
# print(type(int(num)))

# num = "ABC"
# print(type(num))
# int(num) --- ERROR as string ABD is not a number value


# print(int(5.9))
#
# # float = 5.9
# # print(int(float))
#
# age = input("Enter age: ")
# print(age)
# print(type(age))


# a,b,c = map(int , input(). split())
# count caracter frequency:

# name = input(" enter string ")
# count = {}
# for ch in name:
#     if ch in count:
#         count[ch]+=1
#     else:
#         count[ch] = 1
# print(count)





