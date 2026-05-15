import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def load_dataset(file_path="data/mess_data.csv"):
    """Load mess feedback dataset from CSV file."""
    return pd.read_csv(file_path)


def plot_rating_distribution(df):
    """Plot distribution of mess food ratings."""
    plt.figure(figsize=(7, 5))
    plt.hist(df["rating"], bins=5, edgecolor="black")
    plt.title("Rating Distribution")
    plt.xlabel("Rating")
    plt.ylabel("Number of Feedbacks")
    plt.tight_layout()
    plt.show()


def plot_feature_correlation(df):
    """Plot correlation heatmap between features and rating."""
    plt.figure(figsize=(8, 6))
    sns.heatmap(df.corr(), annot=True, cmap="Blues", linewidths=0.5)
    plt.title("Feature Correlation Heatmap")
    plt.tight_layout()
    plt.show()


def plot_feature_vs_rating(df):
    """Plot scatter plots for each feature against rating."""
    features = ["food_quality", "cleanliness", "quantity", "taste"]

    for feature in features:
        plt.figure(figsize=(7, 5))
        plt.scatter(df[feature], df["rating"])
        plt.title(f"{feature.replace('_', ' ').title()} vs Rating")
        plt.xlabel(feature.replace("_", " ").title())
        plt.ylabel("Rating")
        plt.tight_layout()
        plt.show()


def plot_average_feature_scores(df):
    """Plot average score of each feedback feature."""
    features = ["food_quality", "cleanliness", "quantity", "taste"]
    averages = df[features].mean()

    plt.figure(figsize=(8, 5))
    averages.plot(kind="bar", edgecolor="black")
    plt.title("Average Feature Scores")
    plt.xlabel("Features")
    plt.ylabel("Average Score")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.show()


def generate_visualizations(file_path="data/mess_data.csv"):
    """Generate all visualizations for mess feedback analysis."""
    df = load_dataset(file_path)

    plot_rating_distribution(df)
    plot_feature_correlation(df)
    plot_feature_vs_rating(df)
    plot_average_feature_scores(df)


if __name__ == "__main__":
    generate_visualizations()