import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from sklearn.metrics import r2_score
import pickle

# Load dataset
data = pd.read_csv('../data/mess_data.csv')

# Features and target
X = data[['food_quality', 'cleanliness', 'quantity', 'taste']]
y = data['rating']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Models dictionary
models = {
    "Linear Regression": LinearRegression(),
    "Decision Tree": DecisionTreeRegressor(),
    "Random Forest": RandomForestRegressor(),
    "KNN": KNeighborsRegressor(),
    "SVR": SVR()
}

best_model = None
best_score = -1
best_model_name = ""

# Train and evaluate models
for name, model in models.items():

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    score = r2_score(y_test, predictions)

    print(f"{name} Accuracy: {score}")

    if score > best_score:
        best_score = score
        best_model = model
        best_model_name = name

print(f"\nBest Model: {best_model_name}")
print(f"Best Accuracy: {best_score}")

# Save best model
pickle.dump(best_model, open('model.pkl', 'wb'))

print("Best model saved successfully!")