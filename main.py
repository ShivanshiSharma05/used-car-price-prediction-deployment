from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import pickle
import pandas as pd

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

with open("model.pkl", "rb") as f:
    model = pickle.load(f)
    model_features = list(model.feature_names_in_)

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict")
def predict(
    request: Request,
    year: int = Form(...),
    present_price: float = Form(...),
    kms_driven: int = Form(...),
    fuel_type: str = Form(...),
    seller_type: str = Form(...),
    transmission: str = Form(...),
    owner: int = Form(...)
):
    input_data = {
        'Year': year,
        'Present_Price': present_price,
        'Kms_Driven': kms_driven,
        'Owner': owner,
        'Fuel_Type_Diesel': 1 if fuel_type == "Diesel" else 0,
        'Fuel_Type_Petrol': 1 if fuel_type == "Petrol" else 0,
        'Seller_Type_Individual': 1 if seller_type == "Individual" else 0,
        'Transmission_Manual': 1 if transmission == "Manual" else 0
    }

    df = pd.DataFrame([input_data])
    df = df.reindex(columns=model_features, fill_value=0)

    prediction = model.predict(df)[0]

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "prediction": round(float(prediction), 2)
        }
    )