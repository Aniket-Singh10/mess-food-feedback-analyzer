import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
import pickle

# Load dataset
DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'mess_data.csv')
data = pd.read_csv(DATA_PATH)

X = data[['food_quality', 'cleanliness', 'quantity', 'taste']]
y = data['rating']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# R^2 score on held-out test set
score = model.score(X_test, y_test)
print(f"Model R^2 Score: {score}")

# Cross-validation gives a more robust estimate on this small dataset
cv_scores = cross_val_score(LinearRegression(), X, y, cv=5)
print(f"Cross-validated R^2 scores: {cv_scores}")
print(f"Mean CV R^2 Score: {cv_scores.mean()}")

# Save model
MODEL_OUT_PATH = os.path.join(os.path.dirname(__file__), 'model.pkl')
pickle.dump(model, open(MODEL_OUT_PATH, 'wb'))
print("Model saved successfully!")
