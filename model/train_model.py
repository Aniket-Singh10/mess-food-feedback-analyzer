import json
import pickle
from pathlib import Path

import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split


RANDOM_STATE = 42
FEATURES = ["food_quality", "cleanliness", "quantity", "taste"]


def load_data() -> pd.DataFrame:
    repo_root = Path(__file__).resolve().parents[1]
    data_path = repo_root / "data" / "mess_data.csv"
    return pd.read_csv(data_path)


def build_models() -> dict:
    return {
        "linear_regression": LinearRegression(),
        "ridge": Ridge(alpha=1.0, random_state=RANDOM_STATE),
        "random_forest": RandomForestRegressor(
            n_estimators=200,
            max_depth=8,
            random_state=RANDOM_STATE,
        ),
    }


def evaluate(model, x_test, y_test) -> dict:
    y_pred = model.predict(x_test)
    return {
        "r2": float(r2_score(y_test, y_pred)),
        "mae": float(mean_absolute_error(y_test, y_pred)),
        "rmse": float(mean_squared_error(y_test, y_pred) ** 0.5),
    }


def main() -> None:
    data = load_data()
    x = data[FEATURES]
    y = data["rating"]

    x_train, x_test, y_train, y_test = train_test_split(
        x,
        y,
        test_size=0.2,
        random_state=RANDOM_STATE,
    )

    model_candidates = build_models()
    metrics_by_model = {}
    best_model_name = None
    best_score = float("-inf")
    best_model = None

    for model_name, model in model_candidates.items():
        model.fit(x_train, y_train)
        metrics = evaluate(model, x_test, y_test)
        metrics_by_model[model_name] = metrics
        if metrics["r2"] > best_score:
            best_score = metrics["r2"]
            best_model_name = model_name
            best_model = model

    model_dir = Path(__file__).resolve().parent
    model_path = model_dir / "model.pkl"
    metadata_path = model_dir / "model_metadata.json"

    with model_path.open("wb") as fh:
        pickle.dump(best_model, fh)

    metadata = {
        "best_model": best_model_name,
        "features": FEATURES,
        "random_state": RANDOM_STATE,
        "metrics": metrics_by_model,
    }
    metadata_path.write_text(json.dumps(metadata, indent=2), encoding="utf-8")

    print(f"Best model: {best_model_name}")
    print(f"Best R2: {best_score:.4f}")
    print(f"Saved trained model to: {model_path}")
    print(f"Saved metadata to: {metadata_path}")


if __name__ == "__main__":
    main()
