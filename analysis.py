import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

# ==============================
# LOAD DATASET
# ==============================

data = pd.read_csv('data/mess_data.csv')

print("\nDataset Preview:\n")
print(data.head())

# ==============================
# BASIC ANALYSIS
# ==============================

avg = data.mean(numeric_only=True)

print("\nAverage Ratings:\n")
print(avg)

# ==============================
# 2D BAR CHART
# ==============================

plt.figure(figsize=(10,6))

avg.plot(
    kind='bar',
    color='skyblue',
    edgecolor='black'
)

plt.title(
    "Average Mess Food Feedback Analysis",
    fontsize=15
)

plt.xlabel("Features")
plt.ylabel("Average Rating")

plt.xticks(rotation=30)

plt.grid(
    axis='y',
    linestyle='--',
    alpha=0.7
)

plt.tight_layout()
plt.show()

# ==============================
# 3D BAR GRAPH
# ==============================

fig = plt.figure(figsize=(12,8))

ax = fig.add_subplot(111, projection='3d')

x_pos = np.arange(len(avg))
y_pos = np.zeros(len(avg))
z_pos = np.zeros(len(avg))

dx = np.ones(len(avg)) * 0.5
dy = np.ones(len(avg)) * 0.5
dz = avg.values

ax.bar3d(
    x_pos,
    y_pos,
    z_pos,
    dx,
    dy,
    dz,
    shade=True
)

ax.set_xticks(x_pos)
ax.set_xticklabels(avg.index, rotation=20)

ax.set_ylabel("Category")
ax.set_zlabel("Average Rating")

ax.set_title("3D Mess Food Feedback Analysis")

plt.show()

# ==============================
# CORRELATION HEATMAP
# ==============================

corr = data.corr(numeric_only=True)

plt.figure(figsize=(8,6))

plt.imshow(corr, cmap='coolwarm')

plt.colorbar()

plt.xticks(
    range(len(corr.columns)),
    corr.columns,
    rotation=45
)

plt.yticks(
    range(len(corr.columns)),
    corr.columns
)

plt.title("Feature Correlation Heatmap")

plt.tight_layout()
plt.show()

# ==============================
# MACHINE LEARNING MODEL
# ==============================

# Example:
# Predict Overall Rating
# using Taste, Hygiene, Quantity

X = data[['Taste', 'Hygiene', 'Quantity']]
y = data['Overall']

# Train Test Split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Linear Regression Model

model = LinearRegression()

model.fit(X_train, y_train)

# Predictions

predictions = model.predict(X_test)

# Accuracy

mse = mean_squared_error(y_test, predictions)

print("\nModel Mean Squared Error:", mse)

# ==============================
# PREDICTION GRAPH
# ==============================

plt.figure(figsize=(8,5))

plt.plot(
    y_test.values,
    label='Actual Ratings',
    marker='o'
)

plt.plot(
    predictions,
    label='Predicted Ratings',
    marker='x'
)

plt.title("Actual vs Predicted Ratings")

plt.xlabel("Test Samples")
plt.ylabel("Overall Rating")

plt.legend()

plt.grid(True)

plt.tight_layout()
plt.show()

print("\nAnalysis Completed Successfully")