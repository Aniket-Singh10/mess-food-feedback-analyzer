import streamlit as st

st.set_page_config(
    page_title="Mess Food Feedback App",
    page_icon="🍽️",
    layout="centered"
)
# Title and description
st.title("🍽️ Mess Food Feedback App")
st.markdown(
    "Rate your mess food experience based on the following categories."
)

st.divider()

# sliders
food_quality = st.slider(
    "Food Quality",
    min_value=1,
    max_value=5,
    value=3
)

cleanliness = st.slider(
    "Cleanliness",
    min_value=1,
    max_value=5,
    value=3
)

quantity = st.slider(
    "Quantity",
    min_value=1,
    max_value=5,
    value=3
)

taste = st.slider(
    "Taste",
    min_value=1,
    max_value=5,
    value=3
)

st.divider()

# Submit button
if st.button("Submit Feedback"):
    st.success("✅ Feedback submitted successfully!")

    st.write("### Your Ratings")
    st.write(f"🍛 Food Quality: {food_quality}/5")
    st.write(f"🧼 Cleanliness: {cleanliness}/5")
    st.write(f"🍽️ Quantity: {quantity}/5")
    st.write(f"😋 Taste: {taste}/5")
