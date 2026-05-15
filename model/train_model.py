import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import (
    r2_score,
    mean_absolute_error,
    mean_squared_error
)

# Load dataset
data = pd.read_csv("data/mess_data.csv")

# Features and target
X = data[['food_quality', 'cleanliness', 'quantity', 'taste']]
y = data['rating']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# Models dictionary
models = {
    "Linear Regression": LinearRegression(),
    "Decision Tree": DecisionTreeRegressor(random_state=42),
    "Random Forest": RandomForestRegressor(random_state=42)
}

results = {}

best_model = None
best_score = -1

print("\n===== MODEL COMPARISON RESULTS =====")

# Train and evaluate each model
for name, model in models.items():

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    r2 = r2_score(y_test, predictions)
    mae = mean_absolute_error(y_test, predictions)
    rmse = np.sqrt(mean_squared_error(y_test, predictions))

    results[name] = r2

    print(f"\n{name}")
    print(f"R2 Score : {r2:.2f}")
    print(f"MAE      : {mae:.2f}")
    print(f"RMSE     : {rmse:.2f}")

    # Save best model
    if r2 > best_score:
        best_score = r2
        best_model = model

# Save best model
joblib.dump(best_model, "model/model.pkl")

print("\nBest model saved successfully!")

# Visualization
plt.figure(figsize=(8, 5))
plt.bar(results.keys(), results.values())

plt.xlabel("Models")
plt.ylabel("R2 Score")
plt.title("Machine Learning Model Comparison")

plt.show()