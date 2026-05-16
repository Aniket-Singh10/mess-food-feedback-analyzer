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

2. Run data preprocessing and model evaluation:
   ```bash
   python evaluate_models.py
   ```
   *This evaluates multiple models, selects the best one, and saves it to the `model/` folder.*

3. Make predictions using the best model:
   ```bash
   python predict.py
   ```

4. Run the basic training script (Legacy):
   ```bash
   python model/train_model.py
   ```

5. Run analysis visualization:
   ```bash
   python analysis.py
   ```

## Output
- Model predicts rating based on inputs
- Graph visualization of feedback
