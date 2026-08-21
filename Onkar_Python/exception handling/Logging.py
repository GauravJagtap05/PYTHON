# logging

import logging

logging.basicConfig(
    filename="/Users/onkar/PycharmProjects/Python_gaurav/Onkar_Python/exception handling/mylog.txt",
    level=logging.DEBUG
)

try:
    a, b = [int(i) for i in input("Enter two nos: ").split()]
    c = a / b
    print("Result of div =", c)

except Exception as e:
    logging.error(e)