import streamlit as st
import requests

st.title("🚗 Used Car Price Prediction")

# Inputs
year = st.number_input("Year", min_value=2000, max_value=2026)

km_driven = st.number_input("Kilometers Driven", min_value=0)

fuel_type = st.selectbox(
    "Fuel Type",
    ["Petrol", "Diesel", "CNG", "LPG", "Electric"]
)

seller_type = st.selectbox(
    "Seller Type",
    ["Dealer", "Individual", "Trustmark Dealer"]
)

transmission = st.selectbox(
    "Transmission",
    ["Manual", "Automatic"]
)

owner = st.selectbox(
    "Owner",
    [
        "First Owner",
        "Second Owner",
        "Third Owner",
        "Fourth & Above Owner",
        "Test Drive Car"
    ]
)

# Encoding maps
fuel_map = {
    "CNG": 0,
    "Diesel": 1,
    "Petrol": 2,
    "LPG": 3,
    "Electric": 4
}

seller_map = {
    "Dealer": 0,
    "Individual": 1,
    "Trustmark Dealer": 2
}

trans_map = {
    "Automatic": 0,
    "Manual": 1
}

owner_map = {
    "First Owner": 0,
    "Second Owner": 1,
    "Third Owner": 2,
    "Fourth & Above Owner": 3,
    "Test Drive Car": 4
}

# Prediction button
if st.button("Predict Price"):

    data = {
        "year": int(year),
        "km_driven": int(km_driven),
        "fuel_type": fuel_map[fuel_type],
        "seller_type": seller_map[seller_type],
        "transmission": trans_map[transmission],
        "owner": owner_map[owner]
    }

    response = requests.post(
    "http://127.0.0.1:8000/predict",
    json=data
)

st.write(response.text)

if response.status_code == 200:
    result = response.json()
    st.success(f"💰 Predicted Price: ₹ {result['predicted_price']} Lakhs")
else:
    st.error("Backend error")

        