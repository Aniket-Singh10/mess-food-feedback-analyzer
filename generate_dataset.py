import pandas as pd
import random
from datetime import datetime, timedelta

meal_types = ["Breakfast", "Lunch", "Dinner"]
hostel_blocks = ["Block-A", "Block-B", "Block-C", "Block-D"]

positive_feedback = [
    "Food was tasty and hygienic",
    "Very good service today",
    "Fresh food and clean dining area",
    "Dinner quality has improved recently",
    "Good quantity and excellent taste"
]

negative_feedback = [
    "Food was cold",
    "Rice was undercooked",
    "Too much waiting time",
    "Mess area was not clean",
    "Taste needs improvement"
]

mixed_feedback = [
    "Food was tasty but quantity was less",
    "Good service but poor cleanliness",
    "Clean environment but average taste",
    "Quantity was sufficient but food was cold"
]

rows = []

for _ in range(1000):

    food_quality = random.randint(1, 5)
    cleanliness = random.randint(1, 5)
    quantity = random.randint(1, 5)
    taste = random.randint(1, 5)

    service = random.randint(1, 5)
    waiting_time = random.randint(1, 5)

# Introduce some missing values
    if random.random() < 0.03:
        service = None

    if random.random() < 0.03:
        waiting_time = None

    feedback_text = random.choice(
        positive_feedback +
        negative_feedback +
        mixed_feedback
    )

    overall_rating = round(
        (
            food_quality +
            cleanliness +
            quantity +
            taste
        ) / 4
    )

    date = (
        datetime.today()
        - timedelta(days=random.randint(0, 365))
    ).strftime("%Y-%m-%d")

    rows.append([
        food_quality,
        cleanliness,
        quantity,
        taste,
        service,
        waiting_time,
        random.choice(meal_types),
        random.choice(hostel_blocks),
        feedback_text,
        date,
        overall_rating
    ])

df = pd.DataFrame(
    rows,
    columns=[
        "food_quality",
        "cleanliness",
        "quantity",
        "taste",
        "service",
        "waiting_time",
        "meal_type",
        "hostel_block",
        "feedback_text",
        "date",
        "rating"
    ]
)

df.to_csv("data/mess_data.csv", index=False)

print("Dataset generated successfully!")