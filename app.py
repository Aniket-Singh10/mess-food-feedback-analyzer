import streamlit as st
import joblib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# loading the trained model
model = joblib.load("model/model.pkl")
data = pd.read_csv("data/mess_data.csv")

# Page Configuration
st.set_page_config(layout="centered", page_title="Food Rating Prediction")

# Background color setting
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(120deg, #ff0000, #ffffff);
        color: black;
    }
    ./* Glass Container for input parameters*/
    [data-testid="stVerticalBlockBorderWrapper"] > div{
        background: rgba(255,255,255,0.1);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 20px;
        border: 1px solid rgba(255,255,255,0.2);

    }
    .stMarkdown, p, label {
        color: white !important;
    }
    h1{
        font-family: "Inter", sans-serif;
        font-weight: 800;
        text-align: center;
        color: #FFFFFF;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    /* Button Format */
    .stButton>button {
        background-color: #FF4B4B;
        color: black;
        border-radius: 10px;
        border: none;
        height: 3em;
        font-weight: bold;
    }

    /* Slider Format */
    div[data-baseweb="slider"]> div > div{
        background: red;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Mess Food Feedback Analyser")
st.markdown("<p style='text-align: center; color: #ddd;'>Adjust the parameters below to predict the overall satisfaction rating.</p>", unsafe_allow_html=True)
# inputs as slider inside the container
with st.container(border=True):

    food_quality = st.select_slider("Food Quality",options=range(1,11))
    cleanliness  = st.select_slider("Cleanliness",options=range(1,11))
    quantity = st.select_slider(" Quantity",options=range(1,11))
    taste = st.select_slider("taste",options=range(1,11))
    
    st.markdown("</div>", unsafe_allow_html=True)

# rating prediction
if st.button("Rating", use_container_width=True, type="primary"):
    input_data = pd.DataFrame([[
        food_quality, cleanliness, quantity, taste
    ]])
    prediction = model.predict(input_data)[0]
    
    st.divider()
    st.metric(label="Feedback Rating", value=f"{prediction:.2f}/10")

    # Insights section
    st.markdown("<h3 style='color:white; font-weight:bold;'>View Analytics Graph</h3>", unsafe_allow_html=True)

    # correlation analysis
    corr = data.corr()

    fig1, ax1 = plt.subplots(figsize = (7,5))
    sns.heatmap(corr, annot=True, cmap="Reds",linewidths=0.5,ax=ax1)
    ax1.set_title("Correlation Analysis")

    st.pyplot(fig1)

    # Mean Analysis
    mean = data.mean()
    fig2, ax2 = plt.subplots()
    mean.plot(kind='bar', ax=ax2, color="#FF4B4B")
    ax2.set_title("Average Mess Food Feedback Analysis")
    ax2.set_xlabel("Features")
    ax2.set_ylabel("Average Rating")
    ax2.grid(axis='y', linestyle='--', alpha=0.7)
    plt.xticks(rotation=30)
    plt.tight_layout()

    st.pyplot(fig2)

    