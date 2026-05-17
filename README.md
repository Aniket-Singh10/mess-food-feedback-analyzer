# 🍲 Mess Food Feedback Analyzer using Machine Learning

An end-to-end data analytics and predictive machine learning pipeline designed to quantify student feedback, analyze core satisfaction drivers, and predict overall mess service ratings in real-time.

---

## 📌 1. Problem Identification
During daily college life, it is frequently observed that students complain about mess food quality. However, these complaints are often informal, subjective, and highly inconsistent. Without a structured medium to collect and evaluate feedback, it becomes incredibly challenging to:
* **Pinpoint Root Causes:** Isolate specific operational failure points across food quality, hygiene, or taste.
* **Make Data-Driven Decisions:** Transition from opinion-based modifications to empirical, targeted service upgrades.
* **Forecast Satisfaction:** Proactively gauge student sentiment and catch deteriorating food standards early.

## 💡 2. Why This Problem Matters
Diet directly impacts student health, daily mood, and academic productivity. Poor quality or unhygienic institutional food can lead to significant dissatisfaction and widespread health risks.
By leveraging machine learning and data engineering principles:
* **Quantifiable Metrics:** Subjective student concerns are mapped directly to actionable numerical datasets.
* **Operational Visibility:** Mess administration can isolate specific programmatic areas (like hygiene vs. flavor) requiring immediate attention.
* **Empirical Accountability:** Service improvements are budgeted and tracked based on hard data rather than shifting opinions.

---

## 🛠️ 3. Technical Approach & Architecture
The system is constructed as a decoupled, modular data pipeline, ensuring clean separation of concerns between ingestion, training, analytics, and deployment:

1. **Data Ingestion (`data/`):** Processes structured feature columns mapping core feedback indicators on a standard 1–5 scale.
2. **Predictive Modeling (`model/`):** Trains a multivariate Linear Regression model, computing directional impact weights (coefficients) for each feature.
3. **Exploratory Data Analysis (`analysis.py`):** Visualizes descriptive statistical averages and extracts inter-feature collinearity matrices.
4. **Interactive Application (`app.py`):** Deploys a live dashboard via Streamlit to allow stakeholders to run real-time inference on arbitrary parameter combinations.

---

## 📁 4. Project Structure
```text
mess-food-feedback-analyzer/
├── data/
│   └── mess_data.csv       # Cleaned student feedback dataset
├── model/
│   ├── train_model.py      # Automated ML training script with error handling
│   └── model.pkl           # Serialized model artifact (generated upon execution)
├── analysis.py             # Script for Seaborn-driven data visualization & analytics
├── app.py                  # Live interactive Streamlit dashboard application
└── README.md               # Production-grade project documentation