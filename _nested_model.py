from pydantic import BaseModel

class address(BaseModel):
    city: str
    state: str
    pin: str

class Patient(BaseModel):
    name: str
    gender: str
    age: int
    address: address

address_dict = {'city':'Mumbai','state':'Maharashtra','pin':'400001'}

address1 = address(**address_dict)

patient_dict = {'name':'Purti','gender':'Female','age':18,'address':address1}

patient1 = Patient(**patient_dict)

#
print(patient1.address.city)