import streamlit as st
import pandas as pd
import pickle
import numpy as np
from pathlib import Path

# Load Model
MODEL_PATH = Path(__file__).resolve().parent / "model" / "model.pkl"

st.set_page_config(page_title="Mess Feedback Analyzer", page_icon="🍲")

st.title("🍲 Mess Food Rating Predictor")
st.write("Enter the parameters below to predict the overall student satisfaction.")

# User Inputs
food_q = st.slider("Food Quality", 1, 5, 3)
clean = st.slider("Cleanliness", 1, 5, 3)
quant = st.slider("Quantity", 1, 5, 3)
taste = st.slider("Taste", 1, 5, 3)

if st.button("Predict Rating"):
    if MODEL_PATH.exists():
        with open(MODEL_PATH, 'rb') as f:
            model = pickle.load(f)
        
        input_data = np.array([[food_q, clean, quant, taste]])
        prediction = model.predict(input_data)[0]
        
        st.success(f"Predicted Overall Rating: **{prediction:.2f} / 5.0**")
        
        # Simple Logic for Management
        if prediction < 2.5:
            st.warning("Action Required: Low satisfaction predicted.")
        else:
            st.info("Status: Satisfaction is within acceptable levels.")
    else:
        st.error("Model file not found. Please run train_model.py first.")