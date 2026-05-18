import os
import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Ensure correct working directory context if executed from root
csv_path = 'data/mess_data.csv' if os.path.exists('data/mess_data.csv') else '../data/mess_data.csv'
model_output_dir = 'model' if os.path.isdir('model') else '.'

# 1. Load dataset
if not os.path.exists(csv_path):
    raise FileNotFoundError(f"Could not find the dataset at {csv_path}. Check your path execution.")

data = pd.read_csv(csv_path)

# Extract features and target variables
X = data[['food_quality', 'cleanliness', 'quantity', 'taste']]
y = data['rating']

# 2. Split data with a fixed random_state for reproducible evaluations
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Define the dictionary of models to compare
models = {
    "Linear Regression": LinearRegression(),
    "Ridge Regression": Ridge(alpha=1.0),
    "Random Forest Regressor": RandomForestRegressor(n_estimators=100, random_state=42)
}

best_model_name = None
best_r2 = -float('inf')
best_model_instance = None
performance_summary = []

print("=" * 60)
print("  EVALUATING MULTIPLE MACHINE LEARNING MODELS FOR RATING PREDICTION")
print("=" * 60)

# 4. Train and evaluate each model dynamically
for name, model in models.items():
    # Fit model on training data
    model.fit(X_train, y_train)
    
    # Generate test predictions
    predictions = model.predict(X_test)
    
    # Compute advanced evaluation metrics
    mae = mean_absolute_error(y_test, predictions)
    mse = mean_squared_error(y_test, predictions)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, predictions)
    
    performance_summary.append({
        "Model": name,
        "MAE": round(mae, 4),
        "RMSE": round(rmse, 4),
        "R2 Score": round(r2, 4)
    })
    
    print(f"\n📈 Performance Results for: {name}")
    print(f"   -> Mean Absolute Error (MAE)      : {round(mae, 4)}")
    print(f"   -> Root Mean Squared Error (RMSE) : {round(rmse, 4)}")
    print(f"   -> R-squared (R2 Score)          : {round(r2, 4)}")
    
    # Track the optimal model based on R2 score metric
    if r2 > best_r2:
        best_r2 = r2
        best_model_name = name
        best_model_instance = model

print("\n" + "=" * 60)
print("  COMPARISON SUMMARY TABLE")
print("=" * 60)
summary_df = pd.DataFrame(performance_summary)
print(summary_df.to_string(index=False))
print("=" * 60)

# 5. Save the best performing model artifact
output_pkl_path = os.path.join(model_output_dir, 'model.pkl')
with open(output_pkl_path, 'wb') as f:
    pickle.dump(best_model_instance, f)

print(f"\n🏆 Champion Model: '{best_model_name}' tracking an R2 score of {round(best_r2, 4)}")
print(f"💾 Saved successfully to: {output_pkl_path}\n")
