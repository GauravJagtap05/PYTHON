
import logging

logging.basicConfig(filename = "d:/my_logs.txt", level = logging.ERROR)

try:
    a,b = [int(i) for i in input("enter 2 numbers : ").split(',')]
    c = (a / b)
    print(" result of division : ", c)

except Exception as e:
    logging.Exception(e)
