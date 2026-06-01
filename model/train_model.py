import pandas as pd
import os
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

# Load dataset using an absolute path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "..", "data", "mess_data.csv")

data = pd.read_csv(DATA_PATH)

# Dataset validation
print("Dataset Shape:", data.shape)
print("\nMissing Values:")
print(data.isnull().sum())

# Remove missing values if any
data = data.dropna()

# Features and target
X = data[['food_quality', 'cleanliness', 'quantity', 'taste']]
y = data['rating']

# Reproducible train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Evaluation metrics
print("\nModel Evaluation:")
print("R² Score:", r2_score(y_test, predictions))
print("MAE:", mean_absolute_error(y_test, predictions))
print("MSE:", mean_squared_error(y_test, predictions))

# Save model
MODEL_PATH = os.path.join(BASE_DIR, "model.pkl")
with open(MODEL_PATH, "wb") as f:
    pickle.dump(model, f)

print("\nModel saved successfully!")