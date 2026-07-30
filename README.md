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
   pip install pandas scikit-learn matplotlib

2. Run training:
   python model/train_model.py

3. Run analysis:
   python analysis.py

## Output
- Model predicts rating based on inputs
- Graph visualization of feedback

## Troubleshooting

### Installation fails
- Ensure you are using the supported Node.js version.
- Run `npm install` or `npm ci`.
- Delete `node_modules` and reinstall dependencies if necessary.

### Environment variables not loading
- Verify that a `.env` file exists.
- Ensure all required variables are defined.
- Restart the development server after making changes.

## FAQ

### How do I start the project?
Run:

```bash
npm install
npm run dev
```

### How do I report a bug?
Please open a GitHub issue with reproduction steps and relevant logs.

