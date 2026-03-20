# Used Car Price Prediction Web Application

## Project Overview

This project predicts the selling price of a used car using Machine Learning.

## Technologies Used

* Python
* FastAPI
* Streamlit
* Scikit-learn
* Pandas
* NumPy

## Project Files

* train_model.py
* main.py
* frontend.py
* model.pkl

## Run Locally

pip install -r requirements.txt

python train_model.py

uvicorn main:app --reload

streamlit run frontend.py
