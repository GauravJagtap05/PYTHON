## test basic logics
## print('Hello World')

##------

##a=4
##b=6
##print(a)

##---------
#
# declare mmore than 1 variable
# no. of variables and number of values should be same
# a,b = 3,6
# print(a,b)
# print(b)
#
## ---------

## consider pizza cost 300 customer 3 pizzas find bill
##pizza = 300
##qty = 3
##total_prize = 300*3
##print(total_prize)

##--------------

## print function
## from typing import Concatenate

## print('hello world')
## print(2+3)
# import sys
# print(sys.version)

## ---------------------

##first_name = 'Gaurav'
##last_name = 'Jagtap'
##fullname = (first_name +' '+ last_name)
## print(fullname)

##------------------------

## a='gaurav'
## print('its a great day',a)
## print(f'its a great day {a}')

## ------------------------

## consider annual salary is 60000 find monthly
## annual_salary = 60000
## monthly_salary = annual_salary/12
## print('monthly salary is', monthly_salary)
## print(f"monthly salary is {annual_salary/12}")

## --------------------------------------

## consider 1kg onions is 60 rs, customer took 5kg find bill amount
##kg_1 = 60
##qty=5
## print(f'total_bill is {kg_1*qty}')

## ---------------------------------------

## student marks are 95,90,94 findout total,avg and print total,avg
## a=95
## b=90
## c=94
## total = a+b+c
## avg = a+b+c/3
## print('total_marks are', total)
## print('avg_marks are', avg)
### print(f'total is = {a+b+c}')
### print(f'avg is = {a+b+c/3}')

## --------------------------------------------
## input function

## name = input("Enter your name: ")
## print('your name is', name)
## print(f'your name is',{name})
## A= int(input('enter number'))
## B= int(input('enter second number '))
## C= int(input('enter third number '))
## output = A+B+C/2
## print('your output is ',output)
## print('the sum is ',output)
## print(output)
## input values

## note : input always return a string value as a output
## note : if you need a number convert it using int or float.

## age = int(input("Enter your age: "))
## salary = float(input("Enter your salary: "))
## name = input("Enter your name: ")

## ---------------------------------

## wap to read ename and then print ename
## ename = input('enter your name: ')
## print('your name is ', ename)
## TO READ FULL NAME
## FIRST_NAME = input('enter your first name: ')
## LAST_NAME = input('enter your last name: ')
## full_name = FIRST_NAME + ' ' + LAST_NAME
## print('NAME:', full_name)

## -----------------------------------

## wap to read 2 integers and give sum
## a= int(input('enter the number'))
## b= int(input('enter the number'))
## c= a+b
## sum= a+b
## print('total',c)
## print(sum)

## ------------------------------------

## wap to read integer and 1 float vlaue then find multiplication
## a = int(input('enter the number'))
## b = int(input('enter the number'))
## MUL = a*b
## print(MUL)
## print('MULTIPLICATION :', MUL)

## ------------------------------------

## wap read employee salary and read employee monthly salary
## annual_salary = float(input("Enter annual salary: "))
## monthly_salary = annual_salary / 12
## print('monthly_salary :',monthly_salary)
## print(f'monthly salary using F string : {monthly_salary}')

## --------------------------------------

## wap consider a pizza cost = 500 then calcualte the total bill base on the quantity

## pizza = 500
## quantity = int(input(' Enter the quantity of the pizza :'))
## total_bill = pizza * quantity
## print('Total Bill INR :', total_bill)
## print(f'Total Bill INR : {pizza * quantity}')

## ----------------------------------------

## Relational operator

## wap condition to check customer is elegible for vote or not.
## age = int(input("enter your age: "))
## age >= 18
## if age > 18:
   ## print('elegible')
## else:
    ## print('not elegible')

## -------------------------------------------

## wap to check weather the number is divisible by 5
## condition -- num%5

## NUMBER = int(input('ENTER THE NUMBER :'))
## if NUMBER %5==0:
   ## print('the number is Divisible by:',NUMBER )
## else:
    ## print('the number is NOT Divisible by:',NUMBER)

## ----------------------------------------------

## wap to check given number is +ve or not
## condition -- n>0

## Number = int(input('Enter the number :'))
## if Number >0 :
   ## print('the number is positive',Number)
## else :
   ##  print("the number is Negative", Number)

## -------------------------------------------------

## if the number is elegible for discount or not
## condition is = bill amount is 5000+ then elegible for discount

## Billamount = float(input('enter the bill amount'))
## if Billamount >= 5000:
   ## discount = Billamount/0.15
   ## print('Elegible for Discount 15%')
   ## print('Discounted price :', discount)
## else :
   ## print('NOT Elegible for Discount')

## -----------------------------------------------------

## Conditional Statments
## W.a.c = Write a condition :

## 1. W.a.c to check if a record ID is greater than 1000 before inserting into DB
## Condition =  if no.Records_ID > 1000:

## 2. W.a.c to verify if data batch size is equal to expected size (500 rows).
## Condition = if no.batch_data == 500:

## 3. W.a.c to check if file size is less than 1MB, then process it.
## condition = if file_size < 1024* 1024:

## 4. W.a.c to check if number of failed records is not equal to 0.
## condition = if Number_failed_records != 0:

## 5. W.a.c to verify if data pipeline execution time exceeds 10 minutes.
## condition : if execution_time >timedelta(minutes=10) :

## 6. W.a.c to identify if customer rating is less than 3.
## condition : if customer_rating < 3 :

## 7. W.a.c to verify if ETL job status is not equal to 'Success'.
## condition : if status != Success:

## Status = int(input('Enter ELT status (1 = Success, 0 = Failure): '))
## Success = 1
## Failed = 0
## if Success == Status:
   ## print("Job is successfull")
## else:
   ##  print("Job is not successfull")

## ------------------------------------------

## Logical Operators:-
## AND , OR , NOT:-

## AND :-
## Person_age >= 18  AND Salary > 20,000:

## OR :-
## IF City == GOA OR City == Rajastan:

## NOT :-
## if not status == 'Success'
## Means: status is not success then do some operation

## wap to check student is pass or fail  s1>=35 and s2>=35 and s3>= 35

## Marks01 = int(input('Enter subject 1 marks'))
## Marks02 = int(input('Enter subject 2 marks'))
## Marks03 = int(input('Enter subject 3 marks'))

## TASK:
## WACondition to check customer is elegible for half ticket or not:
## Min age 5 years and Max age 11 years

## Min_age = int(input('enter Min_age of child :'))
## max_age = int(input('enter Max_age of child :'))

## if Min_age >= 5 and  max_age <= 11 :
   ##  print('Half Ticket')
## else:
   ##  print('Full Ticket')

## W.A.condition to Check user enter invalid marks or not
## except 0 to 100 it is invalid

## Marks = int(input('Enter Marks :'))
## if Marks>0:
   ## print('Marks is valid')   #Marks <=100:
## elif Marks <= 100:
   ## print('Marks is valid')
## else:
   ##  print('Marks is Invalid')

# WA condition the given characters is digits or not ?


## I have different files; I need to collect all files whose file size is min 1MB as
## well as record count is 1000+.


##I have data of different persons and different countries, but i want to collect
## all Indian person’s data whose age is 18+.


##I have India wise customer data, data is divided by region wise like north,
##south, east and west. now i need collect all records whose region is either
##South or North.

## ------------------------------------------

## Assignment Operator:
## Membership Operator: in,not in

## Courses =['python','DB','DataAnalytics','PowerBI','Excel','Django']
## C = input('enter course Name :')
## print(C in Courses)

## check e-mail is valid or not
## email = 'acdgroup@gmail.com'
## if '@' in email:
   ## print('valid email')

## --------------------------------------------

## control flow statments:
## wap to check weather the number is + or -

## n = int(input('Enter a number: '))
## if n>0:
   ## print('number is +ve ',)
## elif n<0:
   ## print('number is -ve')
## else:
   ## print('number is zero')


## wap to read 3 numbers then print the biggest number

## a=int(input('enter any number'))
## b=int(input('enter any number'))
## c=int(input('enter any number'))
## if a>b and a>c:
   ## print('biggest number is :',a)
## elif b>a and b>c:
   ## print('biggest number is :',b)
## else:
   ## print('biggest number is :', c)

## wap to read subject marks then find total avg and grade

## avg>70              --    grade - A
## avg>=60 and avg<70  --    grade - B
## avg>=50 and avg<60  --    grade - c

##num1 = int(input("Enter number 1: "))
##num2 = int(input("Enter number 2: "))
##num3 = int(input("Enter number 3: "))
##total= num1+num2+num3
##AVG = num1+num2+num3/3
##print('total marks: ',total)
##print('average marks: ',AVG)
##if AVG>70:
  ##  print(" Grade A")
##elif AVG>= 60 and AVG<70:
  ##  print('Garde B')
##elif AVG>=50 and AVG<60:
  ##  print('Grade C')
##else:
  ##  print('Garde D')

## --------------------------

## Multiple IF
## MORETHAN one IF THEN IT IS CALLED AS MULTIPLE IF

# n = 5
# if n>3:
#   n= n+5
# if n>7:
#   n= n-2
# print(n)


## Nested if
## A if inside of another if is called as nested if


## W.A.P to read a number if it is not zero then only check given
# n = int(input('Enter any number :'))
# if n!=0:
#     if n>0:
#         print("it is a +ve number")
#     else:
#         print('it is a negative number')
# else:
#     print('given number is zero')


# wap to check the age of person if it is +ve number then
# only check the person elegible for vote or not.
# otherwise display the message as invalid age
# age = int(input('Enter any number :'))
# if age>0:
#     if age>18:
#         print('person is elegible for vote')
#     else:
#         print('person is not elegible')
# else:
#     print('invalid age')


# wap to read number from 1-3 only, check n value ib b/w 1-3
# or not if yes print valid word
# n = int(input(' Enter number b/w 1 to 3 :'))
# if n>=1 and n<=3:
#     if n==1:
#         print('ONE')
#     if n==2:
#         print('TWO')
#     else:
#         print('THREE')
# else:
#     print('invalid choice')


# WAP
# 1. idly - 60    enter any choice -
# 2. Dosa - 100   cost =
# 3. Vaada - 80   enter quantity -
# 4. Puri - 120   bill anount -

# === WRONG CODE ===
# NUM = int(input(' enter any number b/w 1 to 4 :'))
# quantity = int(input(" enter Quantity :"))
# # bill =  quantity * Price

# if NUM > 0 and NUM <=4:
#     if NUM==1:
#         bill = quantity * 60
#         print("idly cost : 60")
#         print('Bill amount = ',bill )
#     elif NUM==2:
#         bill = quantity * 30
#         print(" Dosa cost : 30")
#         print('Bill amount = ', bill)
#     elif NUM==3:
#         bill = quantity * 80
#         print(' Vada cost : 80')
#         print('Bill amount = ', bill)
#     elif NUM == 4:
#         bill = quantity * 120
#         print(" Puri cost : 120")
#         print('Bill amount = ', bill)
# else:
#     print('invalid choice')
# ====== WRONG CODE ====

# === TASK 1===
# print('1. idly - 60 Rs')
# print('2. Dosa - 100 Rs')
# print('3. Vada - 80 Rs')
# print('4. Puri - 120 Rs')
# NUM = int(input('enter your choice:'))
# if NUM >0 and NUM <=4:
#     if NUM == 1:
#         item_name = 'idly'
#         cost = 60
#     elif NUM == 2:
#         item_name = 'Dosa'
#         cost = 100
#     elif NUM == 3:
#         item_name = 'Vada'
#         cost = 80
#     else:
#         item_name = 'Puri'
#         cost = 120
#     print(f'{item_name} cost is: {cost}')
#     quantity = int(input('Enter quantity:'))
#     BillAmount= cost *quantity
#     print(f" BillAmount is: {BillAmount}")
# else:
#     print(' Invalid Choice')

# TASK 2 FOLLOW UP TASK 1
#-------------------------
# print('1. idly - 60 Rs')
# print('2. Dosa - 100 Rs')
# print('3. Vada - 80 Rs')
# print('4. Puri - 120 Rs')
# NUM = int(input('enter your choice:'))
# if NUM >0 and NUM <=4:
#     if NUM == 1:
#         item_name = 'idly'
#         cost = 60
#     elif NUM == 2:
#         item_name = 'Dosa'
#         cost = 100
#     elif NUM == 3:
#         item_name = 'Vada'
#         cost = 80
#     else:
#         item_name = 'Puri'
#         cost = 120
#     print(f'{item_name} cost is: {cost}')
#     quantity = int(input('Enter quantity:'))
#     BillAmount = cost * quantity
#     CGST = BillAmount * .025
#     SGST = BillAmount * .025
#     TOTALBILL = BillAmount + CGST + SGST
#     PaidAmount = int(input('Given Amount:'))
#     BalanceAmount = PaidAmount - TOTALBILL
#     print(f" BillAmount is: {BillAmount}")
#     print(f' CGST(2.5%): {BillAmount * .025}')
#     print(f' SGST(2.5%): {BillAmount * .025}')
#     print('TotalBillAmount:',TOTALBILL)
#     print('Balance Amount:',BalanceAmount)
# else:
#     print(' Invalid Choice')

# TASK -3 FOLLOW UP TASK 2
#---------------------------
# print('1. idly - 60 Rs')
# print('2. Dosa - 100 Rs')
# print('3. Vada - 80 Rs')
# print('4. Puri - 120 Rs')
#
# choice = int(input('enter your choice:'))
#
# if choice == 1:
#     print('1. Idly - 60 Rs')
#     print('2. Onion Idly - 80 Rs')
#
#     Idly_choice = int(input('enter your choice:'))
#
#     if Idly_choice == 1:
#         item_name = 'Idly'
#         cost = 60
#     elif Idly_choice == 2:
#         item_name = 'Onion Idly'
#         cost = 80
#     else:
#         print('Invalid Idly Choice')
#         exit()
#
#
# elif choice == 2:
#        print('1. Plain Dosa - 100 Rs')
#        print('2. Onion Dosa - 120 Rs')
#        print('3. Masala Dosa - 140 Rs')
#        Dosa_choice = int(input('enter your choice:'))
#
#        if Dosa_choice == 1:
#            item_name = 'Plain Dosa'
#            cost = 100
#        elif Dosa_choice == 2:
#            item_name = 'Onion Dosa'
#            cost = 120
#        elif Dosa_choice == 3:
#            item_name = 'Masala Dosa'
#            cost = 140
#        else:
#             print('Invalid Dosa Choice')
#             exit()
#
#
# elif choice == 3:
#     print('1. Plain Vada - 80 Rs')
#     print('2. Vada Sambar - 100 Rs')
#
#     Vada_choice = int(input('enter your choice:'))
#
#     if Vada_choice == 1:
#         item_name = 'Plain Vada'
#         cost = 80
#     elif Vada_choice == 2:
#         item_name = 'Vada Sambar'
#         cost = 100
#     else:
#         print('Invalid Vada Choice')
#         exit()
#
# elif choice == 4:
#     item_name = 'Puri'
#     cost = 120
#
# print(f'{item_name} cost is: {cost}')
#
# quantity = int(input('Enter quantity:'))
#
# BillAmount = cost * quantity
#
# CGST = BillAmount * .025
# SGST = BillAmount * .025
#
# TOTALBILL = BillAmount + CGST + SGST
#
# print(f" BillAmount is: {BillAmount}")
# print(f' CGST(2.5%): {BillAmount * .025}')
# print(f' SGST(2.5%): {BillAmount * .025}')
#
# PaidAmount = int(input('Given Amount:'))
# BalanceAmount = PaidAmount - TOTALBILL
# print('TotalBillAmount:',TOTALBILL)
# print('Balance Amount:',BalanceAmount)




