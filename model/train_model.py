import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle
import os

# 1. Load JSON dataset from the data folder
# If running from inside the 'model/' folder, path is '../data/mess_feedback.json'
json_path = '../data/mess_feedback.json'

# Safety check: if running from the root project directory instead
if not os.path.exists(json_path):
    json_path = 'data/mess_feedback.json'

# Read the raw JSON and flatten its nested structure automatically
df_raw = pd.read_json(json_path)
data = pd.json_normalize(df_raw.to_dict(orient='records'))

# Fill any missing dish metrics with a neutral score of 3.0 so the model doesn't crash
data = data.fillna(3.0)

# 2. Map all your specific granular features across different dishes
X = data[[
    'cleanliness',
    'items.dal.quality', 'items.dal.taste', 'items.dal.quantity',
    'items.gravy_sabzi.quality', 'items.gravy_sabzi.taste', 'items.gravy_sabzi.quantity',
    'items.dry_sabzi.quality', 'items.dry_sabzi.taste', 'items.dry_sabzi.quantity',
    'items.rice.quality', 'items.rice.taste', 'items.rice.quantity'
]]

# Your target prediction column (renamed slightly to match the new JSON key)
y = data['overall_rating']

# 3. Split data (using a smaller test size like 10% or 20% since we have 15 rows)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Train model
model = LinearRegression()
model.fit(X_train, y_train)

# 5. Accuracy
score = model.score(X_test, y_test)
print(f"Model R² Accuracy: {score:.4f}")

# 6. Save model using your pickle method
pickle.dump(model, open('model.pkl', 'wb'))
print("Model saved successfully as model.pkl!")

# Extra open-source perk: Let's print out the weights to verify it works!
print("\n--- Learned Feature Weights ---")
for feature, coef in zip(X.columns, model.coef_):
    clean_name = feature.replace('items.', '').replace('.', ' ').title()
    print(f"{clean_name}: {coef:.3f}")