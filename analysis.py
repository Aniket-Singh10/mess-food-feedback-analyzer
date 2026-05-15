import os
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

OUTPUT_DIR = "visualizations"
os.makedirs(OUTPUT_DIR, exist_ok=True)

data = pd.read_csv('data/mess_data.csv')
avg = data.mean()

plt.figure(figsize=(8,5))
avg.plot(kind='bar')

plt.title("Average Mess Food Feedback Analysis", fontsize=14)
plt.xlabel("Features")
plt.ylabel("Average Rating")

plt.xticks(rotation=30)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"feedback_analysis_{timestamp}.png"
filepath = os.path.join(OUTPUT_DIR, filename)

if os.path.exists(filepath):
    counter = 1
    base = f"feedback_analysis_{timestamp}"
    while os.path.exists(os.path.join(OUTPUT_DIR, f"{base}_{counter}.png")):
        counter += 1
    filepath = os.path.join(OUTPUT_DIR, f"{base}_{counter}.png")

plt.savefig(filepath, dpi=150, bbox_inches='tight')
print(f"✅ Graph saved to: {filepath}")
plt.show()
