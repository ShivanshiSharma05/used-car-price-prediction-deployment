import streamlit as st
import requests

st.set_page_config(page_title="CarPrice AI", layout="wide", page_icon="🚗")

# Custom CSS
st.markdown("""
<style>
.main {
    background-color: #0f172a;
    color: white;
}
.stButton>button {
    width: 100%;
    background-color: #2563eb;
    color: white;
    border-radius: 10px;
    height: 50px;
    font-size: 18px;
    font-weight: bold;
}
input, div[data-baseweb="select"] {
    border-radius: 10px !important;
}
.big-font {
    font-size: 50px !important;
    font-weight: 700;
    color: white;
}
.blue {
    color: #3b82f6;
}
</style>
""", unsafe_allow_html=True)

# Layout
left, right = st.columns([1, 1])

with left:
    st.markdown('<p class="big-font">Know your car\'s <span class="blue">true worth</span></p>', unsafe_allow_html=True)
    st.write("AI-powered used car resale prediction using deployed ML backend.")
    st.write("✔ Trained Model")
    st.write("✔ FastAPI Backend")
    st.write("✔ Render Deployment")

with right:
    st.subheader("Vehicle Details")

    year = st.number_input("Year", min_value=2000, max_value=2024, value=2019)
    present_price = st.number_input("Present Price (Lakhs)", min_value=0.1, value=5.0)
    kms_driven = st.number_input("KM Driven", min_value=0, value=20000)

    fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG"])
    seller_type = st.selectbox("Seller Type", ["Dealer", "Individual"])
    transmission = st.selectbox("Transmission", ["Manual", "Automatic"])
    owner = st.selectbox("Owner", [0, 1, 2, 3])

    if st.button("Predict Resale Price"):
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
            url = "https://used-car-backend.onrender.com/predict"
            response = requests.post(url, json=payload, timeout=60)

            if response.status_code == 200:
                result = response.json()
                st.success(f"Estimated Price: ₹ {result['predicted_price']:.2f} Lakhs")
            else:
                st.error("Prediction failed")

        except Exception as e:
            st.error(f"Connection Error: {e}")