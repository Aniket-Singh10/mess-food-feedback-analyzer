import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle
import os
import sys

# Get directory where train_model.py is located
base_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(base_dir, '..', 'data', 'mess_data.csv')
model_path = os.path.join(base_dir, 'model.pkl')

print(f"Checking for dataset at: {csv_path}")

# Validation 1: Check if the CSV file exists
if not os.path.exists(csv_path):
    print(f"Error: Dataset file not found at {csv_path}", file=sys.stderr)
    sys.exit(1)

# Validation 2: Check if dataset file is empty
if os.path.getsize(csv_path) == 0:
    print(f"Error: Dataset file at {csv_path} is empty", file=sys.stderr)
    sys.exit(1)

# Validation 3: Parse CSV safely
try:
    data = pd.read_csv(csv_path)
except Exception as e:
    print(f"Error: Failed to parse CSV file: {e}", file=sys.stderr)
    sys.exit(1)

# Validation 4: Check for required columns
required_cols = ['food_quality', 'cleanliness', 'quantity', 'taste', 'rating']
missing_cols = [col for col in required_cols if col not in data.columns]
if missing_cols:
    print(f"Error: Missing required columns in dataset: {missing_cols}", file=sys.stderr)
    sys.exit(1)

# Validation 5: Clean and validate data rows
original_len = len(data)

# Drop missing values
data = data.dropna(subset=required_cols)

# Ensure numeric types
for col in required_cols:
    data[col] = pd.to_numeric(data[col], errors='coerce')

# Drop any row that became NaN after coercion
data = data.dropna(subset=required_cols)

# Filter for valid rating/score range (1 to 5)
invalid_rows = data[
    (data['food_quality'] < 1) | (data['food_quality'] > 5) |
    (data['cleanliness'] < 1) | (data['cleanliness'] > 5) |
    (data['quantity'] < 1) | (data['quantity'] > 5) |
    (data['taste'] < 1) | (data['taste'] > 5) |
    (data['rating'] < 1) | (data['rating'] > 5)
]

if not invalid_rows.empty:
    print(f"Warning: Found {len(invalid_rows)} row(s) with values outside the [1, 5] range. Dropping them.")
    data = data.drop(invalid_rows.index)

# Summary of cleaning
cleaned_len = len(data)
if cleaned_len < original_len:
    print(f"Data Cleaning: Kept {cleaned_len} of {original_len} rows after removing invalid/empty data.")

# Validation 6: Check if we have enough records left
if cleaned_len < 2:
    print("Error: Not enough valid data records to perform training (minimum 2 needed).", file=sys.stderr)
    sys.exit(1)

# Set features and target
X = data[['food_quality', 'cleanliness', 'quantity', 'taste']]
y = data['rating']

# Adjust test size dynamically for small datasets
test_size = 0.2 if cleaned_len >= 5 else (1.0 / cleaned_len)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)

print(f"Training on {len(X_train)} samples, testing on {len(X_test)} samples...")

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Accuracy
try:
    score = model.score(X_test, y_test)
    print(f"Model Accuracy (R^2 Score): {score:.4f}")
except Exception as e:
    print(f"Warning: Could not calculate accuracy score: {e}")

# Save model to the correct location
try:
    with open(model_path, 'wb') as f:
        pickle.dump(model, f)
    print(f"Model saved successfully to {model_path}!")
except Exception as e:
    print(f"Error: Failed to save model: {e}", file=sys.stderr)
    sys.exit(1)