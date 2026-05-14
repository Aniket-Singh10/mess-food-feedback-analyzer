import os
import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# --------------------------------------------------
# Load dataset
# --------------------------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

csv_path = os.path.join(BASE_DIR, '..', 'data', 'mess_data.csv')

data = pd.read_csv(csv_path)

print("\nDataset Preview:")
print(data.head())

# --------------------------------------------------
# Validate columns
# --------------------------------------------------

required_cols = ['food_quality', 'cleanliness', 'quantity', 'taste', 'rating']

for col in required_cols:
    if col not in data.columns:
        raise Exception(f"Missing column: {col}")

# --------------------------------------------------
# Features and target
# --------------------------------------------------

feature_cols = ['food_quality', 'cleanliness', 'quantity', 'taste']

X = data[feature_cols]
y = data['rating']

# --------------------------------------------------
# Train-test split
# --------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# --------------------------------------------------
# Train model
# --------------------------------------------------

print("\nTraining model...")

model = RandomForestRegressor(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

# --------------------------------------------------
# Evaluate model
# --------------------------------------------------

y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nModel Performance:")
print(f"Mean Absolute Error: {mae:.3f}")
print(f"R2 Score: {r2:.3f}")

# --------------------------------------------------
# Feature importance
# --------------------------------------------------

print("\nFeature Importance:")

for name, importance in zip(feature_cols, model.feature_importances_):
    print(f"{name}: {importance:.3f}")

# --------------------------------------------------
# Save model
# --------------------------------------------------

model_path = os.path.join(BASE_DIR, 'rating_model.pkl')

with open(model_path, 'wb') as f:
    pickle.dump(model, f)

print("\nModel saved at:", model_path)

# --------------------------------------------------
# Interactive prediction (FIXED - NO WARNING)
# --------------------------------------------------

print("\n--- Interactive Prediction ---")

while True:

    user_input = input(
        "\nEnter values (food_quality cleanliness quantity taste) or 'exit': "
    )

    if user_input.lower() == 'exit':
        break

    try:
        fq, cl, qt, ts = map(float, user_input.split())

        input_data = pd.DataFrame([{
            "food_quality": fq,
            "cleanliness": cl,
            "quantity": qt,
            "taste": ts
        }])

        prediction = model.predict(input_data)[0]

        print(f"Predicted Rating: {round(prediction, 2)}")

    except Exception:
        print("Invalid input. Please enter 4 numbers separated by spaces.")