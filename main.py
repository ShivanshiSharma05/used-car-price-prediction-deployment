from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd

app = FastAPI()

# 1. Load the model and its required features
with open("model.pkl", "rb") as f:
    model = pickle.load(f)
    model_features = list(model.feature_names_in_)

class CarInput(BaseModel):
    year: int
    present_price: float
    kms_driven: int
    fuel_type: str
    seller_type: str
    transmission: str
    owner: int

@app.post("/predict")
def predict(data: CarInput):
    # 2. Create the exact same dummy columns as pd.get_dummies
    # We manually skip 'CNG', 'Dealer', and 'Automatic' to mimic drop_first=True
    input_data = {
        'Year': data.year,
        'Present_Price': data.present_price,
        'Kms_Driven': data.kms_driven,
        'Owner': data.owner,
        # Only set to 1 if NOT the dropped category
        'Fuel_Type_Diesel': 1 if data.fuel_type == "Diesel" else 0,
        'Fuel_Type_Petrol': 1 if data.fuel_type == "Petrol" else 0,
        'Seller_Type_Individual': 1 if data.seller_type == "Individual" else 0,
        'Transmission_Manual': 1 if data.transmission == "Manual" else 0
    }
    
    # 3. Align with model's expected columns
    df = pd.DataFrame([input_data])
    df = df.reindex(columns=model_features, fill_value=0)

    # 4. Predict
    prediction = model.predict(df)
    return {"predicted_price": round(float(prediction[0]), 2)}

