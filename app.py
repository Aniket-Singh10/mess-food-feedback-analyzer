import json
import pickle
from pathlib import Path

import pandas as pd


FEATURES = ["food_quality", "cleanliness", "quantity", "taste"]


def load_model():
    model_path = Path("model") / "model.pkl"
    with model_path.open("rb") as fh:
        return pickle.load(fh)


def load_metadata():
    metadata_path = Path("model") / "model_metadata.json"
    if metadata_path.exists():
        return json.loads(metadata_path.read_text(encoding="utf-8"))
    return {}


def get_input(feature_name: str) -> float:
    while True:
        raw = input(f"Enter {feature_name} score (1-5): ").strip()
        try:
            value = float(raw)
        except ValueError:
            print("Please enter a valid number.")
            continue
        if 1 <= value <= 5:
            return value
        print("Value must be between 1 and 5.")


def recommendation(pred_rating: float) -> str:
    if pred_rating >= 4.5:
        return "Excellent mess quality. Maintain current standards."
    if pred_rating >= 3.5:
        return "Good quality, but there is room for consistency improvement."
    if pred_rating >= 2.5:
        return "Average quality. Prioritize taste and cleanliness improvements."
    return "Low quality warning. Immediate quality intervention is recommended."


def main():
    model = load_model()
    metadata = load_metadata()
    print("Mess Food Feedback Analyzer")
    print("-" * 40)

    values = [get_input(name) for name in FEATURES]
    frame = pd.DataFrame([values], columns=FEATURES)
    prediction = float(model.predict(frame)[0])
    prediction = max(1.0, min(5.0, prediction))

    print(f"\nPredicted overall rating: {prediction:.2f}/5.00")
    print("Recommendation:", recommendation(prediction))

    if metadata:
        best_model = metadata.get("best_model", "unknown")
        print(f"Model used: {best_model}")


if __name__ == "__main__":
    main()
