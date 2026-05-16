import pickle
import numpy as np

def predict_rating(food_quality, cleanliness, quantity, taste):
    """
    Loads the saved scaler and model, scales the input features, 
    and predicts the rating.
    """
    try:
        # Load scaler
        with open('model/scaler.pkl', 'rb') as f:
            scaler = pickle.load(f)
            
        # Load model
        with open('model/model.pkl', 'rb') as f:
            model = pickle.load(f)
            
    except FileNotFoundError:
        print("Error: Model or scaler not found. Please run evaluate_models.py first.")
        return None
        
    # Prepare input data
    input_data = np.array([[food_quality, cleanliness, quantity, taste]])
    
    # Scale input
    scaled_input = scaler.transform(input_data)
    
    # Make prediction
    prediction = model.predict(scaled_input)[0]
    
    # Clip prediction to valid range [1.0, 5.0]
    prediction = np.clip(prediction, 1.0, 5.0)
    
    return prediction

if __name__ == "__main__":
    print("--- Mess Food Rating Prediction ---")
    
    # Example raw feature values (scale 1-5)
    # You can change these to test different predictions
    test_features = {
        'food_quality': 4.0,
        'cleanliness': 3.5,
        'quantity': 4.0,
        'taste': 4.5
    }
    
    print("\nInput Features:")
    for feature, value in test_features.items():
        print(f"  {feature}: {value}")
        
    predicted_rating = predict_rating(**test_features)
    
    if predicted_rating is not None:
        print(f"\nPredicted Rating: {predicted_rating:.2f} / 5.00")
