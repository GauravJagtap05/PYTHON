# User-defined exception

class MyException(Exception):
    def __init__(self, str):
        self.str = str


def check(bank):
    for k, v in bank.items():
        try:
            print(f"name = {k} balance = {v}")
# we write try and except in for as if we write outside then exception arrives and the code stops
            if v < 2000:
                raise MyException("Balance amount is less than 2000.")

        except MyException as e:
            print("Error:", e)

bank = {
    'raju': 500.75,
    'sita': 54554,
    'amit': 12500.50,
    'neha': 78000.25,
    'rohit': 1500.00,
    'priya': 45670.80,
    'vijay': 3200.00,
    'anjali': 92500.40,
    'rahul': 1800.50,
    'pooja': 34000.60
}

check(bank)