# Mess Food Feedback Analyzer

A machine learning-based application that analyzes mess food feedback and predicts the overall food rating based on food quality, cleanliness, quantity, and taste.

## Problem Statement

Mess food quality can vary from day to day. Students may experience differences in food quality, cleanliness, quantity, and taste. This project uses machine learning to analyze these factors and predict an overall mess food rating.

## Objective

The main objectives of this project are:

- Analyze student feedback about mess food.
- Identify the relationship between different feedback factors and the overall rating.
- Predict the overall mess food rating using machine learning.
- Provide a backend API for making predictions.

## Features

The model uses the following features:

- Food Quality
- Cleanliness
- Quantity
- Taste

The target variable is:

- Rating

## Machine Learning Model

The project uses Linear Regression to predict the overall mess food rating.

The trained model is saved using Python's `pickle` module and loaded by the Flask backend for making predictions.

## Project Structure

mess-food-feedback-analyzer/
│
├── data/
│   └── mess_data.csv
│
├── model/
│   ├── model.pkl
│   └── train_model.py
│
├── app.py
├── analysis.py
├── Project_Report.pdf
└── README.md

## Installation

Clone the repository:

git clone https://github.com/Aniket-Singh10/mess-food-feedback-analyzer.git
cd mess-food-feedback-analyzer

Install the required dependencies:

pip install pandas scikit-learn matplotlib flask

## Train the Model

To train the machine learning model, run:

python model/train_model.py

The trained model is used by the Flask backend for making predictions.

## Run Data Analysis

To generate the feedback analysis graph, run:

python analysis.py

The script calculates the average values of the feedback features and displays them using a bar chart.

## Run the Backend API

Start the Flask application:

python app.py

The API will run at:

http://127.0.0.1:5000

## API Endpoints

### Health Check

GET /api/health

This endpoint checks whether the API is running.

Example response:

{
    "status": "ok"
}

### Predict Mess Food Rating

POST /api/predict

The endpoint accepts the following JSON data:

{
    "food_quality": 4,
    "cleanliness": 4,
    "quantity": 3,
    "taste": 5
}

The API uses these values as input to the trained Linear Regression model.

Example response:

{
    "success": true,
    "prediction": 4.12
}

The prediction value may vary depending on the trained model.

## Request Validation and Error Handling

The API validates incoming requests before making predictions.

It handles:

- Missing required fields
- Non-numeric input values
- Invalid request data
- Model loading failures
- Prediction-time errors

Errors are returned as JSON responses with appropriate HTTP status codes.

## Output

The project provides:

- Average feedback analysis through data visualization
- Machine learning-based mess food rating prediction
- REST API for sending feedback data and receiving predictions
- Health-check endpoint for verifying API availability

## Technologies Used

- Python
- Pandas
- Scikit-learn
- Matplotlib
- Flask
- Pickle

## Model Input

| Feature | Description |
|---|---|
| food_quality | Rating for the quality of food |
| cleanliness | Rating for mess cleanliness |
| quantity | Rating for food quantity |
| taste | Rating for food taste |

## Target

rating

The model predicts the overall mess food rating based on the four input features.