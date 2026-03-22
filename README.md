# Used Car Price Prediction Web Application 🚗

## Project Overview

This project predicts the selling price of a used car using Machine Learning.
It takes user input such as year, present price, kilometers driven, fuel type, seller type, transmission, and owner details, then predicts the estimated resale price.

## Technologies Used

* Python
* FastAPI
* HTML
* CSS
* Scikit-learn
* Pandas
* NumPy

## Project Structure

* `main.py` → Backend application using FastAPI
* `train_model.py` → Model training script
* `model.pkl` → Trained machine learning model
* `templates/index.html` → Frontend HTML
* `static/style.css` → Styling file
* `car data.csv` → Dataset

## Features

* Predict used car resale price
* Interactive frontend UI
* FastAPI backend integration
* Machine learning model deployment

## Run Locally

```bash
pip install -r requirements.txt
python train_model.py
uvicorn main:app --reload
```

Then open:

```bash
http://127.0.0.1:8000
```

## Deployment

Project deployed using Render.

## GitHub Repository

Contains complete source code, model, frontend, backend, and documentation.

