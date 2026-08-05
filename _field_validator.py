from pydantic import BaseModel, EmailStr, computed_field, field_validator, model_validator
from typing import List, Dict

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    height : float
    married: bool
    allergies: List[str] 
    contact_details: Dict[str, str]

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domains = ['hdfc.com', 'icici.com']
        domain_name = value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError('Not a valid email domain')
        return value

    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()

    @model_validator(mode='after')
    def value_emergengy_contact(cls,model):
        if model.age > 60 and 'emrgency_contact' not in model.contact_details:
            raise ValueError('Emergency concact is required for patients above 60 years of age')
        return model

    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight / (self.height ** 2), 2)


def insert_patient_data(patient: Patient):
    print("Name:", patient.name)
    print("Email:", patient.email)
    print("Age:", patient.age)
    print("Weight:", patient.weight)
    print("Height:",patient.height)
    print("Married:", patient.married)
    print("BMI:",patient.bmi)
    print("Allergies:", patient.allergies)
    print("Contact Details:", patient.contact_details)
    print("Inserted Successfully!")

patient_info = {'name':'Purti','email':'abc@hdfc.com','age':18,'weight':47.5,'height':1.598,'married':False,'allergies':['dust','pollen'],'contact_details' : {'phone': '123-456-7890', 'address': '123 Main St, City, Country', 'emrgency_contact': '987-654-3210'}}

patient = Patient(**patient_info)

insert_patient_data(patient)
