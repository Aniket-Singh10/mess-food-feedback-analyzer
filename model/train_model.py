import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

# Resolve paths relative to this script's location, not the working directory.
# This ensures `python model/train_model.py` works from the project root.
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(SCRIPT_DIR, '..', 'data', 'mess_data.csv')
MODEL_PATH = os.path.join(SCRIPT_DIR, 'model.pkl')

# Load dataset
data = pd.read_csv(DATA_PATH)

X = data[['food_quality', 'cleanliness', 'quantity', 'taste']]
y = data['rating']

# Split data (random_state ensures reproducible results across runs)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Accuracy
score = model.score(X_test, y_test)
print(f"Model R² Score: {score:.4f}")

# Save model (use 'with' to ensure file handle is properly closed)
with open(MODEL_PATH, 'wb') as f:
    pickle.dump(model, f)
print(f"Model saved to {MODEL_PATH}")