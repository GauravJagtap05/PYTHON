#
# transactions = [
#     {"id": "T101", "customer": "C01", "amount": 5000, "status": "SUCCESS"},
#     {"id": "T102", "customer": "C02", "amount": 1500, "status": "FAILED"},
#     {"id": "T103", "customer": "C01", "amount": 7500, "status": "SUCCESS"},
#     {"id": "T104", "customer": "C03", "amount": 2000, "status": "SUCCESS"},
#     {"id": "T105", "customer": "C02", "amount": 9000, "status": "SUCCESS"}
# ]
#
# # Write Python code to calculate the total successful transaction amount for each customer.
#
# # customer ---->  total successfull amount
# total_amount ={}
#
# for i in transactions:
#     if i['status'] == 'SUCCESS':
#         customer = i['customer']
#         amount= i['amount']
#         if customer not in total_amount:
#             total_amount[customer] = 0
#             total_amount[customer] += amount
# print(total_amount)

# n = int(input('enter the number'))
# result = 0
# place = 1
# while n > 0:
#     digit = n % 10
# -----------------------------------------------------------------------
# # Q2 — Loops + Conditions
# amounts = [500, 15000, 2500, 75000, 120000, 3000, 45000]
# # Create a Python program that categorizes each transaction:
# # expected output:--
# # < 10000       → LOW
# # 10000-50000   → MEDIUM
# # 50001-100000  → HIGH
# # > 100000      → VERY_HIGH
#
# for i in amounts:
#     if i < 10000:
#         print('Low Balance',i)
#     elif 10000 <= i <= 50000:
#         print('Medium balance',i)
#     elif 50001 <= i <= 1000000:
#         print("High balance",i)
#     else:
#         print('very high balance',i)
# -------------------------------------------------------------------------
#  Q3
# Create a function:
# calculate_transaction_fee(amount, transaction_type)
# UPI:
#     < 1000       → 0
#     >= 1000      → 0.5%
#
# CARD:
#     < 5000       → 1%
#     >= 5000      → 1.5%
#
# BANK_TRANSFER:
#     → 0.2%

# N = input('enter transaction type b/w A,B,C:')
# Transaction_type =['UPI',"CARD",'BANK_TRANSFER']

# def calculate_transactions(amount, Transaction_type):
#     if Transaction_type == 'UPI':
#         if amount < 1000:
#             print('fees is 0',amount)
#         elif amount >= 1000:
#             fees = amount * (0.5 * 1/100)
#             return fees
#             print(f'Amount = {amount} fees = {fees}')
#
#     if Transaction_type == 'CARD':
#         if amount < 5000:
#             fees = amount * 0.01
#             return fees
#             print(f'Amount = {amount} fees = {fees}')
#         elif amount >= 5000:
#             fees = amount * (1.5 * 1/100)
#             return fees
#             print(f'Amount = {amount} fees = {fees}')
#
#     if Transaction_type == 'BANK_TRANSFER':
#         fees = amount * (0.2 * 1/100)
#         return fees
#         print(f'Amount = {amount} fees = {fees}')
#
# e = calculate_transactions(5678,'CARD')
# ---------------------------------------------------------------------
# Q4 — Dictionaries + Functions
# transactions = [
#     {"customer": "C01", "amount": 5000},
#     {"customer": "C02", "amount": 1500},
#     {"customer": "C01", "amount": 3000},
#     {"customer": "C03", "amount": 8000},
#     {"customer": "C02", "amount": 2000},
# ]
# WRITE A FUNCTION
# {
#     "C01": {
#         "transaction_count": 2,
#         "total_amount": 8000
#     },
#     "C02": {
#         "transaction_count": 2,
#         "total_amount": 3500
#     },
#     "C03": {
#         "transaction_count": 1,
#         "total_amount": 8000
#     }
# }


# for i in transactions:
#     if i['status'] == 'SUCCESS':
#         customer = i['customer']
#         amount= i['amount']
#         if customer not in total_amount:
#             total_amount[customer] = 0
#             total_amount[customer] += amount
# print(total_amount)


# n = int(input('Enter a number: '))
# count = 0
# for i in range(2, n):
#     if n % i == 0:
#         count += 1
#         break


# x = int(input("enter the first number "))
# y = int(input("enter the Second number "))
#
# print('x = ',x)
# print('y = ',y)
# print('----------------------')
#
# x,y = y,x
#
# print('x = ',x)
# print('y = ',y)
# --------------------------------------------

a = 123
reverse = 0
while  a > 0:
    a = a % 10
    reverse = reverse * 10 + a
    a = a // 10
print(a)

