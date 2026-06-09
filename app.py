import os
import sys
import pickle
import pandas as pd
import argparse

# Get directory where app.py is located
base_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(base_dir, 'model', 'model.pkl')

def validate_input(val, name):
    """
    Validates that the input is a float and within the range [1.0, 5.0].
    """
    try:
        val_float = float(val)
    except (ValueError, TypeError):
        raise ValueError(f"'{val}' is not a valid number for {name}.")
    
    if val_float < 1.0 or val_float > 5.0:
        raise ValueError(f"{name.replace('_', ' ').title()} rating must be between 1.0 and 5.0 (received: {val_float}).")
    
    return val_float

def get_interactive_input(prompt_text, name):
    """
    Prompts the user interactively until a valid rating is provided.
    """
    while True:
        try:
            val_str = input(prompt_text).strip()
            if not val_str:
                print("Input cannot be empty. Please enter a value.")
                continue
            return validate_input(val_str, name)
        except ValueError as e:
            print(f"Invalid input: {e}")
        except (KeyboardInterrupt, EOFError):
            print("\nExiting prediction tool.")
            sys.exit(0)

def main():
    # Load model
    if not os.path.exists(model_path):
        print(f"Error: Trained model file not found at {model_path}", file=sys.stderr)
        print("Please run model training first to generate the model:", file=sys.stderr)
        print("  python model/train_model.py", file=sys.stderr)
        sys.exit(1)

    try:
        with open(model_path, 'rb') as f:
            model = pickle.load(f)
    except Exception as e:
        print(f"Error: Failed to load model: {e}", file=sys.stderr)
        sys.exit(1)

    # Argument parser
    parser = argparse.ArgumentParser(
        description="Predict Mess Food Rating based on Food Quality, Cleanliness, Quantity, and Taste."
    )
    parser.add_argument('--food-quality', type=float, help="Rating for food quality (1-5)")
    parser.add_argument('--cleanliness', type=float, help="Rating for cleanliness (1-5)")
    parser.add_argument('--quantity', type=float, help="Rating for food quantity (1-5)")
    parser.add_argument('--taste', type=float, help="Rating for food taste (1-5)")
    parser.add_argument('--interactive', action='store_true', help="Force interactive mode even if arguments are provided")

    args = parser.parse_args()

    # Determine execution mode
    interactive_mode = args.interactive or (
        args.food_quality is None and 
        args.cleanliness is None and 
        args.quantity is None and 
        args.taste is None
    )

    if interactive_mode:
        print("====================================================")
        print("        Mess Food Feedback Prediction Tool          ")
        print("====================================================")
        print("Provide ratings between 1.0 (Poor) and 5.0 (Excellent):\n")
        
        food_quality = get_interactive_input("1. Food Quality: ", "food_quality")
        cleanliness = get_interactive_input("2. Cleanliness:  ", "cleanliness")
        quantity = get_interactive_input("3. Quantity:     ", "quantity")
        taste = get_interactive_input("4. Taste:        ", "taste")
    else:
        # Check that all features are provided
        missing = []
        if args.food_quality is None: missing.append("--food-quality")
        if args.cleanliness is None: missing.append("--cleanliness")
        if args.quantity is None: missing.append("--quantity")
        if args.taste is None: missing.append("--taste")
        
        if missing:
            parser.error(f"Missing required prediction arguments: {', '.join(missing)}")
        
        try:
            food_quality = validate_input(args.food_quality, "food_quality")
            cleanliness = validate_input(args.cleanliness, "cleanliness")
            quantity = validate_input(args.quantity, "quantity")
            taste = validate_input(args.taste, "taste")
        except ValueError as e:
            parser.error(str(e))

    # Construct dataframe to avoid scikit-learn feature name warnings
    input_df = pd.DataFrame(
        [[food_quality, cleanliness, quantity, taste]], 
        columns=['food_quality', 'cleanliness', 'quantity', 'taste']
    )

    # Predict rating
    try:
        raw_prediction = model.predict(input_df)[0]
        # Clamp rating to valid 1.0 to 5.0 range
        predicted_rating = max(1.0, min(5.0, raw_prediction))
        
        print("\n----------------------------------------------------")
        print("Prediction Result:")
        print(f"  Inputs: Quality={food_quality}, Cleanliness={cleanliness}, Quantity={quantity}, Taste={taste}")
        print(f"  Predicted Rating: {predicted_rating:.2f} / 5.0")
        print("----------------------------------------------------")
    except Exception as e:
        print(f"Error during rating prediction: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
