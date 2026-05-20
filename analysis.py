import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime

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
# Create folder to store saved graphs
output_dir = "saved_graphs"
os.makedirs(output_dir, exist_ok=True)

# Generate unique filename using timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"feedback_analysis_{timestamp}.png"

# Complete file path
filepath = os.path.join(output_dir, filename)

# Save graph automatically
#plt.savefig(filepath, bbox_inches='tight')
plt.savefig(filepath, dpi=300, bbox_inches='tight')

print(f"Graph saved successfully at: {filepath}")
plt.show()
