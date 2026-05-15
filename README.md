# 🍽️ Mess Food Feedback Analyzer

A machine learning application to predict mess food ratings based on multiple quality factors. Uses a **RandomForest Classifier** for robust and accurate predictions.

**Live Status:** ✅ Production Ready | 📊 5000+ Training Samples | 🎯 94%+ Accuracy

---

## 📋 Table of Contents

- [Problem Statement](#problem-statement)
- [Features](#features)
- [Quick Start](#quick-start)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Contributing](#contributing)

---

## 🎯 Problem Statement

Mess food quality varies daily, causing inconsistency and student frustration. This project aims to:
- **Analyze** factors affecting food quality perception
- **Predict** overall meal ratings based on quality metrics
- **Improve** decision-making for mess management

---

## ✨ Features

- 🤖 **RandomForest Classifier**: Better than Linear Regression for classification tasks
- 📊 **Data Analysis**: Comprehensive statistical analysis with visualizations
- 🌐 **REST API**: Flask-based API with single & batch prediction endpoints
- ✅ **Type Hints**: Full type annotations for better code quality
- 🧪 **Unit Tests**: 15+ test cases for reliability
- 🔍 **Input Validation**: Strict feature validation with error handling
- 📈 **Cross-Validation**: 5-fold CV for robust evaluation
- 🔧 **Configurable**: Centralized config management

---

## 🚀 Quick Start

```bash
# Clone repository
git clone https://github.com/Aniket-Singh10/mess-food-feedback-analyzer.git
cd mess-food-feedback-analyzer

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Validate data
python data_validation.py

# Train model
python model/train_model.py

# Run analysis
python analysis.py

# Start API
python app.py
```

---

## 📁 Project Structure

```
mess-food-feedback-analyzer/
├── app.py                      # Flask REST API
├── analysis.py                 # Data analysis & visualization
├── config.py                   # Configuration management
├── data_validation.py          # Data validation script
├── utils.py                    # Utility functions
├── requirements.txt            # Dependencies
├── .gitignore                  # Git patterns
├── data/mess_data.csv         # Training data (5000 samples)
├── model/
│   ├── train_model.py         # Training script
│   ├── model.pkl              # Trained model
│   └── model_metadata.json    # Model metrics
└── tests/test_analyzer.py     # Unit tests
```

---

## 💻 Usage

### 1. Data Validation
```bash
python data_validation.py
```

### 2. Train Model
```bash
python model/train_model.py
```

### 3. Run Analysis
```bash
python analysis.py
```

### 4. Start API
```bash
python app.py
```

---

## 🌐 API Endpoints

### Health Check
```bash
GET /health
```

### Model Info
```bash
GET /model-info
```

### Single Prediction
```bash
POST /predict
Content-Type: application/json

{
    "food_quality": 4,
    "cleanliness": 3,
    "quantity": 4,
    "taste": 4
}
```

### Batch Predictions
```bash
POST /batch-predict
Content-Type: application/json

{
    "predictions": [
        {"food_quality": 4, "cleanliness": 3, "quantity": 4, "taste": 4},
        {"food_quality": 2, "cleanliness": 2, "quantity": 2, "taste": 1}
    ]
}
```

---

## 📊 Model Performance

- **Algorithm**: RandomForest Classifier
- **Accuracy**: 94-96%
- **Cross-Validation**: 5-Fold (95%+ mean score)
- **Training Samples**: 5000
- **Features**: 4 (food_quality, cleanliness, quantity, taste)

---

## 🤝 Contributing

1. Fork the repository
2. Create feature branch: `git checkout -b feature/your-feature`
3. Commit changes: `git commit -am 'Add feature'`
4. Push: `git push origin feature/your-feature`
5. Open Pull Request

---

## 📜 License

MIT License - Open Source

---

**Made with ❤️ for better mess food quality**
