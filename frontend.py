import streamlit as st
import requests

st.set_page_config(
    page_title="Used Car Price Predictor",
    page_icon="🚗",
    layout="centered"
)

st.title("🚗 Used Car Price Prediction")
st.markdown("Enter car details to estimate resale price")

# Input fields
col1, col2 = st.columns(2)

with col1:
    year = st.number_input("Year of Purchase", min_value=2000, max_value=2024, value=2018)
    present_price = st.number_input("Present Price (Lakhs)", min_value=0.1, value=5.0)
    kms_driven = st.number_input("Kilometers Driven", min_value=0, value=20000)

with col2:
    fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG"])
    seller_type = st.selectbox("Seller Type", ["Dealer", "Individual"])
    transmission = st.selectbox("Transmission", ["Manual", "Automatic"])
    owner = st.selectbox("Previous Owners", [0, 1, 2, 3])

# Prediction button
if st.button("Predict Selling Price"):
    payload = {
        "year": year,
        "present_price": present_price,
        "kms_driven": kms_driven,
        "fuel_type": fuel_type,
        "seller_type": seller_type,
        "transmission": transmission,
        "owner": owner
    }

    try:
        # Replace with your actual backend URL
        url = "YOUR_REAL_BACKEND_URL/predict"

        response = requests.post(url, json=payload, timeout=60)

        if response.status_code == 200:
            result = response.json()

            if "predicted_price" in result:
                st.balloons()
                st.success(f"✅ Estimated Selling Price: ₹ {result['predicted_price']:.2f} Lakhs")
            else:
                st.error(f"⚠️ Backend Error: {result.get('error')}")

        else:
            st.error(f"❌ Server Error: {response.status_code}")

    except Exception as e:
        st.error(f"❌ Connection Failed: {e}")