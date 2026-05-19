from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
with open('model/model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return '''
        <h1>Welcome to Mess Feedback Analyzer</h1>
        <p>Analyze mess data or predict satisfaction.</p>
        <a href="/analysis">View Analysis Graph</a>
    '''
@app.route('/analysis')
def show_analysis():
    return '''
        <div style="text-align: center; font-family: sans-serif;">
            <h1>Mess Food Data Analysis</h1>
            <img src="/static/analysis_plot.png" alt="Analysis Chart" style="max-width: 80%; border: 2px solid #ddd;">
            <br><br>
            <a href="/" style="text-decoration: none; color: blue;">← Back to Home</a>
        </div>
    '''
if __name__ == "__main__":
    app.run(debug=True)