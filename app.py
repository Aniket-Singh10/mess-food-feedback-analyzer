import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

# Page config
st.set_page_config(
    page_title="Mess Food Feedback Analyzer",
    page_icon="🍽️",
    layout="centered"
)

# Load model safely
try:
    model = joblib.load("model/model.pkl")
except FileNotFoundError:
    st.error("Model file not found. Please run model/train_model.py first.")
    st.stop()

# Load dataset
data = pd.read_csv("data/mess_data.csv")

# Sidebar
st.sidebar.title("About")
st.sidebar.info(
    "This app predicts overall mess food ratings using a Linear Regression model."
)

# Main title
st.title("🍽️ Mess Food Feedback Analyzer")
st.write("Predict overall mess food ratings based on student feedback.")

# Input section
st.header("Submit Food Ratings")

food_quality = st.slider("Food Quality", 1, 5, 3)
cleanliness = st.slider("Cleanliness", 1, 5, 3)
quantity = st.slider("Quantity", 1, 5, 3)
taste = st.slider("Taste", 1, 5, 3)

# Prediction
if st.button("Predict Rating"):

    input_data = [[food_quality, cleanliness, quantity, taste]]

    prediction = model.predict(input_data)[0]

    st.success(f"Predicted Overall Rating: {prediction:.2f} / 5")

# Visualization
st.header("Average Feedback Analysis")

avg_scores = data.mean()

fig, ax = plt.subplots(figsize=(8, 5))

ax.bar(avg_scores.index, avg_scores.values)

ax.set_title("Average Feature Ratings")
ax.set_ylabel("Average Score")
ax.set_xlabel("Features")

plt.xticks(rotation=15)

st.pyplot(fig)

# Dataset preview
st.header("Dataset Preview")
st.dataframe(data.head())