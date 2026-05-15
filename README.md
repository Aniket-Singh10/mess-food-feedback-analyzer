# Mess Food Feedback Analyzer 🍲

An interactive machine learning platform to analyze and predict mess food ratings based on student feedback.

## 🚀 Overview
Mess food quality varies daily, and students often face inconsistency in food quality, cleanliness, and taste. This project uses **Linear Regression** to predict ratings based on multiple factors and provides an interactive dashboard for real-time analysis.

## ✨ Features
- **Interactive Dashboard**: Built with Streamlit for a seamless user experience.
- **Real-time Prediction**: Use sliders to predict ratings for specific food scenarios.
- **Batch Processing**: Upload `.csv` or `.xlsx` files to analyze multiple feedback entries at once.
- **Data Visualization**: 
  - Average ratings per category.
  - Correlation heatmaps to see which factors influence ratings the most.
  - Automated statistical summaries for uploaded datasets.

## 🛠️ Tech Stack
- **Language**: Python 3.12
- **Framework**: Streamlit
- **Libraries**: Pandas, Scikit-learn, Matplotlib, Seaborn, Openpyxl

## 📂 Project Structure
- `app.py`: The main interactive web application.
- `analysis.py`: Basic data analysis script.
- `model/train_model.py`: Training script for the Linear Regression model.
- `model/model.pkl`: The saved pre-trained model.
- `data/mess_data.csv`: Sample dataset.

## 🚦 How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/ishwari418/mess-food-feedback-analyzer.git
cd mess-food-feedback-analyzer
```

### 2. Install Dependencies
```powershell
py -m pip install -r requirements.txt
```

### 3. Train the Model (Optional)
If you want to retrain the model with the latest data:
```powershell
cd model
py train_model.py
cd ..
```

### 4. Launch the Web Application
```powershell
py -m streamlit run app.py
```

## 📊 Output
- **Model Accuracy**: R-squared score based on historical data.
- **Visualizations**: Dynamic bar graphs and heatmaps.
- **Downloads**: Export batch prediction results as a CSV file.
