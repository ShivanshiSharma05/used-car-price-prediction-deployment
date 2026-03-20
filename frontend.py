import streamlit as st
import requests

st.set_page_config(page_title="CarPriceAI", layout="wide")

st.markdown("""
<style>
.main {
    background-color: #f5f7fb;
}
.title {
    font-size: 52px;
    font-weight: 800;
    color: white;
}
.left-box {
    background-color: #071a3d;
    padding: 60px;
    border-radius: 20px;
    height: 650px;
}
.right-box {
    background-color: white;
    padding: 40px;
    border-radius: 20px;
    box-shadow: 0px 6px 18px rgba(0,0,0,0.08);
}
.stButton>button {
    width: 100%;
    background-color: #2563eb;
    color: white;
    font-size: 20px;
    border-radius: 12px;
    height: 55px;
}
</style>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1,1])

with col1:
    st.markdown("""
    <div class="left-box">
        <div class="title">Know your car's <span style='color:#3b82f6'>true worth</span></div>
        <br><br>
        <h3 style='color:white;'>AI-based resale prediction for Indian cars</h3>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown('<div class="right-box">', unsafe_allow_html=True)

    car_name = st.text_input("Car Name", "Maruti Swift VXI")

    col3, col4 = st.columns(2)

    with col3:
        year = st.number_input("Year", 2000, 2024, 2019)
        kms_driven = st.number_input("KM Driven", 0, 500000, 4500)
        transmission = st.selectbox("Transmission", ["Manual", "Automatic"])
        owner = st.selectbox("Owner", [0,1,2,3])

    with col4:
        present_price = st.number_input("Present Price (Lakhs)", 0.1, 50.0, 5.0)
        fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG"])
        seller_type = st.selectbox("Seller Type", ["Dealer", "Individual"])

    if st.button("Predict Resale Price →"):

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
            response = requests.post(
                "https://used-car-backend.onrender.com/predict",
                json=payload,
                timeout=60
            )

            if response.status_code == 200:
                result = response.json()
                st.success(f"Estimated Price: ₹ {result['predicted_price']} Lakhs")
                st.balloons()
            else:
                st.error(response.text)

        except Exception as e:
            st.error(f"Connection failed: {e}")

    st.markdown('</div>', unsafe_allow_html=True)