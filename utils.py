"""
Utility functions for Mess Food Feedback Analyzer
Includes logging, validation, and data handling
"""

import logging
import os
from typing import Dict, Any, List, Tuple
import pandas as pd
import numpy as np
from config import (
    LOG_LEVEL, LOG_FILE, DATA_PATH, FEATURE_COLUMNS, 
    TARGET_COLUMN, FEATURE_RANGES, MIN_RATING, MAX_RATING
)

# Configure logging
logging.basicConfig(
    level=getattr(logging, LOG_LEVEL),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


def load_data(file_path: str = DATA_PATH) -> pd.DataFrame:
    """
    Load dataset from CSV file with error handling.
    
    Args:
        file_path: Path to CSV file
        
    Returns:
        DataFrame with loaded data
        
    Raises:
        FileNotFoundError: If file doesn't exist
        ValueError: If file is empty or invalid
    """
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Dataset not found at '{file_path}'")
        
        data = pd.read_csv(file_path)
        
        if data.empty:
            raise ValueError(f"Dataset at '{file_path}' is empty")
        
        logger.info(f"Successfully loaded {len(data)} samples from {file_path}")
        return data
    
    except FileNotFoundError as e:
        logger.error(f"File error: {e}")
        raise
    except pd.errors.ParserError as e:
        logger.error(f"CSV parsing error: {e}")
        raise ValueError(f"Invalid CSV format: {e}")
    except Exception as e:
        logger.error(f"Unexpected error loading data: {e}")
        raise


def validate_data(data: pd.DataFrame) -> Tuple[bool, List[str]]:
    """
    Validate dataset structure and values.
    
    Args:
        data: DataFrame to validate
        
    Returns:
        Tuple of (is_valid, error_messages)
    """
    errors: List[str] = []
    
    # Check required columns
    required_cols = FEATURE_COLUMNS + [TARGET_COLUMN]
    missing_cols = [col for col in required_cols if col not in data.columns]
    if missing_cols:
        errors.append(f"Missing columns: {missing_cols}")
    
    # Check data types
    for col in required_cols:
        if col in data.columns:
            if not pd.api.types.is_numeric_dtype(data[col]):
                errors.append(f"Column '{col}' must be numeric, got {data[col].dtype}")
    
    present_required_cols = [col for col in required_cols if col in data.columns]

    # Check for missing values (only on columns that exist)
    missing_count = data[present_required_cols].isnull().sum().sum() if present_required_cols else 0
    if missing_count > 0:
        logger.warning(f"Found {missing_count} missing values in dataset")
    
    # Check value ranges
    for col in FEATURE_COLUMNS:
        if col in data.columns:
            # Skip range checks for non-numeric columns; type error already captured above.
            if pd.api.types.is_numeric_dtype(data[col]):
                min_val, max_val = FEATURE_RANGES[col]
                out_of_range = ((data[col] < min_val) | (data[col] > max_val)).sum()
                if out_of_range > 0:
                    errors.append(
                        f"Column '{col}' has {out_of_range} values outside range "
                        f"[{min_val}, {max_val}]"
                    )
    
    if TARGET_COLUMN in data.columns:
        if pd.api.types.is_numeric_dtype(data[TARGET_COLUMN]):
            out_of_range = (
                (data[TARGET_COLUMN] < MIN_RATING) | 
                (data[TARGET_COLUMN] > MAX_RATING)
            ).sum()
            if out_of_range > 0:
                errors.append(
                    f"Target '{TARGET_COLUMN}' has {out_of_range} values outside "
                    f"range [{MIN_RATING}, {MAX_RATING}]"
                )
    
    is_valid = len(errors) == 0
    if is_valid:
        logger.info("Data validation passed")
    else:
        for error in errors:
            logger.error(f"Validation error: {error}")
    
    return is_valid, errors


def handle_missing_values(data: pd.DataFrame) -> pd.DataFrame:
    """
    Handle missing values in dataset.
    
    Args:
        data: DataFrame with potential missing values
        
    Returns:
        DataFrame with missing values handled
    """
    logger.info(f"Handling missing values. Missing count: {data.isnull().sum().sum()}")
    
    # Drop rows with missing values (conservative approach)
    # For larger datasets, could use imputation instead
    data_cleaned = data.dropna()
    
    rows_removed = len(data) - len(data_cleaned)
    if rows_removed > 0:
        logger.info(f"Removed {rows_removed} rows with missing values")
    
    return data_cleaned


def prepare_features_and_target(
    data: pd.DataFrame
) -> Tuple[pd.DataFrame, pd.Series]:
    """
    Prepare features and target for model training.
    
    Args:
        data: DataFrame containing all columns
        
    Returns:
        Tuple of (X, y) where X is features and y is target
    """
    X = data[FEATURE_COLUMNS].copy()
    y = data[TARGET_COLUMN].copy()
    
    logger.info(f"Prepared features: {list(X.columns)}")
    logger.info(f"Target variable: {TARGET_COLUMN}")
    
    return X, y


def get_data_stats(data: pd.DataFrame) -> Dict[str, Any]:
    """
    Get statistical summary of dataset.
    
    Args:
        data: DataFrame to analyze
        
    Returns:
        Dictionary with statistics
    """
    stats = {
        'total_samples': len(data),
        'total_features': len(FEATURE_COLUMNS),
        'feature_stats': data[FEATURE_COLUMNS].describe().to_dict(),
        'target_stats': data[TARGET_COLUMN].describe().to_dict(),
        'correlation': data[FEATURE_COLUMNS + [TARGET_COLUMN]].corr().to_dict()
    }
    
    logger.info(f"Dataset stats: {stats['total_samples']} samples, "
                f"{stats['total_features']} features")
    
    return stats
