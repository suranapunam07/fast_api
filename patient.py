from pydantic import BaseModel, AnyUrl, EmailStr, Field
from typing import List, Dict, Optional, Annotated


class Patient(BaseModel):
    name: Annotated[
        str,
        Field(
            max_length=50,
            title="Name of the Patient",
            description="Give the name of the patient in less than 50 characters",
            examples=["Punam", "Nidhi"]
        )
    ]

    email: EmailStr
    linkedin_url: AnyUrl

    age: int = Field(
        gt=0,
        lt=60,
        description="Age should be between 1 and 59"
    )

    weight: float = Field(
        gt=0,
        lt=120,
        description="Weight should be between 0 and 120 kg"
    )

    married: Annotated[
        bool,
        Field(description="Is the patient married?")
    ]

    allergies: Annotated[
        Optional[List[str]],
        Field(
            default=None,
            max_length=5,
            description="Maximum 5 allergies are allowed"
        )
    ]

    contact_details: Dict[str, str]


def insert_patient_data(patient: Patient):
    print("Name:", patient.name)
    print("Email:", patient.email)
    print("LinkedIn URL:", patient.linkedin_url)
    print("Age:", patient.age)
    print("Weight:", patient.weight)
    print("Married:", patient.married)
    print("Allergies:", patient.allergies)
    print("Contact Details:", patient.contact_details)
    print("Inserted Successfully!")


patient_info = {
    "name": "Purti",
    "email": "abc@gmail.com",
    "linkedin_url": "https://linkedin.com/in/purti",

    "age": 19,
    "weight": 45.66,
    "married": True,

    "allergies": [
        "pollen",
        "dust"
    ],

    "contact_details": {
        "email": "purti@gmail.com",
        "phone": "9881819810"
    }
}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)
