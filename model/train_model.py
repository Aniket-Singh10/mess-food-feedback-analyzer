import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle
import sys
def main():
    try:
        print("Loading dataset")
        data = pd.read_csv('../data/mess_data.csv')
    except FileNotFoundError:
        print("Error: The dataset file '../data/mess_data.csv' was not found.")
        sys.exit(1)
    except pd.errors.EmptyDataError:
        print("Error: The dataset file is empty.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading dataset: {e}")
        sys.exit(1)
    try:
        print("Preprocessing and validating data")
        required_columns = ['food_quality', 'cleanliness', 'quantity', 'taste', 'rating']
        missing_columns = [col for col in required_columns if col not in data.columns]
        if missing_columns:
            raise ValueError(f"Missing required columns in dataset: {missing_columns}")
        # Drop rows with NaN or null values
        initial_rows = data.shape[0]
        data = data.dropna(subset=required_columns)
        dropped_na = initial_rows - data.shape[0]
        if dropped_na > 0:
            print(f"Warning: Dropped {dropped_na} rows containing NaN or null values.")
        # Convert to numeric, forcing non-numeric strings to NaN, then drop those NaNs
        for col in required_columns:
            data.loc[:, col] = pd.to_numeric(data[col], errors='coerce')
        
        # Drop rows that became NaN due to coercion
        current_rows = data.shape[0]
        data = data.dropna(subset=required_columns)
        dropped_coerced = current_rows - data.shape[0]
        if dropped_coerced > 0:
            print(f"Warning: Dropped {dropped_coerced} rows containing non-numeric data.")
        # Validate rating ranges (1-5 scale)
        current_rows = data.shape[0]
        valid_range_mask = data[required_columns].apply(lambda x: x.between(1, 5)).all(axis=1)
        data = data[valid_range_mask]
        dropped_invalid = current_rows - data.shape[0]
        if dropped_invalid > 0:
            print(f"Warning: Dropped {dropped_invalid} rows with values outside the 1-5 scale.")
        if data.empty:
            raise ValueError("Error: Dataset is empty after preprocessing and validation. Cannot train model.")
        X = data[['food_quality', 'cleanliness', 'quantity', 'taste']]
        y = data['rating']
    except Exception as e:
        print(f"Data Preprocessing Error: {e}")
        sys.exit(1)
    try:
        print("Splitting data and training model...")
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        # Train model
        model = LinearRegression()
        model.fit(X_train, y_train)
        # Accuracy
        score = model.score(X_test, y_test)
        print(f"Model Accuracy: {score:.4f}")
    except Exception as e:
        print(f"Model Training Error: {e}")
        sys.exit(1)
    try:
        print("Saving model")
        with open('model.pkl', 'wb') as file:
            pickle.dump(model, file)
        print("Model saved successfully!")
    except Exception as e:
        print(f"Error saving model: {e}")
        sys.exit(1)
if __name__ == "__main__":
    main()
