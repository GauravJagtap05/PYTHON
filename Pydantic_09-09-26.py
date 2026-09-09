from typing import Any, Self

# MODEL VALIDATOR

from pydantic import BaseModel, model_validator

class Emp(BaseModel):
    name : str
    age : int
    phone: str

    @classmethod
    @model_validator(mode='after')
    def validate_phone(self):
        # if age > 50 then providing phone no is compulsary
        if self.age>50 and self.phone == '':
            raise ValueError('phone number nust be given')
        else:
            return self


def display(e: Emp):
    print(e.name)
    print(e.age)
    print(e.phone)
    print('-----------------------------------------------------')

e = Emp(name='gopi', age=45, phone='')
display(e)

# ---------------------------------------------------

# COMPUTED FEILD

from pydantic import BaseModel, computed_field

class Emp(BaseModel):
    name : str
    sal: float

    @computed_field
    @property
    def pf(self)-> float:
        return self.sal * 12.5/100

    @computed_field
    @property

    def itax(self)->float:   # we have used this function itax as a field using @property given
        return self.sal * 0.1

def display(e: Emp):
    print(e.name)
    print(e.sal)
    print(e.itax)
    print(e.pf)
    print('--------------------------------------------------')


info = {'name':'vijay', 'sal':45000.50 }
e = Emp(**info)

display(e)

# ----------------------------------------------------------

# NESTED MODELS
# address is a model used inside Emp model # here address is a NESTED model

from pydantic import BaseModel
class Address(BaseModel):
    houseno: str
    city:str
    state:str

class Emp(BaseModel):    # subclass to base model class
    name: str
    sal: float
    addr: Address       # Address is the nested model inside the Emp model


def Display(e:Emp):
    print('Name', e.name)
    print('Salary', e.sal)
    print('Address : ')
    print(e.addr.houseno)
    print(e.addr.city)
    print(e.addr.state)
    print('-----------------------------------------------------------')


address_info = {'houseno':'24/B' , 'city':'Punewale', 'state':'Maharashtra'}
a = Address(**address_info)

Emp_info = {'name':'raj', 'sal': 65490, 'addr': a }  # here a is the object of Address class
e = Emp(**Emp_info)

#Display(e)
data = e.model_dump()     # EXPORT DATA THAT IS IN E and model_dump() -- gives data in the DICTIONARY format
print(data)
print('-------------------------------------------------------------')

data = e.model_dump(include={'name','sal'})  # here it will include the mentioned columns else everything it will exclude
print(data)
print('-------------------------------------------------------------')

data = e.model_dump(exclude={'name','sal'}) # here it will exclude the mentioned columns else everything it will include
print(data)
print('-------------------------------------------------------------')

data = e.model_dump(exclude={'addr':'city'})
print(data)
print('-------------------------------------------------------------')

data = e.model_dump_json(exclude={'addr':{'city'},
                                  'name':True})
print(data)
print('-------------------------------------------------------------')

data  = e.model_dump_json()  # EXPORT DATA THAT IS IN E and model_dump_json() -- gives data in the JSON format
print(data)

# EXPORTING DATA
# exporting data of nested model
















