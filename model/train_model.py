import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

# Load dataset
data = pd.read_csv('../data/mess_data.csv')

X = data[['food_quality', 'cleanliness', 'quantity', 'taste']]
y = data['rating']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Accuracy
score = model.score(X_test, y_test)
print(f"Model Accuracy: {score}")

# Save model
pickle.dump(model, open('model.pkl', 'wb'))
print("Model saved successfully!")