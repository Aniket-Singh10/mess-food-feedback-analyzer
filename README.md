**Mess Food Feedback Analyzer**

- **Purpose:** Analyze and predict mess food ratings using simple machine learning and visualize feedback trends.
- **Status:** Minimal proof-of-concept (data-driven analysis + linear regression model).

**Quick Links**
- **Code:** [model/train_model.py](model/train_model.py)
- **Analysis plot:** [analysis.py](analysis.py)

**Features**
- **Input factors:** `food_quality`, `cleanliness`, `quantity`, `taste`
- **Model:** Linear Regression (scikit-learn)
- **Visualization:** Average feature bar chart (matplotlib)

**Requirements**
- Python 3.8+
- See `requirements.txt` for exact packages.

**Quick Start**
1. Create a virtual environment (recommended):

```bash
python -m venv .venv
source .venv/Scripts/activate   # Windows: .venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Train the model (this saves a model file in `model/`):

```bash
python model/train_model.py
```

4. Run analysis plot (shows an average-rating bar chart):

```bash
python analysis.py
```

**Dataset**
- Place your CSV at `data/mess_data.csv`. Expected columns (case-sensitive):

```
food_quality,cleanliness,quantity,taste,rating
```

**Project Layout**
- `analysis.py`: Visualize averages using `data/mess_data.csv`.
- `model/train_model.py`: Trains and saves a Linear Regression model to `model/model.pkl`.
- `app.py`: Simple CLI to load the trained model and predict ratings.

**Notes & Tips**
- `model/train_model.py` currently trains with a default `test_size=0.2` and prints model score.
- If `model/model.pkl` is missing, run the training step before using `analysis.py`.

**Contributing**
- Improvements welcome: better models, validation, a small web UI, or richer EDA.

**License & Contact**
- Add a license file if you plan to publish.
- For questions, open an issue or email the repository owner.
