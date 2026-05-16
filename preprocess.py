import pandas as pd
import numpy as np
import pickle
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from scipy import stats
import os

def load_and_preprocess_data(filepath='data/mess_data.csv'):
    """
    Loads data, imputes missing values, removes outliers using Z-score,
    scales features, and saves the scaler.
    """
    print(f"Loading data from {filepath}...")
    data = pd.read_csv(filepath)
    
    # Separate features and target
    X = data[['food_quality', 'cleanliness', 'quantity', 'taste']]
    y = data['rating']
    
    # 1. Impute missing values (if any)
    imputer = SimpleImputer(strategy='median')
    X_imputed = pd.DataFrame(imputer.fit_transform(X), columns=X.columns)
    
    # 2. Remove outliers using Z-score (threshold=3)
    z_scores = np.abs(stats.zscore(X_imputed))
    outlier_mask = (z_scores < 3).all(axis=1)
    
    X_clean = X_imputed[outlier_mask]
    y_clean = y[outlier_mask]
    
    print(f"Removed {len(X) - len(X_clean)} outliers out of {len(X)} samples.")
    
    # 3. Scale the features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_clean)
    
    # Ensure model directory exists
    os.makedirs('model', exist_ok=True)
    
    # Save the scaler
    scaler_path = 'model/scaler.pkl'
    with open(scaler_path, 'wb') as f:
        pickle.dump(scaler, f)
    print(f"Scaler saved to {scaler_path}")
    
    return X_scaled, y_clean

if __name__ == "__main__":
    X, y = load_and_preprocess_data()
    print("Preprocessing completed successfully.")
