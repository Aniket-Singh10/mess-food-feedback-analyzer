import pandas as pd
import pickle
import os

def predict_rating(food_quality, cleanliness, quantity, taste):
    # Load model and scaler
    model_path = 'model/model.pkl'
    scaler_path = 'model/scaler.pkl'
    
    if not os.path.exists(model_path) or not os.path.exists(scaler_path):
        print("Model or Scaler not found. Please run evaluate_models.py first.")
        return None
    
    model = pickle.load(open(model_path, 'rb'))
    scaler = pickle.load(open(scaler_path, 'rb'))
    
    # Prepare input data
    input_data = pd.DataFrame([[food_quality, cleanliness, quantity, taste]], 
                             columns=['food_quality', 'cleanliness', 'quantity', 'taste'])
    
    # Scale input data
    input_scaled = pd.DataFrame(scaler.transform(input_data), columns=input_data.columns)
    
    # Predict
    prediction = model.predict(input_scaled)
    return prediction[0]

if __name__ == "__main__":
    # Example prediction
    print("Example Prediction:")
    q, c, qty, t = 4, 5, 4, 5
    result = predict_rating(q, c, qty, t)
    if result is not None:
        print(f"Inputs: Food Quality={q}, Cleanliness={c}, Quantity={qty}, Taste={t}")
        print(f"Predicted Rating: {result:.2f}")
