# EXCEPTION HANDLING

import logging

logging.basicConfig(filename = "d:/my_logs.txt", level = logging.ERROR)

class My_Exception(Exception):# WE ARE CREATING USER DEFINED EXCEPTION
    def __init__(self, str):
        self.str = str
        super().__init__(str)

def BankBalence(bank):
    for key,values in bank.items():
        print(" name = %s , amount %.2f" % (key,values))
        if values < 2000:
            raise  My_Exception(" amount balance low ")
bank = { 'gaurav':100000, "onkar":1000, "sandy":238, "ayush":983, "prajwal":90836}

try:
    BankBalence(bank)
except My_Exception as e:
    print(" exception is ", e)
    logging.exception(e)



# =============================================================================

# import logging
#
# logging.basicConfig(filename = "d:/my_logs.txt", level = logging.ERROR)
#
# try:
#     a,b = [int(i) for i in input("enter 2 numbers : ").split(' ')]
#     c = a/b
#     print(" result of division : ", c)
#
# except Exception as e:
#     logging.exception(e)

