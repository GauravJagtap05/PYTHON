# reverse a string:
# -------------------
# a = 'python'      # a string
# rev = ''          # take a empty reverse string
# for i in a:
#     rev = i + rev    #
# print(rev)
# -----------------------------
# z = a[::-1]
# print(z)
# print(type(z))
#
# # reverse a list:
# # ------------------
# a = [1,2,3,4,5,6,7,8,9]  # list
# b= a[::-1]               # start,stop,step -1 will take the list from end -1 is last index of a string
# print(b)
# print(type(b))

# # check palindrome number
# # ----------------------------
# a = input('enter a string : ')
# s = a[::-1]
# if s == a:
#     print('it is palindrom')
# else:
#     print(' not a palindrom ')
# ---------------------------------------------
# factorial number :
# ---------------------------------
# x = int(input('enter a number - '))
# fact = 1                     # HERA FACT = 1 WE HAVE TO TAKE AS FACT OF 1 IS 1 THEREFORE WE HAVE TO START FROM 1
#
# for i in range(1, x+1):
#     fact = fact * i
# print(fact)
# ------------------------------------
# Palindrome Number:

# N = int(input('enter the number : '))
# is_prime = True
#
# if N <2:
#     is_prime = False
# else:
#     for i in range(2, N):
#         if N % i == 0:
#             is_prime = False
#             break
#
# if is_prime:
#     print('Prime number')
# else:
#     print(" number is not prime")
#  ---------------------------------------------

# find largest number in list

a = [1,6,58,30,67,299,897]

largest = a[0]

for i in a:
    if i > largest:
        largest = i
print(largest)

#


