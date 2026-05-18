import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("data/mess_data.csv")

# Average rating by meal type
meal_avg = data.groupby("meal_type")["rating"].mean()

print("\nAverage Rating by Meal Type:\n")
print(meal_avg)

# Bar chart
meal_avg.plot(kind='bar')

plt.title("Average Rating by Meal Type")
plt.xlabel("Meal Type")
plt.ylabel("Average Rating")

plt.show()

# Compare all features
features = data.groupby("meal_type")[[
    "food_quality",
    "cleanliness",
    "quantity",
    "taste",
    "rating"
]].mean()

print("\nFeature Comparison:\n")
print(features)

# Grouped bar chart
features.plot(kind='bar')

plt.title("Feature Comparison Across Meal Types")
plt.xlabel("Meal Type")
plt.ylabel("Average Score")

plt.show()