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
   pip install pandas scikit-learn matplotlib
   ```

2. Run training (supports path resolution, dataset validation, and clean-up):
   ```bash
   python model/train_model.py
   ```

3. Run analysis (calculates mean ratings and saves visualization):
   ```bash
   python analysis.py
   ```

4. Run prediction (supports CLI arguments or interactive prompt mode):
   ```bash
   # CLI mode:
   python app.py --food-quality 4.0 --cleanliness 3.5 --quantity 4.0 --taste 4.5

   # Interactive mode:
   python app.py
   ```

## Output
- **Model Training**: Saves trained model object to `model/model.pkl`.
- **Model Prediction**: Validates user inputs (numeric, range 1.0-5.0) and predicts food rating.
- **Graph Visualization**: Displays bar chart and saves it as `feedback_analysis.png`.

