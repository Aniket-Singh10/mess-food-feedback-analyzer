# 🍽️ MessFood Feedback Analyzer

> An ML-powered Streamlit web app for predicting and analyzing college mess food ratings.  
> **Built for GSSoC 2026** — beginner-friendly and open for contributions!

---

## 📸 Screenshots

| Home | Single Prediction | CSV Analysis |
|------|-------------------|--------------|
| *(add screenshot)* | *(add screenshot)* | *(add screenshot)* |

---

## ✨ Features

- 🔮 **Single Prediction** — Slide 4 factors and get an instant ML-predicted rating
- 📂 **Bulk CSV Analysis** — Upload a CSV, predict ratings for all rows, download results
- 📊 **Visualizations** — Bar charts, histograms, correlation heatmaps, trend lines
- 📄 **PDF Report** — Auto-generated downloadable report with charts and insights
- 🎨 **Dark-themed UI** — Modern, responsive Streamlit design
- 🧑‍💻 **Beginner-friendly code** — Fully commented and modular

---

## 🧠 ML Model

| Property | Value |
|----------|-------|
| Algorithm | Linear Regression |
| Features | food_quality, cleanliness, quantity, taste |
| Target | rating (1–5 scale) |
| Library | scikit-learn |

---

## 📁 Folder Structure

```
mess-food-feedback-analyzer/
├── app.py                   # Main Streamlit application
├── requirements.txt         # Python dependencies
├── .gitignore
├── CONTRIBUTING.md
├── README.md
├── data/
│   ├── mess_data.csv        # Training dataset
│   └── sample_upload.csv   # Sample CSV for bulk upload testing
└── model/
    ├── train_model.py       # Model training script
    └── model.pkl            # Trained model (joblib)
```

---

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.9+
- Git

### Step 1 — Clone the repo
```bash
git clone https://github.com/<your-username>/mess-food-feedback-analyzer.git
cd mess-food-feedback-analyzer
```

### Step 2 — Create a virtual environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3 — Install dependencies
```bash
pip install -r requirements.txt
```

### Step 4 — (Optional) Retrain the model
```bash
cd model
python train_model.py
cd ..
```

### Step 5 — Run the app
```bash
streamlit run app.py
```

The app opens at **http://localhost:8501** 🚀

---

## 📤 Pushing to GitHub (First Time)

```bash
git init
git add .
git commit -m "Initial Commit: MessFood Feedback Analyzer"
git branch -M main
git remote add origin https://github.com/<your-username>/mess-food-feedback-analyzer.git
git push -u origin main
```

---

## 📊 Sample CSV Format

Upload CSVs with these exact column names:

```csv
food_quality,cleanliness,quantity,taste
4,3,5,4
3,4,3,5
```

A ready-to-use sample is at `data/sample_upload.csv`.

---

## 🔮 Future Improvements

- [ ] Add more ML models (Random Forest, XGBoost) with comparison
- [ ] User authentication for personalised history
- [ ] Time-series support (date column)
- [ ] Mobile-responsive layout improvements
- [ ] Multilingual support
- [ ] Deploy to Streamlit Cloud / Hugging Face Spaces

---

## 🤝 Contributing (GSSoC 2026)

This project is open for contributions under **GirlScript Summer of Code 2026**!

1. 🍴 Fork this repository
2. 🌿 Create a new branch: `git checkout -b feature/your-feature`
3. ✏️ Make your changes
4. 💾 Commit: `git commit -m "Add: your feature description"`
5. 📤 Push: `git push origin feature/your-feature`
6. 🔁 Open a Pull Request

Read [CONTRIBUTING.md](CONTRIBUTING.md) for full guidelines.

---

## 📄 License

This project is licensed under the **MIT License** — free to use, modify, and distribute.

---

<p align="center">Built with ❤️ for <b>GSSoC 2026</b> · MessFood Feedback Analyzer 🍽️</p>
