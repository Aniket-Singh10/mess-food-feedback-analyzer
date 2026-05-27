import os
import pandas as pd
import matplotlib.pyplot as plt

# Load the same JSON training data used by model/train_model.py
base_dir = os.path.dirname(__file__)
json_path = os.path.join(base_dir, '..', 'data', 'mess_feedback.json')
if not os.path.exists(json_path):
    json_path = os.path.join(base_dir, 'data', 'mess_feedback.json')

raw = pd.read_json(json_path)
data = pd.json_normalize(raw.to_dict(orient='records'))
data = data.fillna(3.0)

feature_cols = [
    'cleanliness',
    'items.dal.quality', 'items.dal.taste', 'items.dal.quantity',
    'items.gravy_sabzi.quality', 'items.gravy_sabzi.taste', 'items.gravy_sabzi.quantity',
    'items.dry_sabzi.quality', 'items.dry_sabzi.taste', 'items.dry_sabzi.quantity',
    'items.rice.quality', 'items.rice.taste', 'items.rice.quantity'
]

target_col = 'overall_rating'

# Compute averages and correlations for the same features used in training
averages = data[feature_cols].mean().sort_values(ascending=False)
correlations = data[feature_cols + [target_col]].corr()[target_col].drop(target_col).sort_values(ascending=False)

print('Feature averages used in training:')
print(averages)
print('\nFeature correlation with overall_rating:')
print(correlations)

plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
averages.plot(kind='bar', color='tab:blue')
plt.title('Average Values of Training Features', fontsize=14)
plt.xlabel('Feature')
plt.ylabel('Average Value')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.subplot(1, 2, 2)
correlations.plot(kind='bar', color='tab:green')
plt.title('Feature Correlation with Overall Rating', fontsize=14)
plt.xlabel('Feature')
plt.ylabel('Pearson Correlation')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()
