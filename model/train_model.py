import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split,KFold,cross_val_score,cross_val_predict
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score
import pickle

print("Loading dataset...")
data = pd.read_csv("../data/mess_data.csv")

X = data[['food_quality', 'cleanliness', 'quantity', 'taste']]
y = data['rating']

X_train, X_test, y_train, y_test = train_test_split( X,y,test_size=0.2,random_state=42)
# Train Model
model = LinearRegression()
model.fit(X_train, y_train)
test_r2 = model.score(X_test, y_test)
print(f"R² Score: {test_r2:.4f}")

# K-Fold Cross Validation
print("\nPerforming 5-Fold Cross-Validation...")

kfold = KFold(n_splits=5,shuffle=True,random_state=42)
cv_model = LinearRegression()
r2_scores = cross_val_score(cv_model,X,y,cv=kfold,scoring="r2")

y_pred = cross_val_predict(cv_model,X,y,cv=kfold)
mse = mean_squared_error(y, y_pred)
mae = mean_absolute_error(y, y_pred)
rmse = np.sqrt(mse)
overall_r2 = r2_score(y, y_pred)

print("\nK-Fold Cross-Validation Results")
print(f"Fold R² Scores: {[round(score, 4) for score in r2_scores]}")
print(f"Mean R²: {r2_scores.mean():.4f}")
print(f"Standard Deviation: {r2_scores.std():.4f}")

print("\nPerformance Metrics")
print(f"R² Score : {overall_r2:.4f}")
print(f"MSE      : {mse:.4f}")
print(f"RMSE     : {rmse:.4f}")
print(f"MAE      : {mae:.4f}")

# Save Model
with open("model.pkl", "wb") as file:
    pickle.dump(model, file)
print("\nModel saved successfully as model.pkl") 