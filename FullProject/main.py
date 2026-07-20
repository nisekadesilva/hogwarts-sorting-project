from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = joblib.load('hogwarts_rf_model.pkl')
encoder = joblib.load('target_encoder.pkl')

class StudentInput(BaseModel):
    bravery: int
    intelligence: int
    loyalty: int
    ambition: int
    creativity: int

@app.post("/predict")
def predict_house(data: StudentInput):
    # Use Pandas DataFrame so feature names match training
    features = pd.DataFrame([{
        'bravery': data.bravery,
        'intelligence': data.intelligence,
        'loyalty': data.loyalty,
        'ambition': data.ambition,
        'creativity': data.creativity
    }])
    
    prediction_id = model.predict(features)[0]
    house_name = encoder.classes_[prediction_id]
    
    return {"house": house_name}