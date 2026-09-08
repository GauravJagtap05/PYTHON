# META DATA

from pydantic import BaseModel, Field
from typing import Annotated, Any, Self


class Emp(BaseModel):
    name : Annotated[str, Field(max_length = 15,
                                title = 'Enter name of the employee',
                                description= 'Name should be less than 15 characters',
                                examples=['Ashok', 'vijay Kumar'])]

    age : Annotated[int, Field(gt=20, le=60,
                               title= 'Enter age',
                               description='Age should between 20 & 60')]

    sal : Annotated[float, Field(title='Enter Salary',
                                 description='Please Enter salary',
                                 default=30000.00)]  # default variable is added inside field()

def Display(e: Emp):
    print(e.name)
    print(e.age)
    print(e.sal)
    print('-----------------------------------------------------')


# create an object to emp class
data ={"name":'john Donald','age':30,'sal':900000.00}
e=Emp(**data)
Display(e)

# ---------------------------------------------------------------
# strict validation

from pydantic import BaseModel
from pydantic import StrictInt, StrictFloat, StrictStr

class Emp(BaseModel):
    name:StrictStr
    age:StrictInt
    salary:StrictFloat

def Display(e: Emp):
    print(e.name)
    print(e.age)
    print(e.salary)
    print('------------------------------------------')

e = Emp(name='ramesh', age=89, salary=54332.25)
Display(e)

# -------------------------------------------------------
# strict validation inside field class

from pydantic import BaseModel
# from pydantic import StrictInt, StrictFloat, StrictStr
from typing import Annotated

class Emp(BaseModel):
    age: Annotated[int, Field(ge=20, le=60,
                              title='enter age',
                              description='enter age in the range of 20 to 60',
                              examples=[20,35,45,60],
                              strict=True)]

    Salary: Annotated[float, Field(default=30000.00,
                              description='enter employee salary',
                                   strict=True)]

def Display(e: Emp):
    print(e.age)
    print(e.Salary)
    print('-----------------------------------------------------------')

e = Emp(age=20)
Display(e)

# -------------------------------------------------------------------------------
# fields validators :
# it is a decorator to validate a field value manually in a functions
# to know weather the the email coming from google or microsoft

from pydantic import BaseModel, EmailStr, field_validator

class Emp(BaseModel):
    name: str
    email: EmailStr

    @field_validator('email')
    @classmethod
    def validate_email(cls, value):
        valid_domains =['microsoft.com','google.com']
        # extract the domain name after @
        domain_name = value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError(' Invalid email address')
        return value

    @field_validator('name')
    @classmethod
    def transform(cls, value):
        value = value.upper()
        return value

def Display(e: Emp):
    print(e.name)
    print(e.email)
    print('------------------------------------------------------')

data = {'name':'vijay kumar','email':'vijaykumar@google.com'}
e = Emp(**data)

Display(e)

# -------------------------------------------------------------------------
# FILED VALIDATORS MODES / [ MODE = BEFORE OR AFTER ]
# CHECK IF THE AGE IN BETWEEN 20 AND 60

from pydantic import BaseModel, EmailStr, field_validator

class Emp(BaseModel):
    name: str
    age: int

    @field_validator('age', mode ='before')   # here we have to mention mode BEFORE / AFTER mode is by default there.
    @classmethod
    def validate_age(cls, value):
        if 20<=value<=60:
            return value
        else:
            raise ValueError(' Age must be b/w 20 and 60')

def display(e: Emp):
    print('name =', e.name)
    print('age =', e.age)

e = Emp(name ='ganesh', age= 23)
display(e)





























