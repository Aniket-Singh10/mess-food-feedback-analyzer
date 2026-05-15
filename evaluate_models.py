import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
try:
    from xgboost import XGBRegressor
    HAS_XGBOOST = True
except ImportError:
    HAS_XGBOOST = False

import pickle
from preprocess import preprocess_data
import os

def evaluate_models():
    # Preprocess data
    result = preprocess_data('data/mess_data.csv')
    if result is None:
        return
    X, y = result

    # Define models
    models = {
        'Linear Regression': LinearRegression(),
        'Random Forest': RandomForestRegressor(n_estimators=100, random_state=42),
        'SVR': SVR(kernel='rbf')
    }
    
    if HAS_XGBOOST:
        models['XGBoost'] = XGBRegressor(n_estimators=100, learning_rate=0.05, random_state=42)
    else:
        print("XGBoost not installed. Skipping XGBoost evaluation.")

    best_model = None
    best_score = -float('inf')
    best_model_name = ""

    print("Evaluating models...")
    for name, model in models.items():
        # Use cross-validation for more robust evaluation
        scores = cross_val_score(model, X, y, cv=3, scoring='r2')
        avg_score = scores.mean()
        print(f"{name} R^2 Score: {avg_score:.4f}")
        
        if avg_score > best_score:
            best_score = avg_score
            best_model = model
            best_model_name = name

    print(f"\nBest Model: {best_model_name} with R^2 Score: {best_score:.4f}")

    # Train the best model on all data
    best_model.fit(X, y)
    
    # Save the best model
    if not os.path.exists('model'):
        os.makedirs('model')
    pickle.dump(best_model, open('model/model.pkl', 'wb'))
    print(f"Model saved to model/model.pkl")
    
    # Save model info
    with open('model/model_info.txt', 'w') as f:
        f.write(f"Best Model: {best_model_name}\n")
        f.write(f"R^2 Score: {best_score:.4f}\n")

if __name__ == "__main__":
    evaluate_models()
