## Problem Statement
Mess food quality varies daily, and students often face inconsistency in food quality, cleanliness, and taste.

## Objective
To analyze and predict mess food ratings using machine learning based on different factors.

## Input Features
- Food Quality
- Cleanliness
- Quantity
- Taste

## Application Features
- Predict mess food ratings using Machine Learning
- Interactive Streamlit dashboard
- Dynamic feedback analytics
- Smart improvement suggestions
- Real-time graph updates
- Persistent feedback storage

## Technologies Used
- Python
- Streamlit
- Pandas
- Matplotlib
- Scikit-learn
- NumPy

## Model Used
Linear Regression

## How to Run
1. Install dependencies:
   pip install pandas scikit-learn matplotlib numpy streamlit

2. Run training:
   python model/train_model.py

3. Run analysis:
   python analysis.py

4. Run Streamlit App:
   streamlit run app.py

## Output
- Predicts overall mess food rating
- Displays mess status analysis
- Provides improvement suggestions
- Visualizes feedback analytics dynamically

## Project Structure

```text
mess-food-feedback-analyzer/
│
├── app.py
├── analysis.py
├── data/
│   └── mess_data.csv
├── model/
│   ├── model.pkl
│   └── train_model.py
└── README.md
```