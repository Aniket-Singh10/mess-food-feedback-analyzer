import pickle

import pandas as pd
import streamlit as st

MODEL_PATH = 'model/model.pkl'
DATA_PATH = 'data/mess_data.csv'

@st.cache_data(show_spinner=False)
def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)

@st.cache_resource(show_spinner=False)
def load_model(path: str):
    with open(path, 'rb') as model_file:
        return pickle.load(model_file)


def main() -> None:
    st.set_page_config(
        page_title='Mess Food Rating Predictor',
        page_icon='???',
        layout='centered',
    )

    st.title('Mess Food Feedback Rating Predictor')
    st.markdown(
        'Use the form below to enter mess feedback features and predict the expected mess rating. '
        'This app uses a trained `LinearRegression` model and can be deployed directly with Streamlit.'
    )

    try:
        model = load_model(MODEL_PATH)
    except FileNotFoundError:
        st.error(f'Model file not found at {MODEL_PATH}. Run `python model/train_model.py` first.')
        return

    data = load_data(DATA_PATH)

    with st.sidebar:
        st.header('Input Features')
        food_quality = st.slider('Food Quality', 1, 5, 3)
        cleanliness = st.slider('Cleanliness', 1, 5, 3)
        quantity = st.slider('Quantity', 1, 5, 3)
        taste = st.slider('Taste', 1, 5, 3)
        st.markdown('---')
        st.markdown('### About this app')
        st.markdown(
            '- Trained with `food_quality`, `cleanliness`, `quantity`, and `taste`\n'
            '- Predicts the `rating` of mess food feedback\n'
            '- Built for easy Streamlit deployment'
        )

    feature_values = [[food_quality, cleanliness, quantity, taste]]

    if st.button('Predict Rating'):
        prediction = model.predict(feature_values)
        predicted_rating = float(prediction[0])
        st.success(f'Predicted mess rating: {predicted_rating:.2f} / 5')

        st.write('### Input summary')
        st.write(
            {
                'food_quality': food_quality,
                'cleanliness': cleanliness,
                'quantity': quantity,
                'taste': taste,
            }
        )

    st.markdown('---')
    st.subheader('Training Data Snapshot')
    st.dataframe(data.head(10))

    st.subheader('Feature Distributions')
    st.bar_chart(data[['food_quality', 'cleanliness', 'quantity', 'taste']].mean())

    st.markdown('---')


if __name__ == '__main__':
    main()
