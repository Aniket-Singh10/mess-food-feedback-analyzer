import base64
import io
from datetime import datetime
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from flask import Flask, render_template, request
from sklearn.linear_model import LinearRegression
import pickle

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / 'data' / 'mess_data.csv'
MODEL_PATH = BASE_DIR / 'model' / 'model.pkl'
SUBMISSION_PATH = BASE_DIR / 'data' / 'submissions.csv'

FEATURE_COLUMNS = ['food_quality', 'cleanliness', 'quantity', 'taste']


def load_model():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(f'Model not found at {MODEL_PATH}. Train the model first.')
    with open(MODEL_PATH, 'rb') as fp:
        return pickle.load(fp)


def load_data():
    if not DATA_PATH.exists():
        raise FileNotFoundError(f'Dataset not found at {DATA_PATH}.')
    return pd.read_csv(DATA_PATH)


def load_submissions():
    if not SUBMISSION_PATH.exists():
        SUBMISSION_PATH.write_text('timestamp,food_quality,cleanliness,quantity,taste,predicted_rating\n')
    return pd.read_csv(SUBMISSION_PATH)


def save_submission(row):
    row.to_csv(SUBMISSION_PATH, mode='a', header=False, index=False)


def create_dashboard_plots(data, submissions):
    combined = pd.concat([data, submissions.rename(columns={'predicted_rating': 'rating'})], ignore_index=True, sort=False)
    feature_averages = combined[FEATURE_COLUMNS].mean().round(2)
    ratings = combined['rating'].astype(float)

    recent = submissions.sort_values(by='timestamp', ascending=True).tail(10)
    timestamps = recent['timestamp'].astype(str).tolist() if not recent.empty else []
    predicted_values = recent['predicted_rating'].astype(float).tolist() if not recent.empty else []

    # Average feature bar chart
    fig1, ax1 = plt.subplots(figsize=(7, 4), constrained_layout=True)
    ax1.bar(FEATURE_COLUMNS, feature_averages, color=['#3d7aed', '#50b5ff', '#78d479', '#f5b760'])
    ax1.set_title('Average Feedback Feature Scores')
    ax1.set_ylim(1, 5)
    ax1.set_ylabel('Score')
    ax1.grid(axis='y', linestyle='--', alpha=0.5)
    buf1 = io.BytesIO()
    fig1.savefig(buf1, format='png', dpi=100, bbox_inches='tight')
    plt.close(fig1)
    buf1.seek(0)
    plot1 = base64.b64encode(buf1.read()).decode('ascii')

    # Prediction fluctuation line chart
    fig2, ax2 = plt.subplots(figsize=(7, 4), constrained_layout=True)
    if recent.empty:
        ax2.text(0.5, 0.5, 'No submissions yet', ha='center', va='center', fontsize=12)
        ax2.set_title('Prediction Fluctuation')
        ax2.set_axis_off()
    else:
        indices = list(range(1, len(predicted_values) + 1))
        ax2.plot(indices, predicted_values, marker='o', color='#3d7aed', linewidth=2)
        ax2.scatter(indices[-1], predicted_values[-1], color='#ff4d4f', s=80, label='Latest prediction')
        ax2.axhline(ratings.mean(), color='#50b5ff', linestyle='--', label=f'Average rating {ratings.mean():.2f}')
        ax2.set_title('Prediction Fluctuation')
        ax2.set_xlabel('Recent submissions')
        ax2.set_ylabel('Predicted Rating')
        ax2.set_ylim(1, 5)
        ax2.set_xticks(indices)
        ax2.set_xticklabels(timestamps, rotation=45, ha='right')
        ax2.grid(axis='y', linestyle='--', alpha=0.5)
        ax2.legend()
    buf2 = io.BytesIO()
    fig2.savefig(buf2, format='png', dpi=100, bbox_inches='tight')
    plt.close(fig2)
    buf2.seek(0)
    plot2 = base64.b64encode(buf2.read()).decode('ascii')

    return plot1, plot2


def calculate_dashboard(data, submissions):
    combined = pd.concat([data, submissions.rename(columns={'predicted_rating': 'rating'})], ignore_index=True, sort=False)
    averages = combined[FEATURE_COLUMNS + ['rating']].mean().round(2).to_dict()
    total_feedback = len(combined)
    recent = submissions.sort_values(by='timestamp', ascending=False).head(10)
    recent = recent.assign(timestamp=recent['timestamp'].astype(str))
    recent_feedback = recent.to_dict(orient='records')

    return averages, total_feedback, recent_feedback


@app.route('/', methods=['GET', 'POST'])
def index():
    model = load_model()
    data = load_data()
    submissions = load_submissions()

    prediction = None
    warning_message = None
    if request.method == 'POST':
        form = request.form
        values = {}
        for col in FEATURE_COLUMNS:
            raw_value = form.get(col, '').strip()
            if not raw_value:
                warning_message = 'All fields are required and must be integers between 1 and 5.'
                break
            try:
                value = int(raw_value)
            except ValueError:
                warning_message = 'Please enter only integer values between 1 and 5.'
                break
            if value < 1 or value > 5:
                warning_message = 'Each feedback value must be between 1 and 5.'
                break
            values[col] = value

        if warning_message is None:
            example = pd.DataFrame([values])
            prediction_value = model.predict(example)[0]
            prediction = round(prediction_value, 2)

            submission_row = pd.DataFrame([
                {
                    'timestamp': datetime.now().isoformat(sep=' ', timespec='seconds'),
                    'food_quality': values['food_quality'],
                    'cleanliness': values['cleanliness'],
                    'quantity': values['quantity'],
                    'taste': values['taste'],
                    'predicted_rating': prediction,
                }
            ])
            save_submission(submission_row)
            submissions = pd.concat([submissions, submission_row], ignore_index=True, sort=False)

    averages, total_feedback, recent_feedback = calculate_dashboard(data, submissions)
    plot_data_1, plot_data_2 = create_dashboard_plots(data, submissions)

    return render_template(
        'index.html',
        prediction=prediction,
        warning_message=warning_message,
        averages=averages,
        total_feedback=total_feedback,
        recent_feedback=recent_feedback,
        plot_data_1=plot_data_1,
        plot_data_2=plot_data_2,
    )


if __name__ == '__main__':
    app.run(debug=True, port=5000)
