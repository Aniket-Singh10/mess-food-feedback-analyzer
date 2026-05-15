## Mess Food Feedback Analyzer

Analyze and predict mess food ratings using Machine Learning (Linear Regression) based on student feedback.

## Problem Statement
Mess food quality varies daily, and students often face inconsistency in food quality, cleanliness, and taste.

## Objective
To analyze and predict mess food ratings using machine learning based on different factors.

## Features Used
- Food Quality
- Cleanliness
- Quantity
- Taste

## Model Used
Linear Regression

## How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Train the model:
   ```bash
   python model/train_model.py
   ```

3. Run analysis (generates a bar chart of average feedback):
   ```bash
   python analysis.py
   ```

4. Run prediction (interactive CLI):
   ```bash
   python app.py
   ```

## Output
- Model predicts overall rating (1–5) based on four input features
- Graph visualization of average feedback per feature
