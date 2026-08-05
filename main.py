from fastapi import FastAPI,Path,Query,HTTPException
import json

app = FastAPI()

def load_data():
    with open("patients.json", "r") as f:
        data = json.load(f)
    return data

@app.get("/")
def hello():
    return {"message": "Patients Management System API"}

@app.get("/about")
def about():
    return {"message": "A fully functional API for managing patient records"}

@app.get("/view")
def view():
    return load_data()

@app.get("/patient/{patient_id}")
def view_patient(patient_id: str = Path(..., description="The ID of the patient",example='P001')):
    data = load_data()

    for patient in data:
        if patient["patient_id"] == patient_id:
            return patient

    raise HTTPException(status_code=404, detail='Patient not found')

@app.get('/sort')
def sort_patients(sort_by: str = Query(..., description='Sort on the basis of height,weight,bmi'), order: str = Query('asc', description='sort in ascending order')):
    valid_fields = ['height', 'weight', 'bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail='Invalid sort field')

    data = load_data()

    sort_order = False if order == 'asc' else True
    sorted_data = sorted(data, key=lambda x: x.get(sort_by, 0), reverse=sort_order)

    return sorted_data


    

