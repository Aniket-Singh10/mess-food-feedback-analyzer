"""
Unit tests for Mess Food Feedback Analyzer
Tests for data validation, model training, and API
"""

import unittest
import json
import os
import sys
import tempfile
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

import pandas as pd
import numpy as np

from config import FEATURE_COLUMNS, TARGET_COLUMN, FEATURE_RANGES
from utils import load_data, validate_data, prepare_features_and_target


class TestDataLoading(unittest.TestCase):
    """Test data loading functionality."""
    
    def setUp(self):
        """Create temporary test data."""
        self.test_data = pd.DataFrame({
            'food_quality': [1, 3, 5],
            'cleanliness': [2, 3, 4],
            'quantity': [1, 3, 5],
            'taste': [2, 4, 5],
            'rating': [1, 3, 5]
        })
        
        # Create temporary CSV file
        self.temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv')
        self.test_data.to_csv(self.temp_file.name, index=False)
        self.temp_file.close()
    
    def tearDown(self):
        """Clean up temporary file."""
        if os.path.exists(self.temp_file.name):
            os.unlink(self.temp_file.name)
    
    def test_load_data_success(self):
        """Test successful data loading."""
        data = load_data(self.temp_file.name)
        self.assertEqual(len(data), 3)
        self.assertEqual(list(data.columns), FEATURE_COLUMNS + [TARGET_COLUMN])
    
    def test_load_data_missing_file(self):
        """Test loading non-existent file."""
        with self.assertRaises(FileNotFoundError):
            load_data('/non/existent/file.csv')


class TestDataValidation(unittest.TestCase):
    """Test data validation functionality."""
    
    def test_valid_data(self):
        """Test validation of valid data."""
        data = pd.DataFrame({
            'food_quality': [1, 3, 5],
            'cleanliness': [2, 3, 4],
            'quantity': [1, 3, 5],
            'taste': [2, 4, 5],
            'rating': [1, 3, 5]
        })
        
        is_valid, errors = validate_data(data)
        self.assertTrue(is_valid)
        self.assertEqual(len(errors), 0)
    
    def test_missing_columns(self):
        """Test validation with missing columns."""
        data = pd.DataFrame({
            'food_quality': [1, 3, 5],
            'cleanliness': [2, 3, 4]
        })
        
        is_valid, errors = validate_data(data)
        self.assertFalse(is_valid)
        self.assertTrue(any('Missing columns' in error for error in errors))
    
    def test_non_numeric_data(self):
        """Test validation with non-numeric data."""
        data = pd.DataFrame({
            'food_quality': ['a', 'b', 'c'],
            'cleanliness': [2, 3, 4],
            'quantity': [1, 3, 5],
            'taste': [2, 4, 5],
            'rating': [1, 3, 5]
        })
        
        is_valid, errors = validate_data(data)
        self.assertFalse(is_valid)
        self.assertTrue(any('numeric' in error for error in errors))
    
    def test_out_of_range_values(self):
        """Test validation with out-of-range values."""
        data = pd.DataFrame({
            'food_quality': [1, 10, 5],  # 10 is out of range
            'cleanliness': [2, 3, 4],
            'quantity': [1, 3, 5],
            'taste': [2, 4, 5],
            'rating': [1, 3, 5]
        })
        
        is_valid, errors = validate_data(data)
        self.assertFalse(is_valid)
        self.assertTrue(any('outside range' in error for error in errors))


class TestFeaturePreperation(unittest.TestCase):
    """Test feature preparation functionality."""
    
    def test_feature_preparation(self):
        """Test feature and target separation."""
        data = pd.DataFrame({
            'food_quality': [1, 3, 5],
            'cleanliness': [2, 3, 4],
            'quantity': [1, 3, 5],
            'taste': [2, 4, 5],
            'rating': [1, 3, 5]
        })
        
        X, y = prepare_features_and_target(data)
        
        self.assertEqual(X.shape, (3, 4))
        self.assertEqual(y.shape, (3,))
        self.assertEqual(list(X.columns), FEATURE_COLUMNS)
        self.assertTrue((y == data['rating']).all())


class TestAPIRequests(unittest.TestCase):
    """Test API request validation."""
    
    def test_validate_input_valid(self):
        """Test validation of valid input."""
        from app import validate_input
        
        data = {
            'food_quality': 3,
            'cleanliness': 4,
            'quantity': 3,
            'taste': 4
        }
        
        is_valid, error_msg, parsed_data = validate_input(data)
        self.assertTrue(is_valid)
        self.assertEqual(error_msg, '')
        self.assertEqual(len(parsed_data), 4)
    
    def test_validate_input_missing_features(self):
        """Test validation with missing features."""
        from app import validate_input
        
        data = {'food_quality': 3, 'cleanliness': 4}
        
        is_valid, error_msg, parsed_data = validate_input(data)
        self.assertFalse(is_valid)
        self.assertIn('Missing features', error_msg)
    
    def test_validate_input_out_of_range(self):
        """Test validation with out-of-range values."""
        from app import validate_input
        
        data = {
            'food_quality': 10,  # Out of range
            'cleanliness': 4,
            'quantity': 3,
            'taste': 4
        }
        
        is_valid, error_msg, parsed_data = validate_input(data)
        self.assertFalse(is_valid)
        self.assertIn('between', error_msg)


class TestPredictionRanges(unittest.TestCase):
    """Test that predictions are in valid range."""
    
    def test_prediction_output_range(self):
        """Test that model predictions are in valid range."""
        # This would require loading actual model
        # Placeholder for integration testing
        pass


if __name__ == '__main__':
    unittest.main()
