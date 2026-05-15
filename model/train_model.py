import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    r2_score,
    mean_absolute_error,
    mean_squared_error,
    explained_variance_score,
    max_error
)
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

# Predictions
y_pred = model.predict(X_test)

# Accuracy
score = model.score(X_test, y_test)
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred) ** 0.5
evs = explained_variance_score(y_test, y_pred)
max_err = max_error(y_test, y_pred)

print(f"Model Accuracy: {score}")
print(f"R2 Score: {r2:.4f}")
print(f"MAE: {mae:.4f}")
print(f"MSE: {mse:.4f}")
print(f"RMSE: {rmse:.4f}")
print(f"Explained Variance Score: {evs:.4f}")
print(f"Max Error: {max_err:.4f}")

# Save model
pickle.dump(model, open('model.pkl', 'wb'))
print("Model saved successfully!")