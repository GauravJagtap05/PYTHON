# def decor():
#     def decor(my_func):
#         def inner():

'''

def decor(my_function):
    def inner():
        res = my_function()
        res = res + 10
        return res
    return inner

def my_function():
    return 100

x = decor(my_function)
res = x()
print(res)

x = decor(my_function)
res =x()
print(res)

'''