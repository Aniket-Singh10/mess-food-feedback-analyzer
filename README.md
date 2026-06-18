# Mess Food Feedback Analyzer

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange.svg)
![pandas](https://img.shields.io/badge/pandas-Data-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## Overview

**Mess Food Feedback Analyzer** is a machine learning project that predicts institutional food ratings based on customer feedback. The system analyzes key factors affecting food satisfaction—including quality, cleanliness, quantity, and taste—to provide predictive insights and identify trends in dining service performance.

This project is designed to help institutional food services improve their meal quality by understanding which factors most significantly impact overall ratings.

## Features

- **Predictive Analytics**: Uses Linear Regression to predict overall food ratings
- **Multi-factor Analysis**: Evaluates food quality, cleanliness, quantity, and taste
- **Data Visualization**: Generates bar charts showing average ratings across different factors
- **Model Serialization**: Saves trained models for easy deployment and reuse
- **Scalable Dataset**: Built to handle growing feedback data

## Tech Stack

| Component | Technology |
|-----------|------------|
| **Language** | Python 3.x |
| **ML Framework** | scikit-learn |
| **Data Processing** | pandas |
| **Visualization** | matplotlib |
| **Model Serialization** | pickle |

## Project Structure

```
mess-food-feedback-analyzer/
├── README.md                    # Project documentation
├── app.py                       # Application entry point
├── analysis.py                  # Data analysis and visualization
├── data/
│   └── mess_data.csv           # Training dataset with feedback records
├── model/
│   ├── train_model.py          # Model training script
│   └── model.pkl               # Trained model (binary format)
└── Project_Report.pdf          # Detailed project report
```

## Installation

### Prerequisites
- Python 3.6 or higher
- pip (Python package manager)

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/mess-food-feedback-analyzer.git
   cd mess-food-feedback-analyzer
   ```

2. **Create a virtual environment** (optional but recommended)
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install pandas scikit-learn matplotlib
   ```

## Configuration

The dataset `mess_data.csv` contains feedback records with the following columns:

| Column | Type | Range | Description |
|--------|------|-------|-------------|
| `food_quality` | Integer | 1-5 | Rating of food quality |
| `cleanliness` | Integer | 1-5 | Rating of hygiene and cleanliness |
| `quantity` | Integer | 1-5 | Rating of portion size |
| `taste` | Integer | 1-5 | Rating of food taste |
| `rating` | Integer | 1-5 | Overall satisfaction rating |

## Usage

### Train the Model

Train the Linear Regression model on the dataset:

```bash
python model/train_model.py
```

**Expected output:**
```
Model Accuracy: 0.XX
Model saved successfully!
```

The trained model is saved as `model.pkl` for future predictions.

### Analyze Data

Generate visualization of average feedback across all factors:

```bash
python analysis.py
```

This produces a bar chart showing:
- Average ratings for food_quality, cleanliness, quantity, taste
- Overall feedback trends
- Visual comparison across features

### Make Predictions

To use the trained model for predictions, load and use the saved model:

```python
import pickle
import numpy as np

# Load the model
model = pickle.load(open('model/model.pkl', 'rb'))

# Example: Predict rating
features = np.array([[4, 4, 3, 4]])  # [quality, cleanliness, quantity, taste]
predicted_rating = model.predict(features)
print(f"Predicted Rating: {predicted_rating[0]:.2f}")
```

## Machine Learning Model

**Algorithm**: Linear Regression

- **Purpose**: Predict overall food rating based on four independent features
- **Training/Test Split**: 80/20
- **Features**: food_quality, cleanliness, quantity, taste
- **Target Variable**: rating
- **Model Performance**: Accuracy score displayed on training completion

## API/Data Interface

### Input Format

Features expected by the model:
```
[food_quality, cleanliness, quantity, taste]
```

All values should be integers in the range 1-5.

### Output Format

```
Predicted Rating: X.XX
```

Where X.XX is the predicted overall rating (typically 1.0-5.0).

## Screenshots

**Data Visualization Output:**

The analysis script generates a bar chart showing average feedback metrics:
- X-axis: Features (food_quality, cleanliness, quantity, taste)
- Y-axis: Average Rating (0-5 scale)
- Grid lines for easy reading

## Testing

### Test the Model Pipeline

```bash
# Step 1: Train the model
python model/train_model.py

# Step 2: Verify model.pkl was created
# Step 3: Run analysis
python analysis.py

# Step 4: Verify chart visualization displays
```

### Manual Testing

Test predictions with sample data:

```python
import pickle
import numpy as np

model = pickle.load(open('model/model.pkl', 'rb'))

# Test cases
test_cases = [
    ([5, 5, 5, 5], "Excellent"),
    ([1, 1, 1, 1], "Poor"),
    ([3, 3, 3, 3], "Average")
]

for features, expectation in test_cases:
    prediction = model.predict([features])[0]
    print(f"{expectation}: {prediction:.2f}")
```

## Deployment

### Requirements for Production

- Python 3.6+ runtime
- Required packages: pandas, scikit-learn, matplotlib
- Pre-trained model: `model/model.pkl`

### Deployment Steps

1. Ensure all dependencies are installed
2. Place `model.pkl` in the model directory
3. Use `analysis.py` for batch analysis or integrate the model into your application
4. For web deployment, wrap prediction logic in a Flask/FastAPI endpoint

### Example Flask Integration

```python
from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('model/model.pkl', 'rb'))

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = np.array([[data['quality'], data['cleanliness'], 
                         data['quantity'], data['taste']]])
    prediction = model.predict(features)[0]
    return jsonify({'rating': round(prediction, 2)})
```

## Contributing

Contributions are welcome! Please follow these guidelines:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/your-feature`)
3. **Commit** your changes (`git commit -m 'Add your feature'`)
4. **Push** to the branch (`git push origin feature/your-feature`)
5. **Open** a Pull Request with a clear description

### Contribution Ideas

- Implement advanced ML models (Random Forest, SVM, Neural Networks)
- Add web interface using Flask/Streamlit
- Expand dataset with more feedback records
- Implement model performance metrics and cross-validation
- Add data preprocessing and feature scaling
- Create REST API for predictions

## License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

**Questions?** Open an issue or contact the project maintainers.
