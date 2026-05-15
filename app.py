"""
Flask REST API for Mess Food Feedback Analyzer
Provides endpoints for model predictions and monitoring
"""

import json
import logging
import os
from typing import Dict, Any, List
import pickle

from flask import Flask, request, jsonify
import pandas as pd

from config import (
    FLASK_HOST, FLASK_PORT, FLASK_DEBUG, LOG_FILE, LOG_LEVEL,
    FEATURE_COLUMNS, MODEL_PATH, MODEL_METADATA_PATH,
    FEATURE_RANGES, MIN_RATING, MAX_RATING
)

# Setup logging
logging.basicConfig(
    level=getattr(logging, LOG_LEVEL),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

# Global model variable
model = None
model_metadata = None


def load_model() -> bool:
    """
    Load trained model from disk.
    
    Returns:
        True if successful, False otherwise
    """
    global model, model_metadata
    
    try:
        if not os.path.exists(MODEL_PATH):
            logger.error(f"Model file not found at {MODEL_PATH}")
            return False
        
        with open(MODEL_PATH, 'rb') as f:
            model = pickle.load(f)
        
        logger.info(f"✓ Model loaded from {MODEL_PATH}")
        
        # Load metadata if available
        if os.path.exists(MODEL_METADATA_PATH):
            with open(MODEL_METADATA_PATH, 'r') as f:
                model_metadata = json.load(f)
            logger.info(f"✓ Model metadata loaded from {MODEL_METADATA_PATH}")
        
        return True
    
    except Exception as e:
        logger.error(f"✗ Failed to load model: {e}")
        return False


def validate_input(data: Dict[str, Any]) -> tuple[bool, str, Dict]:
    """
    Validate prediction input data.
    
    Args:
        data: Input dictionary with features
        
    Returns:
        Tuple of (is_valid, error_message, parsed_data)
    """
    parsed_data = {}
    
    # Check if all required features are present
    missing_features = [f for f in FEATURE_COLUMNS if f not in data]
    if missing_features:
        return False, f"Missing features: {missing_features}", {}
    
    # Validate and parse each feature
    for feature in FEATURE_COLUMNS:
        try:
            value = float(data[feature])
            min_val, max_val = FEATURE_RANGES[feature]
            
            if value < min_val or value > max_val:
                return False, (
                    f"Feature '{feature}' must be between {min_val} and {max_val}, "
                    f"got {value}"
                ), {}
            
            parsed_data[feature] = value
        
        except (ValueError, TypeError):
            return False, f"Feature '{feature}' must be numeric, got {data[feature]}", {}
    
    return True, "", parsed_data


@app.route('/health', methods=['GET'])
def health_check() -> tuple[Dict[str, Any], int]:
    """Health check endpoint."""
    status = {
        'status': 'healthy',
        'model_loaded': model is not None,
        'timestamp': pd.Timestamp.now().isoformat()
    }
    return jsonify(status), 200


@app.route('/model-info', methods=['GET'])
def model_info() -> tuple[Dict[str, Any], int]:
    """Get model information and metadata."""
    if model is None:
        return jsonify({'error': 'Model not loaded'}), 500
    
    info = {
        'model_type': 'RandomForestClassifier',
        'features': FEATURE_COLUMNS,
        'feature_ranges': FEATURE_RANGES,
        'output_range': {'min': MIN_RATING, 'max': MAX_RATING},
        'metadata': model_metadata
    }
    
    return jsonify(info), 200


@app.route('/predict', methods=['POST'])
def predict() -> tuple[Dict[str, Any], int]:
    """
    Make a single prediction.
    
    Expected JSON:
    {
        "food_quality": 4,
        "cleanliness": 3,
        "quantity": 4,
        "taste": 4
    }
    
    Returns:
        JSON with prediction and confidence
    """
    if model is None:
        return jsonify({'error': 'Model not loaded'}), 500
    
    try:
        data = request.get_json()
        
        if data is None:
            return jsonify({'error': 'No JSON data provided'}), 400
        
        # Validate input
        is_valid, error_msg, parsed_data = validate_input(data)
        if not is_valid:
            return jsonify({'error': error_msg}), 400
        
        # Create DataFrame for prediction
        X = pd.DataFrame([parsed_data])
        
        # Make prediction
        prediction = model.predict(X)[0]
        
        # Get prediction probabilities if available
        probabilities = None
        if hasattr(model, 'predict_proba'):
            proba = model.predict_proba(X)[0]
            probabilities = {
                str(int(label)): float(prob)
                for label, prob in zip(model.classes_, proba)
            }
        
        response = {
            'prediction': int(prediction),
            'confidence': float(max(model.predict_proba(X)[0])),
            'probabilities': probabilities,
            'input': parsed_data
        }
        
        logger.info(f"Prediction made: {prediction} (confidence: {response['confidence']:.4f})")
        
        return jsonify(response), 200
    
    except Exception as e:
        logger.error(f"Prediction error: {e}", exc_info=True)
        return jsonify({'error': f'Prediction failed: {str(e)}'}), 500


@app.route('/batch-predict', methods=['POST'])
def batch_predict() -> tuple[Dict[str, Any], int]:
    """
    Make multiple predictions in batch.
    
    Expected JSON:
    {
        "predictions": [
            {
                "food_quality": 4,
                "cleanliness": 3,
                "quantity": 4,
                "taste": 4
            },
            ...
        ]
    }
    
    Returns:
        JSON with list of predictions
    """
    if model is None:
        return jsonify({'error': 'Model not loaded'}), 500
    
    try:
        data = request.get_json()
        
        if data is None or 'predictions' not in data:
            return jsonify({'error': 'No predictions data provided'}), 400
        
        predictions_data = data['predictions']
        
        if not isinstance(predictions_data, list):
            return jsonify({'error': 'predictions must be a list'}), 400
        
        if len(predictions_data) == 0:
            return jsonify({'error': 'predictions list is empty'}), 400
        
        # Validate all inputs
        validated_data = []
        for idx, item in enumerate(predictions_data):
            is_valid, error_msg, parsed_data = validate_input(item)
            if not is_valid:
                return jsonify({
                    'error': f'Invalid input at index {idx}: {error_msg}'
                }), 400
            validated_data.append(parsed_data)
        
        # Create DataFrame and make predictions
        X = pd.DataFrame(validated_data)
        predictions = model.predict(X)
        
        response = {
            'batch_size': len(predictions),
            'predictions': [
                {
                    'index': idx,
                    'prediction': int(pred),
                    'input': validated_data[idx]
                }
                for idx, pred in enumerate(predictions)
            ]
        }
        
        logger.info(f"Batch prediction completed: {len(predictions)} samples")
        
        return jsonify(response), 200
    
    except Exception as e:
        logger.error(f"Batch prediction error: {e}", exc_info=True)
        return jsonify({'error': f'Batch prediction failed: {str(e)}'}), 500


@app.errorhandler(404)
def not_found(error) -> tuple[Dict[str, str], int]:
    """Handle 404 errors."""
    return jsonify({'error': 'Endpoint not found. Use /health, /model-info, /predict, or /batch-predict'}), 404


@app.errorhandler(405)
def method_not_allowed(error) -> tuple[Dict[str, str], int]:
    """Handle 405 errors."""
    return jsonify({'error': 'Method not allowed'}), 405


@app.errorhandler(500)
def internal_error(error) -> tuple[Dict[str, str], int]:
    """Handle 500 errors."""
    logger.error(f"Internal server error: {error}")
    return jsonify({'error': 'Internal server error'}), 500


if __name__ == '__main__':
    logger.info("=" * 60)
    logger.info("Starting Mess Food Feedback Analyzer API")
    logger.info("=" * 60)
    
    # Load model before starting server
    if not load_model():
        logger.error("Failed to load model. Please train the model first using:")
        logger.error("  python data_validation.py")
        logger.error("  python model/train_model.py")
    else:
        logger.info("Model loaded successfully. API ready!")
        logger.info(f"Starting Flask server on {FLASK_HOST}:{FLASK_PORT}")
    
    app.run(host=FLASK_HOST, port=FLASK_PORT, debug=FLASK_DEBUG)
