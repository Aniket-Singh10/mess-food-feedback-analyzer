import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt

from sklearn.model_selection import (
    train_test_split,
    cross_val_score
)

from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import (
    mean_squared_error,
    mean_absolute_error,
    r2_score
)

# ==========================================
# LOAD DATASET
# ==========================================

data = pd.read_csv('../data/mess_data.csv')

print("\nDataset Preview:\n")
print(data.head())

# ==========================================
# CHECK NULL VALUES
# ==========================================

print("\nMissing Values:\n")
print(data.isnull().sum())

# Fill missing values if any

data.fillna(data.mean(numeric_only=True), inplace=True)

# ==========================================
# FEATURE SELECTION
# ==========================================

X = data[['food_quality', 'cleanliness', 'quantity', 'taste']]
y = data['rating']

# ==========================================
# FEATURE SCALING
# ==========================================

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

# ==========================================
# TRAIN TEST SPLIT
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled,
    y,
    test_size=0.2,
    random_state=42
)

# ==========================================
# LINEAR REGRESSION MODEL
# ==========================================

lr_model = LinearRegression()

lr_model.fit(X_train, y_train)

lr_predictions = lr_model.predict(X_test)

# ==========================================
# RANDOM FOREST MODEL
# ==========================================

rf_model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

rf_model.fit(X_train, y_train)

rf_predictions = rf_model.predict(X_test)

# ==========================================
# MODEL EVALUATION FUNCTION
# ==========================================

def evaluate_model(name, y_test, predictions):

    mse = mean_squared_error(y_test, predictions)

    rmse = np.sqrt(mse)

    mae = mean_absolute_error(y_test, predictions)

    r2 = r2_score(y_test, predictions)

    print(f"\n{name} Performance")

    print("-" * 30)

    print(f"R2 Score       : {r2:.4f}")

    print(f"Mean Squared Error : {mse:.4f}")

    print(f"Root MSE       : {rmse:.4f}")

    print(f"Mean Absolute Error : {mae:.4f}")

# ==========================================
# EVALUATE MODELS
# ==========================================

evaluate_model(
    "Linear Regression",
    y_test,
    lr_predictions
)

evaluate_model(
    "Random Forest",
    y_test,
    rf_predictions
)

# ==========================================
# CROSS VALIDATION
# ==========================================

cv_scores = cross_val_score(
    rf_model,
    X_scaled,
    y,
    cv=5
)

print("\nCross Validation Scores:")
print(cv_scores)

print(f"\nAverage CV Score: {cv_scores.mean():.4f}")

# ==========================================
# FEATURE IMPORTANCE
# ==========================================

importance = rf_model.feature_importances_

features = X.columns

plt.figure(figsize=(8,5))

plt.bar(features, importance)

plt.title("Feature Importance")

plt.xlabel("Features")
plt.ylabel("Importance Score")

plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()

plt.show()

# ==========================================
# ACTUAL VS PREDICTED GRAPH
# ==========================================

plt.figure(figsize=(8,5))

plt.plot(
    y_test.values,
    label='Actual Ratings',
    marker='o'
)

plt.plot(
    rf_predictions,
    label='Predicted Ratings',
    marker='x'
)

plt.title("Actual vs Predicted Ratings")

plt.xlabel("Samples")
plt.ylabel("Ratings")

plt.legend()

plt.grid(True)

plt.tight_layout()

plt.show()

# ==========================================
# SAVE BEST MODEL
# ==========================================

pickle.dump(
    rf_model,
    open('model.pkl', 'wb')
)

pickle.dump(
    scaler,
    open('scaler.pkl', 'wb')
)

print("\nModel and scaler saved successfully!")

# ==========================================
# SAMPLE PREDICTION
# ==========================================

sample = [[8, 9, 7, 8]]

sample_scaled = scaler.transform(sample)

prediction = rf_model.predict(sample_scaled)

print("\nSample Prediction:")
print(f"Predicted Rating: {prediction[0]:.2f}")

print("\nTraining Completed Successfully!")