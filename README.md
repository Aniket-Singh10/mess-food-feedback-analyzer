## Problem Statement
Mess food quality varies daily, and students often face inconsistency in food quality, cleanliness, and taste.

## Objective
To analyze and predict mess food ratings using machine learning based on detailed menu feedback metrics.

## What We Updated
- Restored the project training dataset from `data/mess_feedback.json` so the model can run.
- Verified the correct Python interpreter and environment for this repo.
- Updated `analysis.py` to use the same JSON training data and show analytics for the actual training features.
- Explained why the model learned `cleanliness` as a near-zero coefficient in the trained linear regression.

## Data and Features Used
The model uses flattened JSON features from the mess feedback data:
- `cleanliness`
- `items.dal.quality`, `items.dal.taste`, `items.dal.quantity`
- `items.gravy_sabzi.quality`, `items.gravy_sabzi.taste`, `items.gravy_sabzi.quantity`
- `items.dry_sabzi.quality`, `items.dry_sabzi.taste`, `items.dry_sabzi.quantity`
- `items.rice.quality`, `items.rice.taste`, `items.rice.quantity`

## Adding More Food Items
To add more food items to the model:
1. Update `data/mess_feedback.json` with the new item under the `items` object for each record.
   Example:
   ```json
   "items": {
     "dal": { "quality": 3.0, "taste": 4.0, "quantity": 3.0 },
     "paneer": { "quality": 4.0, "taste": 4.0, "quantity": 3.0 },
     "rice": { "quality": 3.0, "taste": 4.0, "quantity": 3.0 }
   }
   ```
2. Add the new feature columns to both `model/train_model.py` and `analysis.py` in the `feature_cols` list.
   Example:
   ```python
   'items.paneer.quality',
   'items.paneer.taste',
   'items.paneer.quantity',
   ```
3. Run the training script again to retrain the model with the new features.

## Model Used
- `sklearn.linear_model.LinearRegression`
- Target: `overall_rating`

### Notes on the updated model
- The model is trained on nested JSON feedback data that is flattened before training.
- The training script now loads `data/mess_feedback.json` and fills missing values with `3.0`.
- `cleanliness` may appear to have a near-zero coefficient because the other dish metrics already explain the rating variation in this small dataset.
- The analytics script now computes both feature averages and correlations with `overall_rating` using the same training data.

## Recommended Environment
Use the conda environment that contains the required packages:
- `C:\Users\Quassar\miniconda3\envs\signlang\python.exe`

## How to Run
1. Open a terminal in the project root:
   ```powershell
   cd "C:\Users\Quassar\Documents\Codes\Projects\open source Contribution\mess-food-feedback-analyzer"
   ```
2. Run training with the correct interpreter:
   ```powershell
   & "C:\Users\Quassar\miniconda3\envs\signlang\python.exe" "model\train_model.py"
   ```
3. Run analysis:
   ```powershell
   & "C:\Users\Quassar\miniconda3\envs\signlang\python.exe" "analysis.py"
   ```

## Output
- `model/train_model.py` prints the model R² score and learned feature weights.
- `analysis.py` shows feature average values and correlations with overall rating.
