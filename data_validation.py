"""
Data validation and quality check script for Mess Food Feedback Analyzer
Run this before training to ensure data quality
"""

import sys
import logging
from utils import load_data, validate_data, handle_missing_values, get_data_stats
from config import DATA_PATH

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def main() -> int:
    """
    Main validation function.
    
    Returns:
        0 if validation passed, 1 if failed
    """
    try:
        logger.info("=" * 60)
        logger.info("Starting Data Validation")
        logger.info("=" * 60)
        
        # Load data
        logger.info(f"Loading data from {DATA_PATH}...")
        data = load_data(DATA_PATH)
        
        # Initial validation
        logger.info("\nValidating data structure...")
        is_valid, errors = validate_data(data)
        
        if not is_valid:
            logger.error("\nValidation failed with errors:")
            for error in errors:
                logger.error(f"  ✗ {error}")
            return 1
        
        logger.info("✓ Data structure validation passed")
        
        # Handle missing values
        logger.info("\nHandling missing values...")
        data = handle_missing_values(data)
        
        # Get statistics
        logger.info("\nGenerating data statistics...")
        stats = get_data_stats(data)
        
        logger.info("\n" + "=" * 60)
        logger.info("DATA STATISTICS")
        logger.info("=" * 60)
        logger.info(f"Total Samples: {stats['total_samples']}")
        logger.info(f"Total Features: {stats['total_features']}")
        
        logger.info("\nFeature Statistics:")
        for feature, stat_dict in stats['feature_stats'].items():
            logger.info(f"  {feature}:")
            logger.info(f"    Mean: {stat_dict['mean']:.2f}")
            logger.info(f"    Std: {stat_dict['std']:.2f}")
            logger.info(f"    Min: {stat_dict['min']:.2f}")
            logger.info(f"    Max: {stat_dict['max']:.2f}")
        
        logger.info("\nTarget Variable Statistics:")
        target_stat = stats['target_stats']
        logger.info(f"    Mean: {target_stat['mean']:.2f}")
        logger.info(f"    Std: {target_stat['std']:.2f}")
        logger.info(f"    Min: {target_stat['min']:.2f}")
        logger.info(f"    Max: {target_stat['max']:.2f}")
        
        logger.info("\n" + "=" * 60)
        logger.info("✓ Data validation completed successfully!")
        logger.info("=" * 60)
        
        return 0
    
    except Exception as e:
        logger.error(f"\n✗ Validation failed: {e}")
        return 1


if __name__ == '__main__':
    sys.exit(main())
