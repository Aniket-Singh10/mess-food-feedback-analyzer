"""
Model training script for Mess Food Feedback Analyzer
Uses RandomForest Classifier for robust rating prediction
"""

import sys
import json
import logging
from typing import Tuple, Dict, Any
import pickle
import os

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, classification_report, mean_absolute_error
)

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import (
    DATA_PATH, FEATURE_COLUMNS, TARGET_COLUMN, TEST_SIZE,
    RANDOM_STATE, CV_FOLDS, MODEL_PATH, MODEL_PARAMS, MODEL_METADATA_PATH
)
from utils import load_data, validate_data, handle_missing_values, prepare_features_and_target

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def train_model(X_train: pd.DataFrame, y_train: pd.Series) -> RandomForestClassifier:
    """Train RandomForest Classifier model."""
    logger.info("Training RandomForest Classifier model...")
    model = RandomForestClassifier(**MODEL_PARAMS)
    model.fit(X_train, y_train)
    logger.info("✓ Model training completed")
    return model


def evaluate_model(
    model: RandomForestClassifier,
    X_test: pd.DataFrame,
    y_test: pd.Series
) -> Dict[str, Any]:
    """Evaluate model performance on test set."""
    logger.info("\nEvaluating model on test set...")
    y_pred = model.predict(X_test)
    
    metrics = {
        'accuracy': accuracy_score(y_test, y_pred),
        'precision': precision_score(y_test, y_pred, average='weighted', zero_division=0),
        'recall': recall_score(y_test, y_pred, average='weighted', zero_division=0),
        'f1_score': f1_score(y_test, y_pred, average='weighted', zero_division=0),
        'mae': mean_absolute_error(y_test, y_pred),
        'confusion_matrix': confusion_matrix(y_test, y_pred).tolist(),
    }
    
    return metrics


def cross_validate_model(
    model: RandomForestClassifier,
    X: pd.DataFrame,
    y: pd.Series
) -> Dict[str, Any]:
    """Perform k-fold cross-validation."""
    logger.info(f"\nPerforming {CV_FOLDS}-fold cross-validation...")
    
    cv_scores = cross_val_score(
        model, X, y, cv=CV_FOLDS, scoring='accuracy', n_jobs=-1
    )
    
    cv_results = {
        'fold_scores': cv_scores.tolist(),
        'mean_score': cv_scores.mean(),
        'std_score': cv_scores.std(),
        'cv_folds': CV_FOLDS
    }
    
    logger.info(f"CV Scores: {[f'{s:.4f}' for s in cv_scores]}")
    logger.info(f"Mean CV Score: {cv_results['mean_score']:.4f} "
                f"(+/- {cv_results['std_score']:.4f})")
    
    return cv_results


def get_feature_importance(
    model: RandomForestClassifier,
    feature_names: list
) -> Dict[str, float]:
    """Extract feature importance from model."""
    importances = model.feature_importances_
    return {name: float(importance) 
            for name, importance in zip(feature_names, importances)}


def save_model(
    model: RandomForestClassifier,
    model_path: str = MODEL_PATH
) -> None:
    """Save trained model to disk."""
    try:
        os.makedirs(os.path.dirname(model_path), exist_ok=True)
        with open(model_path, 'wb') as f:
            pickle.dump(model, f)
        logger.info(f"✓ Model saved to {model_path}")
    except Exception as e:
        logger.error(f"✗ Failed to save model: {e}")
        raise


def save_metadata(
    metadata: Dict[str, Any],
    metadata_path: str = MODEL_METADATA_PATH
) -> None:
    """Save model metadata."""
    try:
        from datetime import datetime
        
        os.makedirs(os.path.dirname(metadata_path), exist_ok=True)
        metadata['trained_at'] = datetime.now().isoformat()
        
        with open(metadata_path, 'w') as f:
            json.dump(metadata, f, indent=2)
        logger.info(f"✓ Model metadata saved to {metadata_path}")
    except Exception as e:
        logger.error(f"✗ Failed to save metadata: {e}")
        raise


def main() -> int:
    """Main training pipeline."""
    try:
        logger.info("=" * 70)
        logger.info("MESS FOOD FEEDBACK ANALYZER - MODEL TRAINING")
        logger.info("=" * 70)
        
        # Load and validate data
        logger.info("\n[1/6] Loading and validating data...")
        data = load_data(DATA_PATH)
        
        is_valid, errors = validate_data(data)
        if not is_valid:
            logger.error("Data validation failed!")
            return 1
        
        # Handle missing values
        data = handle_missing_values(data)
        
        # Prepare features and target
        logger.info("\n[2/6] Preparing features and target...")
        X, y = prepare_features_and_target(data)
        logger.info(f"Features shape: {X.shape}")
        logger.info(f"Target shape: {y.shape}")
        
        # Split data
        logger.info("\n[3/6] Splitting data (80/20 train/test)...")
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE, stratify=y
        )
        logger.info(f"Train set: {X_train.shape[0]} samples")
        logger.info(f"Test set: {X_test.shape[0]} samples")
        
        # Train model
        logger.info("\n[4/6] Training RandomForest Classifier...")
        model = train_model(X_train, y_train)
        
        # Evaluate on test set
        logger.info("\n[5/6] Evaluating model...")
        test_metrics = evaluate_model(model, X_test, y_test)
        
        logger.info("\nTest Set Metrics:")
        logger.info(f"  Accuracy:  {test_metrics['accuracy']:.4f}")
        logger.info(f"  Precision: {test_metrics['precision']:.4f}")
        logger.info(f"  Recall:    {test_metrics['recall']:.4f}")
        logger.info(f"  F1-Score:  {test_metrics['f1_score']:.4f}")
        logger.info(f"  MAE:       {test_metrics['mae']:.4f}")
        
        # Cross-validation
        cv_results = cross_validate_model(model, X, y)
        
        # Feature importance
        feature_importance = get_feature_importance(model, FEATURE_COLUMNS)
        logger.info("\nFeature Importance:")
        for feature, importance in sorted(feature_importance.items(), 
                                         key=lambda x: x[1], reverse=True):
            logger.info(f"  {feature}: {importance:.4f}")
        
        # Save model and metadata
        logger.info("\n[6/6] Saving model and metadata...")
        save_model(model, MODEL_PATH)
        
        metadata = {
            'model_type': 'RandomForestClassifier',
            'features': FEATURE_COLUMNS,
            'target': TARGET_COLUMN,
            'test_metrics': test_metrics,
            'cv_results': cv_results,
            'feature_importance': feature_importance,
            'train_samples': int(X_train.shape[0]),
            'test_samples': int(X_test.shape[0]),
            'total_samples': int(len(data))
        }
        save_metadata(metadata, MODEL_METADATA_PATH)
        
        logger.info("\n" + "=" * 70)
        logger.info("✓ MODEL TRAINING COMPLETED SUCCESSFULLY")
        logger.info("=" * 70)
        
        return 0
    
    except Exception as e:
        logger.error(f"\n✗ Training failed: {e}", exc_info=True)
        return 1


if __name__ == '__main__':
    sys.exit(main())
