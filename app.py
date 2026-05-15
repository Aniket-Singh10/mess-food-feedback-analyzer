import pickle
import numpy as np

def predict_rating():
    print("--- Mess Food Rating Predictor ---")
    try:
        # Load the trained model
        with open('model/model.pkl', 'rb') as f:
            model = pickle.load(f)
        
        # Get user inputs
        print("\nPlease enter ratings (1-10) for the following:")
        quality = float(input("Food Quality: "))
        cleanliness = float(input("Cleanliness: "))
        quantity = float(input("Quantity: "))
        taste = float(input("Taste: "))
        
        # Prepare data for prediction
        features = np.array([[quality, cleanliness, quantity, taste]])
        
        # Make prediction
        prediction = model.predict(features)[0]
        
        print(f"\nPredicted Overall Rating: {prediction:.2f} / 10")
        
    except FileNotFoundError:
        print("Error: model.pkl not found. Please run 'python model/train_model.py' first.")
    except ValueError:
        print("Error: Please enter valid numeric values between 1 and 10.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    predict_rating()
