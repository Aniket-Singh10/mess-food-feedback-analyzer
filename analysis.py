import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

data = pd.read_csv("data/mess_data.csv")
output_dir = Path("outputs")
output_dir.mkdir(exist_ok=True)

avg = data.mean()

plt.figure(figsize=(8, 5))
avg.plot(kind="bar")

plt.title("Average Mess Food Feedback Analysis", fontsize=14)
plt.xlabel("Features")
plt.ylabel("Average Rating")

plt.xticks(rotation=30)
plt.grid(axis="y", linestyle="--", alpha=0.7)

plt.tight_layout()
plt.savefig(output_dir / "average_feedback.png", dpi=200)
plt.close()

corr = data.corr(numeric_only=True)
plt.figure(figsize=(7, 5))
im = plt.imshow(corr, cmap="YlGnBu", vmin=-1, vmax=1)
plt.colorbar(im, fraction=0.046, pad=0.04)
plt.xticks(range(len(corr.columns)), corr.columns, rotation=45, ha="right")
plt.yticks(range(len(corr.columns)), corr.columns)
plt.title("Feature Correlation Heatmap")
plt.tight_layout()
plt.savefig(output_dir / "correlation_heatmap.png", dpi=200)
plt.close()

print("Saved analysis charts:")
print(f"- {output_dir / 'average_feedback.png'}")
print(f"- {output_dir / 'correlation_heatmap.png'}")
