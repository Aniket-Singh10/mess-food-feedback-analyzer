import pandas as pd
import matplotlib.pyplot as plt
import os
import sys

# Get directory where analysis.py is located
base_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(base_dir, 'data', 'mess_data.csv')

print(f"Checking for dataset at: {csv_path}")

# Validation 1: Check if the CSV file exists
if not os.path.exists(csv_path):
    print(f"Error: Dataset file not found at {csv_path}", file=sys.stderr)
    sys.exit(1)

# Validation 2: Check if dataset file is empty
if os.path.getsize(csv_path) == 0:
    print(f"Error: Dataset file at {csv_path} is empty", file=sys.stderr)
    sys.exit(1)

# Validation 3: Parse CSV safely
try:
    data = pd.read_csv(csv_path)
except Exception as e:
    print(f"Error: Failed to parse CSV file: {e}", file=sys.stderr)
    sys.exit(1)

if data.empty:
    print("Error: Dataset is empty. Cannot perform analysis.", file=sys.stderr)
    sys.exit(1)

# Validation 4: Calculate mean of numeric columns only to prevent warnings/errors
numeric_data = data.select_dtypes(include=['number'])
if numeric_data.empty:
    print("Error: No numeric columns found in the dataset to analyze.", file=sys.stderr)
    sys.exit(1)

avg = numeric_data.mean()

print("\nAverage Mess Food Feedback Analysis:")
for col, val in avg.items():
    print(f"  {col.replace('_', ' ').title()}: {val:.2f}")

# Plot styling and creation
plt.figure(figsize=(8, 5))
avg.plot(kind='bar', color='#4F46E5', edgecolor='#3730A3', linewidth=1.2)

plt.title("Average Mess Food Feedback Analysis", fontsize=14, fontweight='bold', pad=15)
plt.xlabel("Features", fontsize=11, labelpad=10)
plt.ylabel("Average Rating (1-5)", fontsize=11, labelpad=10)

plt.xticks(rotation=30)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()

# Save plot to file so it's accessible in headless/CI environments
output_plot_path = os.path.join(base_dir, 'feedback_analysis.png')
try:
    plt.savefig(output_plot_path, dpi=150)
    print(f"\nAnalysis plot saved successfully to {output_plot_path}")
except Exception as e:
    print(f"\nWarning: Could not save plot to file: {e}", file=sys.stderr)

# Attempt to show the plot if GUI is available
try:
    # Check if a display exists or if matplotlib is running with a GUI backend
    if plt.get_backend().lower() != 'agg':
        plt.show()
    else:
        print("Note: Running in a headless environment. Displaying plot window skipped.")
except Exception as e:
    print(f"Note: Could not display plot window: {e}")
