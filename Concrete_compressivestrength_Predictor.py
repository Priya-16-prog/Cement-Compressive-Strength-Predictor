import streamlit as st
import pandas as pd
import numpy as np
import joblib

# -----------------------------
# Load saved model and scaler
# -----------------------------

model = joblib.load(r"C:\Users\priya\OneDrive\Documents\concrete_model.pkl")
scaler = joblib.load(r"C:\Users\priya\OneDrive\Documents\scaler.pkl")

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="Concrete Strength Predictor", layout="centered")

# Title
st.title("🏗️ Concrete Compressive Strength Prediction")
st.write("Enter the mix proportions to predict concrete strength (MPa).")

# User Inputs
cement = st.number_input("Cement (kg/m³)", 100.0, 600.0, 300.0)
slag = st.number_input("Blast Furnace Slag (kg/m³)", 0.0, 300.0, 50.0)
flyash = st.number_input("Fly Ash (kg/m³)", 0.0, 300.0, 100.0)
water = st.number_input("Water (kg/m³)", 100.0, 250.0, 180.0)
superplasticizer = st.number_input("Superplasticizer (kg/m³)", 0.0, 30.0, 5.0)
coarse_agg = st.number_input("Coarse Aggregate (kg/m³)", 800.0, 1200.0, 950.0)
fine_agg = st.number_input("Fine Aggregate (kg/m³)", 600.0, 1000.0, 800.0)
age = st.number_input("Age (days)", 1, 365, 28)

# Prepare input for model
input_data = np.array([[cement, slag, flyash, water, superplasticizer,
                        coarse_agg, fine_agg, age]])

# Scale numerical inputs
input_scaled = scaler.transform(input_data)

# Prediction
if st.button("Predict Strength"):
    strength = model.predict(input_scaled)[0]
    st.success(f"✅ Predicted Concrete Strength: {strength:.2f} MPa")
