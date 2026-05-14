import pandas as pd
import numpy as np

np.random.seed(42)

data = []

for i in range(200):
    food_quality = np.random.randint(1, 11)
    cleanliness = np.random.randint(1, 11)
    quantity = np.random.randint(1, 11)
    taste = np.random.randint(1, 11)

    rating = (
        0.3 * food_quality +
        0.2 * cleanliness +
        0.3 * taste +
        0.2 * quantity
    )

    rating += np.random.normal(0, 0.5)
    rating = max(1, min(10, round(rating, 1)))

    data.append([food_quality, cleanliness, quantity, taste, rating])

df = pd.DataFrame(data, columns=[
    "food_quality", "cleanliness", "quantity", "taste", "rating"
])

df.to_csv("data/mess_data.csv", index=False)

print("Dataset expanded successfully:", len(df))