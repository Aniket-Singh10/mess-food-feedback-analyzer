import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv('data/mess_data.csv')

# Handle missing values
data = data.fillna(data.mean())

# Calculate average ratings
avg = data.mean()

# Apply dark theme
plt.style.use('dark_background')

# Create figure
plt.figure(figsize=(9, 6))

# Create bar chart
ax = avg.plot(kind='bar')

# Add value labels on bars
for i, value in enumerate(avg):
    plt.text(
        i,
        value + 0.05,
        f"{value:.2f}",
        ha='center',
        fontsize=10,
        fontweight='bold'
    )

# Graph title and labels
plt.title(
    "Average Mess Food Feedback Analysis",
    fontsize=16,
    fontweight='bold'
)

plt.xlabel("Features", fontsize=12)
plt.ylabel("Average Rating", fontsize=12)

# Rotate x-axis labels
plt.xticks(rotation=20)

# Add grid
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Adjust layout
plt.tight_layout()

# Show graph
plt.show()