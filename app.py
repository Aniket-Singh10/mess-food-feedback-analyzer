from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# Load dataset
df = pd.read_csv('data/mess_data.csv')


# ---------------- HOME API ----------------
@app.route('/')
def home():
    return jsonify({
        "message": "Mess Food Feedback Analytics Dashboard API Running"
    })


# ---------------- AVERAGE RATING API ----------------
@app.route('/dashboard/average-rating')
def average_rating():

    avg_rating = df['rating'].mean()

    return jsonify({
        "average_rating": round(avg_rating, 2)
    })


# ---------------- FOOD QUALITY API ----------------
@app.route('/dashboard/food-quality')
def food_quality():

    avg_food_quality = df['food_quality'].mean()

    return jsonify({
        "average_food_quality": round(avg_food_quality, 2)
    })


# ---------------- CLEANLINESS STATS API ----------------
@app.route('/dashboard/cleanliness-stats')
def cleanliness_stats():

    avg_cleanliness = df['cleanliness'].mean()

    return jsonify({
        "average_cleanliness": round(avg_cleanliness, 2)
    })


# ---------------- QUANTITY ANALYSIS API ----------------
@app.route('/dashboard/quantity-analysis')
def quantity_analysis():

    avg_quantity = df['quantity'].mean()

    return jsonify({
        "average_quantity_rating": round(avg_quantity, 2)
    })


# ---------------- TASTE ANALYSIS API ----------------
@app.route('/dashboard/taste-analysis')
def taste_analysis():

    avg_taste = df['taste'].mean()

    return jsonify({
        "average_taste_rating": round(avg_taste, 2)
    })










# ---------------- OVERALL SUMMARY API ----------------
@app.route('/dashboard/overall-summary')
def overall_summary():

    summary = {
        "average_rating": round(df['rating'].mean(), 2),
        "average_food_quality": round(df['food_quality'].mean(), 2),
        "average_cleanliness": round(df['cleanliness'].mean(), 2),
        "average_quantity": round(df['quantity'].mean(), 2),
        "average_taste": round(df['taste'].mean(), 2)
    }

    return jsonify(summary)


# ---------------- RUN APP ----------------
if __name__ == '__main__':
    app.run(debug=True)