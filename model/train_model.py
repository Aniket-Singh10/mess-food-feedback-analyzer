import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

BASE_DIR=os.path.dirname(os.path.abspath(__file__))
csv_path=os.path.join(BASE_DIR,"..","data","mess_data.csv")


# Load dataset
data = pd.read_csv(csv_path)

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