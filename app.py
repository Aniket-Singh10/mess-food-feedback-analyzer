from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# Load dataset
df = pd.read_csv('data/mess_data.csv')


# Home API
@app.route('/')
def home():
    return jsonify({
        "message": "Mess Food Feedback Analytics API Running"
    })


# Average Rating API
@app.route('/average-rating')
def average_rating():

    avg_rating = df['rating'].mean()

    return jsonify({
        "average_rating": round(avg_rating, 2)
    })


# Food Quality Analysis
@app.route('/food-quality')
def food_quality():

    avg_food_quality = df['food_quality'].mean()

    return jsonify({
        "average_food_quality": round(avg_food_quality, 2)
    })


# Cleanliness Statistics
@app.route('/cleanliness-stats')
def cleanliness_stats():

    avg_cleanliness = df['cleanliness'].mean()

    return jsonify({
        "average_cleanliness": round(avg_cleanliness, 2)
    })


# Quantity Analysis
@app.route('/quantity-analysis')
def quantity_analysis():

    avg_quantity = df['quantity'].mean()

    return jsonify({
        "average_quantity_rating": round(avg_quantity, 2)
    })


# Taste Analysis
@app.route('/taste-analysis')
def taste_analysis():

    avg_taste = df['taste'].mean()

    return jsonify({
        "average_taste_rating": round(avg_taste, 2)
    })


if __name__ == '__main__':
    app.run(debug=True)