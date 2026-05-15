import os
import pandas as pd
import matplotlib.pyplot as plt

# Resolve path relative to script location
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(SCRIPT_DIR, 'data', 'mess_data.csv')

data = pd.read_csv(DATA_PATH)

# Only compute averages for the input features, not the target variable (rating).
# Including 'rating' in the feature chart is misleading — it mixes what we
# predict with the factors we use for prediction.
feature_cols = ['food_quality', 'cleanliness', 'quantity', 'taste']
avg = data[feature_cols].mean()

plt.figure(figsize=(8, 5))
avg.plot(kind='bar', color=['#4361ee', '#3a86ff', '#8338ec', '#ff006e'])

plt.title("Average Mess Food Feedback Analysis", fontsize=14)
plt.xlabel("Features")
plt.ylabel("Average Rating")

plt.xticks(rotation=30)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()
