import pandas as pd
import matplotlib.pyplot as plt

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
plt.show()
correlation = data.corr()

plt.figure(figsize=(8,6))
plt.imshow(correlation, cmap='coolwarm', interpolation='nearest')
plt.colorbar()

plt.xticks(range(len(correlation.columns)), correlation.columns, rotation=45)
plt.yticks(range(len(correlation.columns)), correlation.columns)

plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()
