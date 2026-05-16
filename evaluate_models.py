import pandas as pd
import pickle
import os
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from preprocess import load_and_preprocess_data

# Try importing XGBoost, gracefully handle if not available
try:
    from xgboost import XGBRegressor
    HAS_XGBOOST = True
except ImportError:
    HAS_XGBOOST = False
    print("Warning: XGBoost is not installed. Skipping XGBoost model.")

def evaluate_and_select_best_model():
    """
    Evaluates multiple regression models, prints their R^2 scores,
    and saves the best performing model.
    """
    X, y = load_and_preprocess_data()
    
    models = {
        'Linear Regression': LinearRegression(),
        'Random Forest': RandomForestRegressor(random_state=42),
        'SVR': SVR()
    }
    
    if HAS_XGBOOST:
        models['XGBoost'] = XGBRegressor(random_state=42)
        
    print("\nEvaluating Models (3-fold Cross Validation R^2 Score):")
    print("-" * 50)
    
    best_model_name = None
    best_model = None
    best_score = -float('inf')
    
    results = {}
    
    for name, model in models.items():
        # Using 3-fold CV since the dataset is quite small
        # Suppress potential warnings from small dataset sizes
        try:
            scores = cross_val_score(model, X, y, cv=3, scoring='r2')
            mean_score = scores.mean()
            results[name] = mean_score
            print(f"{name:<20} : {mean_score:.4f}")
            
            if mean_score > best_score:
                best_score = mean_score
                best_model_name = name
                best_model = model
        except Exception as e:
            print(f"{name:<20} : Failed to evaluate ({str(e)})")
            
    print("-" * 50)
    print(f"Best Model: {best_model_name} with R^2 = {best_score:.4f}")
    
    # Train the best model on the full cleaned dataset
    best_model.fit(X, y)
    
    # Save the model
    os.makedirs('model', exist_ok=True)
    model_path = 'model/model.pkl'
    with open(model_path, 'wb') as f:
        pickle.dump(best_model, f)
    print(f"\nBest model saved to {model_path}")
    
    # Save model info
    info_path = 'model/model_info.txt'
    with open(info_path, 'w') as f:
        f.write(f"Best Model: {best_model_name}\n")
        f.write(f"Cross-Validation R^2 Score: {best_score:.4f}\n")
        f.write("\nAll Model Scores:\n")
        for name, score in results.items():
            f.write(f"{name}: {score:.4f}\n")
    print(f"Model information saved to {info_path}")

if __name__ == "__main__":
    evaluate_and_select_best_model()
