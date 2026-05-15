import streamlit as st
import pandas as pd
import pickle
import os
import matplotlib.pyplot as plt
import seaborn as sns

# Set page config
st.set_page_config(
    page_title="Mess Food Feedback Analyzer",
    page_icon="🍲",
    layout="wide"
)

# Title and Description
st.title("🍲 Mess Food Feedback Analyzer")
st.markdown("""
Predict mess food ratings and analyze feedback data using Machine Learning.
""")

# Load Model
@st.cache_resource
def load_model():
    model_paths = ['model/model.pkl', 'model.pkl']
    for path in model_paths:
        if os.path.exists(path):
            with open(path, 'rb') as f:
                return pickle.load(f)
    return None

model = load_model()

if model is None:
    st.error("Model not found! Please run 'python model/train_model.py' first.")
else:
    # Sidebar for all inputs
    st.sidebar.header("Controls")
    
    # --- Manual Prediction Inputs ---
    st.sidebar.subheader("1. Manual Prediction")
    food_quality = st.sidebar.slider("Food Quality", 1, 5, 3)
    cleanliness = st.sidebar.slider("Cleanliness", 1, 5, 3)
    quantity = st.sidebar.slider("Quantity", 1, 5, 3)
    taste = st.sidebar.slider("Taste", 1, 5, 3)
    
    # --- Batch Analysis Input ---
    st.sidebar.markdown("---")
    st.sidebar.subheader("2. Batch Analysis")
    uploaded_file = st.sidebar.file_uploader("Upload CSV/Excel", type=['csv', 'xlsx'])

    # Main Area Layout
    col1, col2 = st.columns([1, 1])

    with col1:
        st.header("Manual Prediction Result")
        input_data = pd.DataFrame([[food_quality, cleanliness, quantity, taste]], 
                                 columns=['food_quality', 'cleanliness', 'quantity', 'taste'])
        prediction = model.predict(input_data)[0]
        
        st.metric("Predicted Rating", f"{prediction:.2f} / 5.0")
        if prediction >= 4:
            st.success("Excellent food quality!")
        elif prediction >= 3:
            st.info("Satisfactory quality.")
        else:
            st.warning("Needs improvement.")

    with col2:
        st.header("Feedback Trends")
        data_path = 'data/mess_data.csv'
        if os.path.exists(data_path):
            df_viz = pd.read_csv(data_path)
            avg_ratings = df_viz.mean()
            fig, ax = plt.subplots(figsize=(8, 5))
            avg_ratings.plot(kind='bar', color='#66B2FF', ax=ax)
            plt.xticks(rotation=30)
            st.pyplot(fig)
        else:
            st.write("No historical data found for trends.")

    st.markdown("---")

    # Batch Analysis Results (Full Width)
    if uploaded_file:
        st.header("Batch Analysis Results")
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
        
        required_cols = ['food_quality', 'cleanliness', 'quantity', 'taste']
        if all(col in df.columns for col in required_cols):
            df['predicted_rating'] = model.predict(df[required_cols])
            
            # Show Table
            st.write("### Predictions Table")
            st.dataframe(df, use_container_width=True)
            
            # Show Bar Chart for Uploaded Data
            st.write("### Uploaded Data Analysis")
            col_u1, col_u2 = st.columns(2)
            
            with col_u1:
                avg_uploaded = df[required_cols].mean()
                fig_u, ax_u = plt.subplots()
                avg_uploaded.plot(kind='bar', color='#99FF99', ax=ax_u)
                plt.title("Average Scores (Uploaded Data)")
                plt.xticks(rotation=30)
                st.pyplot(fig_u)
            
            with col_u2:
                st.write("#### Statistics Summary")
                st.write(df.describe())

            csv = df.to_csv(index=False)
            st.download_button("Download Predictions", csv, "predictions.csv", "text/csv")
        else:
            st.error(f"Missing columns: {', '.join(required_cols)}")
    
    st.header("Detailed Data Analysis")
    if os.path.exists('data/mess_data.csv'):
        df_corr = pd.read_csv('data/mess_data.csv')
        fig2, ax2 = plt.subplots(figsize=(10, 4))
        sns.heatmap(df_corr.corr(), annot=True, cmap='RdYlGn', ax=ax2)
        st.pyplot(fig2)
