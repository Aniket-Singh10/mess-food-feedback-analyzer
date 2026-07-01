import pickle
from pathlib import Path

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Resolve dataset location relative to this script
script_dir = Path(__file__).resolve().parent
data_path = script_dir.parent / 'data' / 'mess_data.csv'

if not data_path.exists():
    raise FileNotFoundError(f"Dataset not found: {data_path}")

# Load dataset
data = pd.read_csv(data_path)

X = data[['food_quality', 'cleanliness', 'quantity', 'taste']]
y = data['rating']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Accuracy
score = model.score(X_test, y_test)
print(f"Model Accuracy: {score}")

# Save model
model_file = script_dir / 'model.pkl'
with open(model_file, 'wb') as f:
    pickle.dump(model, f)

print(f"Model saved successfully at {model_file}")