import streamlit as st

# Add page title and short description
st.title("Mess Food Feedback App")
st.write("Please provide your feedback on the mess food. Rate each category on a scale from 1 (Poor) to 5 (Excellent).")

# Create a form for the feedback to group inputs and the submit button
with st.form("feedback_form"):
    # Add input fields/sliders for the required categories (1 to 5)
    food_quality = st.slider("Food Quality", min_value=1, max_value=5, value=3, step=1)
    cleanliness = st.slider("Cleanliness", min_value=1, max_value=5, value=3, step=1)
    quantity = st.slider("Quantity", min_value=1, max_value=5, value=3, step=1)
    taste = st.slider("Taste", min_value=1, max_value=5, value=3, step=1)
    
    # Add a submit button
    submitted = st.form_submit_button("Submit Feedback")

    if submitted:
        st.success("Thank you! Your feedback has been recorded.")
        # Note: No prediction or database storage logic is required for this issue.