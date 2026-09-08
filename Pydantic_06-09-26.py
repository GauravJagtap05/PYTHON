
# - dictionary unpacking operator
# -----------------------------------
import pydantic

def myfun(**x):                      # ** -> (it is a unpacking operator)
    for k,v in x.items():            # here items is a method that takes values from dictionary in k,v form
        print(k,v)                   # display key - value pair

# pass a dictionary
dt = {'name':'John','age':25,'city':'Pune'}
myfun(**dt)

# 2 and option we can directly give the  unpacked dictionary while calling the function
# un[packed data we won't give-it in key:value pair we give it in key=value
myfun(name='John', age=25, city='Pune')


## how to validate (string) and how to validate (INT)
# CHECK THE ABOVE GIVEN STRING AND INT VALIDATION

# ---------------------------------------------------------------------------------------------
#  Q1
#  validate student roll_no and name using pydantic
#  roll no == int and name == string

# IN PYDANTIC :-
# 3 STEPS -- for validation
# STEP 1 - CREATE A BASE MODEL CLASS WE HAVE TO WRITE-- IN THIS MODEL WE SHOULD DEFINE THE DATATYPES AND CONSTRAINTS
# STEP 2 - CREATE AN OBJECT TO AN BASE MODEL CLASS & PASS DATA TO THIS OBJECT
# STEPS 3 - PASS THE BASE MODEL OBJECT TO FUNCTIONS

# TYPE VALIDATION USING PYDANTIC

# # STEP 1 - CREATE A BASE MODEL CLASS WE HAVE TO WRITE-- IN THIS MODEL WE SHOULD DEFINE THE DATATYPES AND CONSTRAINTS
# from pydantic import BaseModel
# class Student(BaseModel):
#     rno: int
#     name : str
#
# # STEPS 3 - PASS THE BASE MODEL OBJECT TO FUNCTIONS
# def display(z: Student):
#     print(" Student rno = ",z.rno)
#     print(" Student rno = ",z.name)
#
# #  OR using OOP'S how will write using the class
# # ------------------------------------------------
# class Myclass:
#     def display(z: Student):
#         print(" Student rno = ", z.rno)
#         print(" Student rno = ", z.name)
#
# # STEP 2 - CREATE AN OBJECT TO AN BASE MODEL CLASS & PASS DATA TO THIS OBJECT
# data ={'rno': 101, 'name': 'Gaurav Jagtap'}       # Data can be passed in 2 form key value arguments or dictionary
# z = Student(**data)
#
# #  OR
# # ------
# z = Student(rno= 101, name= 'Gaurav Jagtap')  # 2nd form key value arguments
#
# m = Myclass()
# m.display(z)

# ------------------------------------------------------------------------------
#  how to work with DATE datatype and DATETIME datatype
#
# date -> 2026/9/6
# datetime -> 2026/9/6, 14,30,25
#
# DATE TYPE VALIDATION USING PYDANTIC
# STEP 1 - CREATE A BASE MODEL CLASS WE HAVE TO WRITE-- IN THIS MODEL WE SHOULD DEFINE THE DATATYPES AND CONSTRAINTS

from pydantic import BaseModel
from datetime import date    # -- or datetime

class Event(BaseModel):
    title: str
    dt: date  #or dt: datetime

# STEPS 3 - PASS THE BASE MODEL OBJECT TO FUNCTIONS
def Display(e: Event):
    print("Event = ",obj.title)
    print("Date = {}/{}/{} ".format(obj.dt.day,obj.dt.month,obj.dt.year))

    # or --
    # print("On = {}/{}/{} ".format(obj.dt.day,obj.dt.month,obj.dt.year))
    # print("At = {} ( / or : ) {} ".format(obj.dt.hour,obj.dt.minute))


# STEP 2 - CREATE AN OBJECT TO AN BASE MODEL CLASS & PASS DATA TO THIS OBJECT
D = {'title':'python class', 'dt':date(2026,9,5) }
# -- OR
# D = {'title':'python class', 'dt':datetime.now() or today() } to get the current time
obj = Event(**D)

Display(obj)

# ----------------------------------------------------------------------------------
# TYPE VALIDATION for group of objects
#  how to work with DATE datatype and DATETIME datatype

# STEP 1 - CREATE A BASE MODEL CLASS WE HAVE TO WRITE-- IN THIS MODEL WE SHOULD DEFINE THE DATATYPES AND CONSTRAINTS.

from pydantic import BaseModel
from datetime import date
from typing import List , Dict

class Emp(BaseModel):
    name : str
    age : int
    doj : date
    Married : bool
    qualification : List[str]
    contact : Dict[str, str]

# STEPS 3 - PASS THE BASE MODEL OBJECT TO FUNCTIONS

def insert_emp_data(e: Emp):
    print(e.name)
    print(e.age)
    print(e.doj)
    print(e.Married)
    print(e.qualification)
    print('Mobile No: ', e.contact['MobNo'])
    print('Address : ', e.contact['Add'])
    print(' Inserted into Db')


# STEP 2 - CREATE AN OBJECT TO AN BASE MODEL CLASS & PASS DATA TO THIS OBJECT.

info = {'name': 'john', 'age':34, 'doj': date(2000,10,15),
        'Married':True, 'qualification':['Btech','Mtech'], 'contact':{'MobNo' : '+91 - 9284354631', 'Add':'plot no 33, AVD Office Ravet, Punewale'}}

e =Emp(**info)
insert_emp_data(e)