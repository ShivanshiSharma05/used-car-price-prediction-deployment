from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd

app = FastAPI()

model = pickle.load(open("model.pkl", "rb"))

class CarInput(BaseModel):
    year: int
    km_driven: int
    fuel_type: int
    seller_type: int
    transmission: int
    owner: int

@app.get("/")
def home():
    return {"message": "Used Car Price Prediction API Running"}

@app.post("/predict")
def predict(data: CarInput):

    features = pd.DataFrame([{
        "year": data.year,
        "km_driven": data.km_driven,
        "fuel_type": data.fuel_type,
        "seller_type": data.seller_type,
        "transmission": data.transmission,
        "owner": data.owner
    }])

    prediction = model.predict(features)

    return {
        "predicted_price": round(float(prediction[0]), 2)
    }
