import streamlit as st
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.sidebar.title("About")

st.sidebar.info(
    """
    This project predicts mess food ratings
    using Machine Learning based on:
    - Food Quality
    - Cleanliness
    - Quantity
    - Taste
    """
)

# Load trained model
model = pickle.load(open('model/model.pkl', 'rb'))

st.title("Mess Food Feedback Analyzer")

st.write("Enter mess food parameters to predict overall rating.")

food_quality = st.slider("Food Quality", 1, 10, 5)
cleanliness = st.slider("Cleanliness", 1, 10, 5)
quantity = st.slider("Quantity", 1, 10, 5)
taste = st.slider("Taste", 1, 10, 5)

if st.button("Predict Rating"):

    features = np.array([[food_quality, cleanliness, quantity, taste]])
    prediction = model.predict(features)

    st.success(f"Predicted Overall Rating: {prediction[0]:.2f}")

    if prediction[0] >= 8:
        st.success("Excellent Mess Food 🍽️")
        st.success("Mess Status: Excellent 🍽️")

    elif prediction[0] >= 6:
        st.info("Average Mess Food 🙂")
        st.warning("Mess Status: Needs Minor Improvements 🙂")

    else:
        st.error("Poor Mess Food 😕")
        st.error("Mess Status: Immediate Attention Needed 😕")

    st.subheader("Suggestions for Improvement")

    suggestions = []

    if food_quality < 5:
        suggestions.append("Improve food quality and freshness.")

    if cleanliness < 5:
        suggestions.append("Maintain better hygiene and cleanliness.")

    if quantity < 5:
        suggestions.append("Increase food serving quantity.")

    if taste < 5:
        suggestions.append("Enhance taste and seasoning.")

    if suggestions:
        for s in suggestions:
            st.write("•", s)

    else:
        st.success("Great! Your mess performance looks excellent.")
        
    new_feedback = pd.DataFrame({
        "food_quality": [food_quality],
        "cleanliness": [cleanliness],
        "quantity": [quantity],
        "taste": [taste],
        "rating": [prediction[0]]
    })
    
    data = pd.read_csv("data/mess_data.csv")
    updated_data = pd.concat([data, new_feedback], ignore_index=True)
    updated_data.to_csv("data/mess_data.csv", index=False)

st.markdown("---")

st.subheader("Average Feedback Analysis")

updated_data = pd.read_csv("data/mess_data.csv")
st.write("Total Feedback Entries:", len(updated_data))
avg = updated_data.mean()

fig, ax = plt.subplots(figsize=(8,5))
avg.plot(kind='bar', ax=ax)

plt.title("Average Mess Food Feedback")
plt.xlabel("Features")
plt.ylabel("Average Rating")
plt.xticks(rotation=30)

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
st.pyplot(fig)