# 🍽️ Mess Food Feedback Analyzer using Machine Learning

A Machine Learning project that analyzes and predicts mess food ratings based on different factors such as food quality, cleanliness, quantity, and taste. The project also evaluates model performance using multiple regression algorithms and visualization techniques.

---

## 📌 Problem Statement

Mess food quality varies daily, and students often face inconsistency in food quality, cleanliness, hygiene, quantity, and taste. There is no proper way to analyze feedback and predict overall food ratings.

---

## 🎯 Objective

Develop a Machine Learning model that predicts mess food ratings based on user feedback while comparing multiple regression algorithms and evaluating their performance.

---

## ✨ Features

- Predicts mess food ratings
- Uses Machine Learning regression algorithms
- Compares multiple models
- Displays evaluation metrics
- Generates correlation heatmap
- Visualizes Actual vs Predicted ratings
- Automatically saves the best-performing model

---

## 📊 Dataset Features

The model uses the following input features:

- Food Quality
- Cleanliness
- Quantity
- Taste

Target Variable:

- Rating

---

## 🤖 Machine Learning Models Used

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- Support Vector Regressor (SVR)
- XGBoost Regressor

---

## 📈 Evaluation Metrics

The project evaluates each model using:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

---

## 📉 Visualizations

### Correlation Heatmap

Shows the relationship between different input features and the target variable.

### Actual vs Predicted Plot

Compares the actual ratings with the predicted ratings to evaluate prediction accuracy.

### Model Comparison

Compares all regression models based on their R² Score and other evaluation metrics.

---

## 📂 Project Structure

```
Mess-Food-Feedback-Analyzer/
│
├── data/
│   └── mess_data.csv
│
├── model/
│   ├── train_model.py
│   └── model.pkl
│
├── analysis.py
├── app.py
├── README.md
└── requirements.txt
```

---

## 🛠️ Installation

Clone the repository

```bash
git clone https://github.com/<your-username>/Mess-Food-Feedback-Analyzer.git
```

Move into the project directory

```bash
cd Mess-Food-Feedback-Analyzer
```

Install the required dependencies

```bash
pip install -r requirements.txt
```

Or install manually

```bash
pip install pandas numpy matplotlib seaborn scikit-learn xgboost Flask
```

---

## ▶️ How to Run

Train the model

```bash
python model/train_model.py
```

Run analysis

```bash
python analysis.py
```

Run the Flask application

```bash
python app.py
```

---

## 📌 Output

The project generates:

- Predicted food ratings
- MAE
- MSE
- RMSE
- R² Score
- Correlation Heatmap
- Actual vs Predicted Plot
- Model Comparison Results
- Saved best model (`model.pkl`)

---

## 🧰 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost


---

## 🚀 Future Improvements

- Hyperparameter Tuning
- Cross Validation
- Feature Engineering
- Larger Dataset
- Real-time Feedback Collection
- Deployment on Cloud
- Interactive Dashboard using Streamlit

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push your branch

```bash
git push origin feature-name
```

5. Open a Pull Request

---

