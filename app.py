from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load trained model
try:
    with open("model/model.pkl", "rb") as file:
        model = pickle.load(file)
except Exception:
    model = None


@app.route("/api/predict", methods=["POST"])
def predict():
    if model is None:
        return jsonify({
            "success": False,
            "error": "Model could not be loaded."
        }), 500

    try:
        data = request.get_json()
        if not data:
            return jsonify({
                "success": False,
                "error":"Request body is required."
            }), 400

        required_fields = [
            "food_quality",
            "cleanliness",
            "quantity",
            "taste"
        ]

        # Check for missing fields
        missing_fields = [
            field for field in required_fields
            if field not in data
        ]
        if missing_fields:
            return jsonify({
                "success": False,
                "error": "Missing fields",
                "fields": missing_fields
            }), 400

        # Convert input values to numbers
        features = [
            float(data["food_quality"]),
            float(data["cleanliness"]),
            float(data["quantity"]),
            float(data["taste"])
        ]
        prediction = model.predict([features])[0]
        return jsonify({
            "success": True,
            "prediction": round(float(prediction), 2)
        }), 200

    except (ValueError, TypeError):
        return jsonify({
            "success": False,
            "error": "All feature values must be numeric."
        }), 400
    except Exception:
        app.logger.exception("Prediction failed")

        return jsonify({
            "success": False,
            "error": "Unable to generate prediction."
        }), 500


@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({
        "status": "ok"
    }), 200
if __name__ == "__main__":
    app.run(debug=True)