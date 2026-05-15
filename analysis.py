"""
Data analysis and visualization script for Mess Food Feedback
Generates comprehensive insights about the feedback data
"""

import sys
import logging
from typing import Dict, Any

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from config import (
    DATA_PATH, FEATURE_COLUMNS, TARGET_COLUMN,
    FIGURE_WIDTH, FIGURE_HEIGHT, DPI
)
from utils import load_data, validate_data, handle_missing_values, get_data_stats

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def plot_feature_distributions(data: pd.DataFrame, output_path: str = None) -> None:
    """
    Plot distributions of all features.
    
    Args:
        data: DataFrame with features
        output_path: Path to save figure (optional)
    """
    logger.info("Generating feature distribution plots...")
    
    fig, axes = plt.subplots(2, 2, figsize=(FIGURE_WIDTH, FIGURE_HEIGHT))
    fig.suptitle('Feature Distributions', fontsize=16, fontweight='bold')
    
    for idx, feature in enumerate(FEATURE_COLUMNS):
        ax = axes[idx // 2, idx % 2]
        data[feature].hist(bins=20, ax=ax, color='skyblue', edgecolor='black')
        ax.set_title(f'{feature.replace("_", " ").title()}')
        ax.set_xlabel('Rating')
        ax.set_ylabel('Frequency')
        ax.grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    
    if output_path:
        plt.savefig(output_path, dpi=DPI, bbox_inches='tight')
        logger.info(f"Saved distribution plot to {output_path}")
    
    plt.show()


def plot_feature_averages(data: pd.DataFrame, output_path: str = None) -> None:
    """
    Plot average ratings for each feature.
    
    Args:
        data: DataFrame with features
        output_path: Path to save figure (optional)
    """
    logger.info("Generating feature average plot...")
    
    feature_averages = data[FEATURE_COLUMNS].mean()
    
    fig, ax = plt.subplots(figsize=(FIGURE_WIDTH, FIGURE_HEIGHT * 0.6))
    bars = ax.bar(range(len(feature_averages)), feature_averages.values, 
                   color='steelblue', edgecolor='black', alpha=0.8)
    
    # Add value labels on bars
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.2f}', ha='center', va='bottom', fontweight='bold')
    
    ax.set_xticks(range(len(feature_averages)))
    ax.set_xticklabels([col.replace('_', ' ').title() for col in feature_averages.index])
    ax.set_title('Average Feature Ratings', fontsize=14, fontweight='bold')
    ax.set_ylabel('Average Rating')
    ax.set_ylim(0, 5.5)
    ax.grid(axis='y', linestyle='--', alpha=0.3)
    
    plt.tight_layout()
    
    if output_path:
        plt.savefig(output_path, dpi=DPI, bbox_inches='tight')
        logger.info(f"Saved average plot to {output_path}")
    
    plt.show()


def plot_correlation_matrix(data: pd.DataFrame, output_path: str = None) -> None:
    """
    Plot correlation matrix heatmap.
    
    Args:
        data: DataFrame with all columns
        output_path: Path to save figure (optional)
    """
    logger.info("Generating correlation matrix...")
    
    cols_to_plot = FEATURE_COLUMNS + [TARGET_COLUMN]
    corr_matrix = data[cols_to_plot].corr()
    
    fig, ax = plt.subplots(figsize=(FIGURE_WIDTH * 0.8, FIGURE_HEIGHT * 0.8))
    sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm', 
                center=0, square=True, ax=ax, cbar_kws={'label': 'Correlation'})
    
    ax.set_title('Feature Correlation Matrix', fontsize=14, fontweight='bold')
    
    plt.tight_layout()
    
    if output_path:
        plt.savefig(output_path, dpi=DPI, bbox_inches='tight')
        logger.info(f"Saved correlation plot to {output_path}")
    
    plt.show()


def plot_target_distribution(data: pd.DataFrame, output_path: str = None) -> None:
    """
    Plot target variable distribution.
    
    Args:
        data: DataFrame with target column
        output_path: Path to save figure (optional)
    """
    logger.info("Generating target distribution plot...")
    
    fig, ax = plt.subplots(figsize=(FIGURE_WIDTH * 0.7, FIGURE_HEIGHT * 0.6))
    
    rating_counts = data[TARGET_COLUMN].value_counts().sort_index()
    bars = ax.bar(rating_counts.index, rating_counts.values, 
                   color='coral', edgecolor='black', alpha=0.8)
    
    # Add value labels
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height)}', ha='center', va='bottom', fontweight='bold')
    
    ax.set_xlabel('Rating')
    ax.set_ylabel('Count')
    ax.set_title('Target Variable Distribution', fontsize=14, fontweight='bold')
    ax.set_xticks(range(1, 6))
    ax.grid(axis='y', linestyle='--', alpha=0.3)
    
    plt.tight_layout()
    
    if output_path:
        plt.savefig(output_path, dpi=DPI, bbox_inches='tight')
        logger.info(f"Saved target distribution plot to {output_path}")
    
    plt.show()


def print_statistics(stats: Dict[str, Any]) -> None:
    """
    Print detailed statistics to console.
    
    Args:
        stats: Statistics dictionary from get_data_stats()
    """
    logger.info("\n" + "=" * 70)
    logger.info("DETAILED DATA STATISTICS")
    logger.info("=" * 70)
    
    logger.info(f"\nTotal Samples: {stats['total_samples']}")
    logger.info(f"Total Features: {stats['total_features']}")
    
    logger.info("\nFeature Statistics:")
    logger.info("-" * 70)
    for feature, stat_dict in stats['feature_stats'].items():
        logger.info(f"\n{feature.upper()}:")
        for stat_name, value in stat_dict.items():
            logger.info(f"  {stat_name:10s}: {value:8.2f}")
    
    logger.info(f"\n\n{TARGET_COLUMN.upper()} Statistics:")
    logger.info("-" * 70)
    for stat_name, value in stats['target_stats'].items():
        logger.info(f"  {stat_name:10s}: {value:8.2f}")
    
    logger.info("\n" + "=" * 70)


def main() -> int:
    """
    Main analysis pipeline.
    
    Returns:
        0 on success, 1 on failure
    """
    try:
        logger.info("=" * 70)
        logger.info("MESS FOOD FEEDBACK - DATA ANALYSIS")
        logger.info("=" * 70)
        
        # Load and validate data
        logger.info("\nLoading data...")
        data = load_data(DATA_PATH)
        
        is_valid, errors = validate_data(data)
        if not is_valid:
            logger.error("Data validation failed!")
            return 1
        
        # Handle missing values
        data = handle_missing_values(data)
        
        # Get statistics
        stats = get_data_stats(data)
        print_statistics(stats)
        
        # Generate visualizations
        logger.info("\nGenerating visualizations...")
        plot_feature_distributions(data, 'analysis_feature_distributions.png')
        plot_feature_averages(data, 'analysis_feature_averages.png')
        plot_correlation_matrix(data, 'analysis_correlation.png')
        plot_target_distribution(data, 'analysis_target_distribution.png')
        
        logger.info("\n" + "=" * 70)
        logger.info("✓ ANALYSIS COMPLETED SUCCESSFULLY")
        logger.info("=" * 70)
        
        return 0
    
    except Exception as e:
        logger.error(f"\n✗ Analysis failed: {e}", exc_info=True)
        return 1


if __name__ == '__main__':
    sys.exit(main())
