# Mess Food Feedback Analyzer 🍽️📊

A Machine Learning-based project that analyzes and predicts mess food ratings based on different food quality parameters such as cleanliness, taste, quantity, and overall food quality.

---

## 📌 Problem Statement

Mess food quality often varies daily, causing inconsistency in:
- Food quality
- Cleanliness
- Taste
- Quantity

Students frequently face issues regarding food standards and overall dining experience.

---

## 🎯 Objective

The objective of this project is to:
- Analyze mess food feedback
- Predict food ratings using Machine Learning
- Compare different ML models for better prediction accuracy
- Visualize model performance using graphs

---

# 🚀 Features

✅ Food rating prediction using Machine Learning  
✅ Multiple ML model comparison  
✅ Graph visualization of model performance  
✅ Automatic best model selection  
✅ Model saving using Joblib  

---

# 🧠 Machine Learning Models Used

The project compares multiple machine learning models:

| Model | Purpose |
|---|---|
| Linear Regression | Baseline prediction model |
| Decision Tree Regressor | Tree-based prediction |
| Random Forest Regressor | Ensemble learning model |

---

# 📊 Evaluation Metrics

The models are evaluated using:

- R² Score
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)

---

# 🗂️ Dataset Features

The dataset contains the following features:

| Feature | Description |
|---|---|
| food_quality | Overall food quality rating |
| cleanliness | Cleanliness level |
| quantity | Food quantity satisfaction |
| taste | Taste rating |
| rating | Final predicted rating |

---

# 🛠️ Tech Stack

- Python
- Pandas
- Scikit-learn
- Matplotlib
- NumPy
- Joblib

---

# 📁 Project Structure

```bash
mess-food-feedback-analyzer/
│
├── data/
│   └── food_feedback.csv
│
├── model/
│   ├── train_model.py
│   └── model.pkl
│
├── analysis.py
├── app.py
├── README.md
└── Project_Report.pdf
```

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/mess-food-feedback-analyzer.git
```

Move into the project directory:

```bash
cd mess-food-feedback-analyzer
```

Install dependencies:

```bash
pip install pandas scikit-learn matplotlib numpy joblib
```

---

# ▶️ How to Run

## Train the Model

```bash
python model/train_model.py
```

---

# 📈 Output

The project:
- Trains multiple ML models
- Compares their performance
- Displays evaluation metrics
- Generates a comparison graph
- Saves the best-performing model automatically

---

# 📷 Sample Visualization

## Machine Learning Model Comparison

(Add screenshot here)

Example:
- Linear Regression
- Decision Tree
- Random Forest

Compared using R² Scores.

---

# 💾 Best Model Saving

The best-performing model is automatically saved as:

```bash
model/model.pkl
```

---

# 🔮 Future Improvements

- Add Deep Learning models
- Build Streamlit Web App
- Add NLP-based textual feedback analysis
- Real-time feedback collection
- Deploy project online
- Add admin dashboard

---

# 🤝 Contributing

Contributions are welcome!

If you'd like to contribute:
1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a Pull Request

---

# 👨‍💻 Contributors

- Aniket Singh
- Prince Jain

---

# ⭐ Support

If you like this project, give it a ⭐ on GitHub!