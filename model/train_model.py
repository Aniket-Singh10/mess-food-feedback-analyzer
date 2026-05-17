import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import pickle
from pathlib import Path

# Consistent path management
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "mess_data.csv"
MODEL_PATH = BASE_DIR / "model" / "model.pkl"

def train():
    if not DATA_PATH.exists():
        print(f"Error: {DATA_PATH} not found.")
        return

    # Load dataset
    data = pd.read_csv(DATA_PATH)
    X = data[['food_quality', 'cleanliness', 'quantity', 'taste']]
    y = data['rating']

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Evaluation
    score = model.score(X_test, y_test)
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    
    print(f"Model R^2 Score: {score:.2f}")
    print(f"Mean Squared Error: {mse:.2f}")

    # Save model
    with open(MODEL_PATH, 'wb') as f:
        pickle.dump(model, f)
    print(f"Model saved to {MODEL_PATH}")

if __name__ == "__main__":
    train()