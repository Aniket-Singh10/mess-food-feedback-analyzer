import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent / "data" / "mess_data.csv"

def run_analysis():
    if not DATA_PATH.exists():
        print("Data file not found.")
        return

    data = pd.read_csv(DATA_PATH)
    
    # 1. Bar Plot for Averages
    plt.figure(figsize=(10, 5))
    sns.set_style("whitegrid")
    avg_ratings = data.mean()
    avg_ratings.plot(kind='bar', color=['#4e79a7', '#f28e2b', '#e15759', '#76b7b2', '#59a14f'])
    
    plt.title("Average Student Feedback Scores", fontsize=15)
    plt.ylabel("Rating (1-5)")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()

    # 2. Correlation Heatmap
    plt.figure(figsize=(8, 6))
    sns.heatmap(data.corr(), annot=True, cmap="YlGnBu")
    plt.title("Feature Correlation Map")
    plt.show()

if __name__ == "__main__":
    run_analysis()