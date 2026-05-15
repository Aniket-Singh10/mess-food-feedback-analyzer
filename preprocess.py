import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
import pickle
import os

def preprocess_data(file_path):
    # Load dataset
    if not os.path.exists(file_path):
        print(f"File {file_path} not found.")
        return None
    
    data = pd.read_csv(file_path)
    
    # Handle missing values
    imputer = SimpleImputer(strategy='mean')
    data_imputed = pd.DataFrame(imputer.fit_transform(data), columns=data.columns)
    
    # Remove outliers using Z-score (threshold = 3)
    # Note: With very small datasets, this might remove too much, but it's a good feature to have.
    z_scores = np.abs((data_imputed - data_imputed.mean()) / data_imputed.std())
    data_clean = data_imputed[(z_scores < 3).all(axis=1)]
    
    X = data_clean.drop('rating', axis=1)
    y = data_clean['rating']
    
    # Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    X_scaled = pd.DataFrame(X_scaled, columns=X.columns)
    
    # Save scaler for later use in prediction
    if not os.path.exists('model'):
        os.makedirs('model')
    pickle.dump(scaler, open('model/scaler.pkl', 'wb'))
    
    return X_scaled, y

if __name__ == "__main__":
    X, y = preprocess_data('data/mess_data.csv')
    if X is not None:
        print("Preprocessing complete.")
        print(f"Features shape: {X.shape}")
        print("Scaler saved to model/scaler.pkl")
