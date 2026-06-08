import pickle 
def get_rating_input(feature_name):
    while True:
        try:
            value =float(input(f"Enter {feature_name} (1-5):"))
            if 1 <= value <= 5:
                return value
            print("Value must be between 1 and 5.")
        except ValueError:
            print("Please enter a valid number.")
def main():
    try:
        with open("model.pkl", "rb") as file:
            model =pickle.load(file)

    except FileNotFoundError:
        print("model.pkl not found.")
        print("Run train_model.py first.")
        return
    print("\n=== Mess Rating Predictor ===\n")

    food_quality = get_rating_input("Food Quality")
    cleanliness = get_rating_input("Cleanliness")
    quantity = get_rating_input("Quantity")
    taste = get_rating_input("Taste")
    prediction = model.predict([[food_quality,cleanliness,quantity,taste]])
    print(f"\nPredicted Mess Rating: "f"{prediction[0]:.2f}/5")

if __name__ == "__main__":
    main()
