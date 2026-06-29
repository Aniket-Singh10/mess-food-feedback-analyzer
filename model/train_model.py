import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

from xgboost import XGBRegressor

# -----------------------------
# Load Dataset
# -----------------------------
data = pd.read_csv('../data/mess_data.csv')

# Features and Target
X = data[['food_quality', 'cleanliness', 'quantity', 'taste']]
y = data['rating']

# -----------------------------
# Correlation Heatmap
# -----------------------------
plt.figure(figsize=(8,6))
sns.heatmap(
    data.corr(numeric_only=True),
    annot=True,
    cmap="coolwarm",
    linewidths=0.5
)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

# -----------------------------
# Train-Test Split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# -----------------------------
# Models
# -----------------------------
models = {
    "Linear Regression": LinearRegression(),
    "Decision Tree": DecisionTreeRegressor(random_state=42),
    "Random Forest": RandomForestRegressor(
        n_estimators=100,
        random_state=42
    ),
    "SVR": SVR(),
    "XGBoost": XGBRegressor(
        objective="reg:squarederror",
        n_estimators=100,
        learning_rate=0.1,
        max_depth=4,
        random_state=42
    )
}

best_model = None
best_score = -999
best_name = ""
best_prediction = None

results = []

# -----------------------------
# Train & Evaluate
# -----------------------------
for name, model in models.items():

    model.fit(X_train, y_train)

    prediction = model.predict(X_test)

    mae = mean_absolute_error(y_test, prediction)
    mse = mean_squared_error(y_test, prediction)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, prediction)

    results.append({
        "Model": name,
        "MAE": mae,
        "MSE": mse,
        "RMSE": rmse,
        "R2 Score": r2
    })

    print("\n" + "="*60)
    print(name)
    print("="*60)
    print(f"MAE      : {mae:.4f}")
    print(f"MSE      : {mse:.4f}")
    print(f"RMSE     : {rmse:.4f}")
    print(f"R² Score : {r2:.4f}")

    if r2 > best_score:
        best_score = r2
        best_model = model
        best_name = name
        best_prediction = prediction

# -----------------------------
# Comparison Table
# -----------------------------
results_df = pd.DataFrame(results)

print("\n\nModel Comparison")
print(results_df.sort_values(by="R2 Score", ascending=False))

# -----------------------------
# Bar Chart of R² Scores
# -----------------------------
plt.figure(figsize=(8,5))
plt.bar(results_df["Model"], results_df["R2 Score"])
plt.title("Model Comparison (R² Score)")
plt.xlabel("Models")
plt.ylabel("R² Score")
plt.xticks(rotation=15)
plt.tight_layout()
plt.show()

# -----------------------------
# Actual vs Predicted
# -----------------------------
plt.figure(figsize=(7,6))

plt.scatter(y_test, best_prediction, alpha=0.7)

plt.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()],
    color="red",
    linewidth=2
)

plt.xlabel("Actual Ratings")
plt.ylabel("Predicted Ratings")
plt.title(f"Actual vs Predicted ({best_name})")

plt.tight_layout()
plt.show()

# -----------------------------
# Save Best Model
# -----------------------------
with open("model.pkl", "wb") as file:
    pickle.dump(best_model, file)

print(f"\nBest Model : {best_name}")
print(f"Best R² Score : {best_score:.4f}")
print("Best model saved successfully as model.pkl")