import streamlit as st

st.set_page_config(page_title="Mess Food Feedback Analyzer")

st.title("🍽️ Mess Food Feedback Analyzer")

st.write("Analyze and predict mess food ratings using ML.")

feedback_available = False

if feedback_available:
    st.success("Feedback data loaded successfully!")
else:
    st.info("📭 No feedback data available yet.")

    st.markdown("""
    ### What you can do:
    - Add new food feedback
    - Upload dataset
    - Run prediction analysis
    """)

    st.button("Add Feedback")