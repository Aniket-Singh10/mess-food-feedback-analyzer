"""
Configuration file for Mess Food Feedback Analyzer
All hardcoded values are managed here for easy modification
"""

import os
from typing import Dict, Any

# Data Configuration
DATA_PATH: str = os.getenv('DATA_PATH', 'data/mess_data.csv')
FEATURE_COLUMNS: list = ['food_quality', 'cleanliness', 'quantity', 'taste']
TARGET_COLUMN: str = 'rating'

# Model Configuration
MODEL_PATH: str = os.getenv('MODEL_PATH', 'model/model.pkl')
MODEL_METADATA_PATH: str = 'model/model_metadata.json'
TEST_SIZE: float = 0.2
RANDOM_STATE: int = 42
CV_FOLDS: int = 5

# Model Parameters
MODEL_PARAMS: Dict[str, Any] = {
    'n_estimators': 100,
    'max_depth': 10,
    'min_samples_split': 5,
    'min_samples_leaf': 2,
    'random_state': RANDOM_STATE,
    'n_jobs': -1
}

# Visualization Configuration
FIGURE_WIDTH: int = 10
FIGURE_HEIGHT: int = 6
DPI: int = 100

# Flask API Configuration
FLASK_DEBUG: bool = os.getenv('FLASK_DEBUG', 'False') == 'True'
FLASK_PORT: int = int(os.getenv('FLASK_PORT', 5000))
FLASK_HOST: str = os.getenv('FLASK_HOST', '0.0.0.0')

# Logging Configuration
LOG_LEVEL: str = os.getenv('LOG_LEVEL', 'INFO')
LOG_FILE: str = 'app.log'

# Input Validation
MIN_RATING: int = 1
MAX_RATING: int = 5
FEATURE_MIN: int = 1
FEATURE_MAX: int = 5

# Feature ranges for validation
FEATURE_RANGES: Dict[str, tuple] = {
    'food_quality': (FEATURE_MIN, FEATURE_MAX),
    'cleanliness': (FEATURE_MIN, FEATURE_MAX),
    'quantity': (FEATURE_MIN, FEATURE_MAX),
    'taste': (FEATURE_MIN, FEATURE_MAX),
}
