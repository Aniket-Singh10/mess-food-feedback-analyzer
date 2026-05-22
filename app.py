from flask import Flask, request

import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return '''
    <h2>Mess Food Feedback Predictor</h2>

    <form action="/predict" method="post">

        Food Quality:
        <input type="number" name="food_quality" min="1" max="5" required><br><br>

        Cleanliness:
        <input type="number" name="cleanliness" min="1" max="5" required><br><br>

        Quantity:
        <input type="number" name="quantity" min="1" max="5" required><br><br>

        Taste:
        <input type="number" name="taste" min="1" max="5" required><br><br>

        <button type="submit">Predict Rating</button>

    </form>
    '''

@app.route('/predict', methods=['POST'])
def predict():

    food_quality = float(request.form['food_quality'])
    cleanliness = float(request.form['cleanliness'])
    quantity = float(request.form['quantity'])
    taste = float(request.form['taste'])

    features = np.array([[food_quality, cleanliness, quantity, taste]])

    prediction = model.predict(features)

    return f"<h2>Predicted Rating: {prediction[0]:.2f}</h2>"

if __name__ == "__main__":
    app.run(debug=True)