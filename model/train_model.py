import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

# Load dataset

import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(BASE_DIR, 'data', 'mess_data.csv')

data = pd.read_csv(file_path)

X = data[['food_quality', 'cleanliness', 'quantity', 'taste']]
y = data['rating']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2 ,random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Accuracy
score = model.score(X_test, y_test)
print(f"Model Accuracy: {score}")

# Save model
model_path = os.path.join(BASE_DIR, 'model', 'model.pkl')

with open(model_path, 'wb') as f:
    pickle.dump(model, f)
print("Model saved successfully!")