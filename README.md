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

## Enhanced Dataset

The dataset has been upgraded from a small demo dataset (~15 rows) to a realistic synthetic dataset containing 1000+ feedback entries.

### Dataset Features

* Food Quality Rating
* Cleanliness Rating
* Quantity Rating
* Taste Rating
* Service Rating
* Waiting Time Rating
* Meal Type (Breakfast/Lunch/Dinner)
* Hostel Block Information
* Student Feedback Text
* Feedback Date
* Overall Rating

### Improvements

* Increased dataset size for better analytics
* Added realistic student feedback comments
* Added contextual information such as meal type and hostel block
* Improved variability in ratings
* Supports future machine learning and NLP tasks
* Suitable for sentiment analysis experiments

### Dataset Generation

A dataset generation script (`generate_dataset.py`) has been added to create realistic synthetic mess feedback data for experimentation and model training.
