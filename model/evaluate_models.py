"""
evaluate_models.py
------------------
Resolves Issue #190 - Evaluate Multiple Models for Better Accuracy

Compares 7 regression models to find the best one for predicting
mess food ratings based on food_quality, cleanliness, quantity, taste.

Models compared:
    1. Linear Regression
    2. Ridge Regression
    3. Decision Tree Regressor
    4. Random Forest Regressor
    5. Gradient Boosting Regressor
    6. Support Vector Regressor (SVR)
    7. K-Nearest Neighbours Regressor

Metrics:
    - MAE  (Mean Absolute Error)
    - RMSE (Root Mean Squared Error)
    - R2   (Coefficient of Determination)
    - CV R2 (5-fold Cross-Validation R2)

Output:
    - Console table comparing all models
    - model/model_comparison.png  (bar chart)
    - model/best_model.pkl        (best model auto-saved)
"""

import os
import pickle
import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

from sklearn.linear_model import LinearRegression, Ridge
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor

warnings.filterwarnings("ignore")

# ---------- Load Data ----------
BASE_DIR  = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "..", "data", "mess_data.csv")

data = pd.read_csv(DATA_PATH)

X = data[['food_quality', 'cleanliness', 'quantity', 'taste']]
y = data['rating']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("\n" + "=" * 58)
print("  Mess Food Feedback - Multi-Model Evaluation")
print("  Resolves Issue #190")
print("=" * 58)
print(f"  Samples: {len(data)}  |  Train: {len(X_train)}  |  Test: {len(X_test)}")
print("=" * 58 + "\n")

# ---------- Define Models ----------
models = {
    "Linear Regression":    LinearRegression(),
    "Ridge Regression":     Ridge(alpha=1.0),
    "Decision Tree":        DecisionTreeRegressor(max_depth=6, random_state=42),
    "Random Forest":        RandomForestRegressor(n_estimators=100, random_state=42),
    "Gradient Boosting":    GradientBoostingRegressor(n_estimators=100, random_state=42),
    "SVR":                  Pipeline([("scaler", StandardScaler()), ("svr", SVR(kernel="rbf"))]),
    "K-Nearest Neighbours": KNeighborsRegressor(n_neighbors=5),
}

# ---------- Train & Evaluate ----------
results = []

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred    = model.predict(X_test)
    mae       = mean_absolute_error(y_test, y_pred)
    rmse      = np.sqrt(mean_squared_error(y_test, y_pred))
    r2        = r2_score(y_test, y_pred)
    cv_mean   = cross_val_score(model, X, y, cv=5, scoring="r2").mean()
    results.append({
        "Model":  name,
        "MAE":    round(mae, 4),
        "RMSE":   round(rmse, 4),
        "R2":     round(r2, 4),
        "CV_R2":  round(cv_mean, 4),
    })

results_df = pd.DataFrame(results).sort_values("R2", ascending=False).reset_index(drop=True)

# ---------- Print Results ----------
header = f"{'Model':<24} {'MAE':>8} {'RMSE':>8} {'R2':>8} {'CV_R2':>8}"
sep    = "-" * len(header)
print(header)
print(sep)
for i, row in results_df.iterrows():
    tag = " << BEST" if i == 0 else ""
    print(f"{row['Model']:<24} {row['MAE']:>8} {row['RMSE']:>8} {row['R2']:>8} {row['CV_R2']:>8}{tag}")
print(sep)

best_name = results_df.iloc[0]["Model"]
print(f"\nBest Model : {best_name}")
print(f"R2         : {results_df.iloc[0]['R2']}")
print(f"CV_R2      : {results_df.iloc[0]['CV_R2']}")
print(f"MAE        : {results_df.iloc[0]['MAE']}")
print(f"RMSE       : {results_df.iloc[0]['RMSE']}\n")

# ---------- Save Best Model ----------
best_model      = models[best_name]
best_model_path = os.path.join(BASE_DIR, "best_model.pkl")
with open(best_model_path, "wb") as f:
    pickle.dump(best_model, f)
print(f"Best model saved -> {best_model_path}")

# ---------- Plot Comparison Chart ----------
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle("Mess Food Feedback - Multi-Model Comparison (Issue #190)",
             fontsize=13, fontweight="bold")

names     = results_df["Model"].tolist()
r2_vals   = results_df["R2"].tolist()
mae_vals  = results_df["MAE"].tolist()
rmse_vals = results_df["RMSE"].tolist()
colors    = ["#2ecc71" if i == 0 else "#3498db" for i in range(len(names))]

# Chart 1: R2 Score
ax1 = axes[0]
bars = ax1.barh(names[::-1], r2_vals[::-1], color=colors[::-1], edgecolor="white", height=0.6)
ax1.set_xlabel("R2 Score")
ax1.set_title("R2 Score by Model", fontweight="bold")
ax1.set_xlim(0, 1.1)
ax1.grid(axis="x", linestyle="--", alpha=0.5)
for bar, val in zip(bars, r2_vals[::-1]):
    ax1.text(bar.get_width() + 0.01, bar.get_y() + bar.get_height() / 2,
             f"{val:.4f}", va="center", fontsize=9)
ax1.legend(handles=[mpatches.Patch(color="#2ecc71", label=f"Best: {best_name}")],
           loc="lower right", fontsize=9)

# Chart 2: MAE & RMSE
ax2   = axes[1]
x     = np.arange(len(names))
w     = 0.35
r1    = ax2.bar(x - w/2, mae_vals,  w, label="MAE",  color="#e74c3c", alpha=0.85)
r2    = ax2.bar(x + w/2, rmse_vals, w, label="RMSE", color="#e67e22", alpha=0.85)
ax2.set_xticks(x)
ax2.set_xticklabels(names, rotation=35, ha="right", fontsize=9)
ax2.set_ylabel("Error (lower is better)")
ax2.set_title("MAE & RMSE by Model", fontweight="bold")
ax2.legend()
ax2.grid(axis="y", linestyle="--", alpha=0.5)
for rect in list(r1) + list(r2):
    ax2.text(rect.get_x() + rect.get_width() / 2., rect.get_height() + 0.005,
             f"{rect.get_height():.3f}", ha="center", va="bottom", fontsize=7)

plt.tight_layout()
chart_path = os.path.join(BASE_DIR, "model_comparison.png")
plt.savefig(chart_path, dpi=150, bbox_inches="tight")
print(f"Comparison chart saved -> {chart_path}")

print("\nDone! Issue #190 resolved.\n")
