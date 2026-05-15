"""
Mess Food Feedback Analyzer — CLI Prediction Interface

Loads the trained Linear Regression model and predicts the overall
mess food rating from four input features.

Usage:
    python app.py
"""

import os
import sys
import pickle


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(SCRIPT_DIR, 'model', 'model.pkl')

FEATURES = ['food_quality', 'cleanliness', 'quantity', 'taste']
VALID_RANGE = (1, 5)


def load_model():
    """Load the trained model from disk."""
    if not os.path.exists(MODEL_PATH):
        print(
            "Error: Trained model not found at '{}'. "
            "Run 'python model/train_model.py' first.".format(MODEL_PATH)
        )
        sys.exit(1)

    with open(MODEL_PATH, 'rb') as f:
        model = pickle.load(f)
    return model


def get_rating(prompt):
    """Prompt the user for a rating between 1 and 5."""
    while True:
        try:
            value = int(input(prompt))
            if VALID_RANGE[0] <= value <= VALID_RANGE[1]:
                return value
            print(
                "  Please enter a value between {} and {}.".format(
                    VALID_RANGE[0], VALID_RANGE[1]
                )
            )
        except ValueError:
            print("  Invalid input. Please enter a whole number.")


def main():
    model = load_model()

    print("\n=== Mess Food Feedback Analyzer ===")
    print("Rate each factor from {} to {}:\n".format(VALID_RANGE[0], VALID_RANGE[1]))

    inputs = []
    for feature in FEATURES:
        label = feature.replace('_', ' ').title()
        value = get_rating("  {}: ".format(label))
        inputs.append(value)

    prediction = model.predict([inputs])[0]
    # Clamp prediction to valid range
    prediction = max(VALID_RANGE[0], min(VALID_RANGE[1], round(prediction, 2)))

    print("\n---------------------------------")
    print("  Predicted Overall Rating: {:.2f} / {}".format(prediction, VALID_RANGE[1]))
    print("---------------------------------\n")


if __name__ == '__main__':
    main()
