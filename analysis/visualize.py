
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

# Load dataset
df = pd.read_csv("data/feedback.csv")

print(df.head())

# Correlation Heatmap
plt.figure(figsize=(8,6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Feature Correlation Heatmap")
plt.show()

# Rating Distribution
plt.figure(figsize=(7,5))
sns.histplot(df["Rating"], bins=5, kde=True)
plt.title("Rating Distribution")
plt.show()

# Scatter Plot
plt.figure(figsize=(7,5))
sns.scatterplot(x=df["Taste"], y=df["Rating"])
plt.title("Taste vs Rating")
plt.show()

# Feature Importance
X = df[["FoodQuality", "Cleanliness", "Quantity", "Taste"]]
y = df["Rating"]

model = LinearRegression()
model.fit(X, y)

importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.coef_
})

plt.figure(figsize=(8,5))
sns.barplot(x="Feature", y="Importance", data=importance)
plt.title("Feature Importance")
plt.show()
