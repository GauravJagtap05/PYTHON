
# WORKING WITH DEFAULT VARIABLES

from pydantic import BaseModel
from typing import List , Dict

# IN PYDANTIC :-
# 3 STEPS -- for validation
# STEP 1 - CREATE A BASE MODEL CLASS WE HAVE TO WRITE-- IN THIS MODEL WE SHOULD DEFINE THE DATATYPES AND CONSTRAINTS
# STEP 2 - CREATE AN OBJECT TO AN BASE MODEL CLASS & PASS DATA TO THIS OBJECT
# STEPS 3 - PASS THE BASE MODEL OBJECT TO FUNCTIONS

 # -----------------------------------------------------------------

from pydantic import BaseModel
from typing import List , Dict

# STEP 1 - CREATE A BASE MODEL CLASS WE HAVE TO WRITE-- IN THIS MODEL WE SHOULD DEFINE THE DATATYPES AND CONSTRAINTS
class Emp(BaseModel):
    name: str
    age : int
    sal : float = 45000.00       # here 45000 is the default value if salary is not mentioned it will by default take 45000 by default
    married : bool = False  # false by default value
    qualification : list[str] = ['B.tech']   # B tech default va;ue
    contact : Dict[str, str] = None # None by default value

# STEPS 3 - PASS THE BASE MODEL OBJECT TO FUNCTIONS

def Insert_emp_data(obj: Emp):
    print(obj.name)
    print(obj.age)
    print(obj.sal)
    print(obj.married)
    print(obj.qualification)
    print(obj.contact)
    print('inserted into db')

# STEP 2 - CREATE AN OBJECT TO AN BASE MODEL CLASS & PASS DATA TO THIS OBJECT
Info = {'name':'Gaurav','age':28}
obj = Emp(**Info)

Insert_emp_data(obj)

# -----------------------------------------------------------------------

# WORKING WITH OPTIONAL VARIABLES

from pydantic import BaseModel
from typing import List , Dict , Optional         # here we have to  importing OPTIONAL class with list dict

# STEP 1 - CREATE A BASE MODEL CLASS WE HAVE TO WRITE-- IN THIS MODEL WE SHOULD DEFINE THE DATATYPES AND CONSTRAINTS
class Emp(BaseModel):
    name: str
    age : int
    sal : Optional[float] = None      # we have to give optional key word before every variable
    married : Optional[bool ]= False                   # false by optional value # - here we cannot skip the variable value we have to enter some data (or) we have to enter the none value
    qualification : Optional[list[str] ]= ['B.tech']   # B tech optional value
    contact : Optional[Dict[str, str]] = None          # None by optional value

# STEPS 3 - PASS THE BASE MODEL OBJECT TO FUNCTIONS

def Insert_emp_data(obj: Emp):
    print(obj.name)
    print(obj.age)
    print(obj.sal)
    print(obj.married)
    print(obj.qualification)
    print(obj.contact)
    print('inserted into db')

# STEP 2 - CREATE AN OBJECT TO AN BASE MODEL CLASS & PASS DATA TO THIS OBJECT
Info = {'name':'Gaurav','age':28}
obj = Emp(**Info)

Insert_emp_data(obj)

# ----------------------------------------------------------

from pydantic import BaseModel
from typing import List , Dict , Optional         # here we have to  importing OPTIONAL class with list dict

# STEP 1 - CREATE A BASE MODEL CLASS WE HAVE TO WRITE-- IN THIS MODEL WE SHOULD DEFINE THE DATATYPES AND CONSTRAINTS
class Emp(BaseModel):
    name: str
    age : Optional[int]  # here age is optional variable
# STEPS 3 - PASS THE BASE MODEL OBJECT TO FUNCTIONS

def Insert_emp_data(obj: Emp):
    print(obj.name)
    print(obj.age)
    print('inserted into db')

# STEP 2 - CREATE AN OBJECT TO AN BASE MODEL CLASS & PASS DATA TO THIS OBJECT
Info = {'name':'Gaurav','age': None}  # here we have to mention variable name weather we will pass data to the variable or not just mention the name and pass none value to the variable
obj = Emp(**Info)

Insert_emp_data(obj)

# ------------------------------------------------------------------------
# VALIDATING EMAIL'S AND URL'S

from pydantic import BaseModel, EmailStr, AnyUrl # we have to import  EmailStr and AnyUrl class

# STEP 1 - CREATE A BASE MODEL CLASS WE HAVE TO WRITE-- IN THIS MODEL WE SHOULD DEFINE THE DATATYPES AND CONSTRAINTS
class Emp(BaseModel):
    name : str
    age : int
    email : EmailStr
    linkedin : AnyUrl


# STEPS 3 - PASS THE BASE MODEL OBJECT TO FUNCTIONS
def display(e: Emp):
    print(e.name)
    print(e.age)
    print(e.email)
    print(e.linkedin)


# STEP 2 - CREATE AN OBJECT TO AN BASE MODEL CLASS & PASS DATA TO THIS OBJECT
Data = {"name": "Johan", 'age': 25, "email": "John123@gmail.com", 'linkedin': 'https://linkedin.com/john-1234'}

e = Emp(**Data)
display(e)

# ------------------------------------------------------------------------
# CONSTRAINTS OR CONDITIONS:--

from pydantic import BaseModel, Field
from typing import List

# STEP 1 - CREATE A BASE MODEL CLASS WE HAVE TO WRITE-- IN THIS MODEL WE SHOULD DEFINE THE DATATYPES AND CONSTRAINTS
class Emp(BaseModel):
    name: str = Field(max_length = 15)
    age : int = Field(ge=20, le=60)
    sal: float = Field(gt=30000.00)
    qualification: list[str] = Field(max_length=2)  # max element in this list should be equal to 2

# STEPS 3 - PASS THE BASE MODEL OBJECT TO FUNCTIONS
def display(e: Emp):
    print(e.name)
    print(e.age)
    print(e.sal)
    print(e.qualification)


# STEP 2 - CREATE AN OBJECT TO AN BASE MODEL CLASS & PASS DATA TO THIS OBJECT
dict = {'name':'John' , 'age': 32, 'sal': 45000.00, 'qualification': ['B.tech']}
e = Emp(**dict)

display(e)
