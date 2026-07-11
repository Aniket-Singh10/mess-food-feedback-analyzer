"""
Simple CLI app to predict a mess food rating using the trained
Linear Regression model saved in model/model.pkl.

Usage:
    python app.py
"""
import os
import pickle

MODEL_PATH = os.path.join(os.path.dirname(__file__), "model", "model.pkl")

def load_model(path=MODEL_PATH):
    with open(path, "rb") as f:
        return pickle.load(f)

def predict_rating(model, food_quality, cleanliness, quantity, taste):
    features = [[food_quality, cleanliness, quantity, taste]]
    return model.predict(features)[0]

def main():
    model = load_model()

    food_quality = float(input("Food Quality (1-5): "))
    cleanliness = float(input("Cleanliness (1-5): "))
    quantity = float(input("Quantity (1-5): "))
    taste = float(input("Taste (1-5): "))

    rating = predict_rating(model, food_quality, cleanliness, quantity, taste)
    print(f"Predicted Rating: {rating:.2f}")


if __name__ == "__main__":
    main()
