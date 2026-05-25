## Mess Food Feedback Analyzer

### Problem Statement
Mess food quality varies daily, and students often face inconsistency in food quality, cleanliness, quantity, and taste.

### Objective
Analyze historical mess feedback data and predict overall rating using machine learning.

### Features
- Multi-model training pipeline (`LinearRegression`, `Ridge`, `RandomForestRegressor`)
- Automatic best-model selection by R2 score
- Model metadata export with metrics (`model/model_metadata.json`)
- CLI prediction app with score validation and quality recommendations
- Data analysis charts:
  - average feature ratings bar chart
  - feature-correlation heatmap

### Dataset Columns
- `food_quality`
- `cleanliness`
- `quantity`
- `taste`
- `rating` (target)

### Requirements
Use Python 3.9+.

Install dependencies:
```bash
pip install pandas scikit-learn matplotlib
```

### How to Run
1. Train and select best model:
```bash
python model/train_model.py
```
2. Generate analytics charts:
```bash
python analysis.py
```
3. Run prediction app:
```bash
python app.py
```

### Generated Outputs
- `model/model.pkl`
- `model/model_metadata.json`
- `outputs/average_feedback.png`
- `outputs/correlation_heatmap.png`
