import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ==============================
# CONFIG
# ==============================
DATA_PATH = "data/mess_data.csv"
OUTPUT_DIR = "eda_outputs"

os.makedirs(OUTPUT_DIR, exist_ok=True)

sns.set_style("whitegrid")

# ==============================
# LOAD DATA
# ==============================
df = pd.read_csv(DATA_PATH)

print("\n===== DATA OVERVIEW =====")
print(df.head())
print("\nShape:", df.shape)

# ==============================
# DATA QUALITY CHECKS
# ==============================
print("\n===== DATA QUALITY CHECKS =====")
print("Missing values:\n", df.isnull().sum())
print("\nDuplicate rows:", df.duplicated().sum())

# ==============================
# STATISTICAL SUMMARY
# ==============================
print("\n===== STATISTICS =====")
print(df.describe())

# ==============================
# CORRELATION ANALYSIS
# ==============================
corr = df.corr()

plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Feature Correlation Heatmap")
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/correlation_heatmap.png")
plt.close()

# ==============================
# TARGET DISTRIBUTION
# ==============================
plt.figure(figsize=(6, 4))
sns.histplot(df["rating"], bins=10, kde=True)
plt.title("Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/rating_distribution.png")
plt.close()

# ==============================
# FEATURE IMPACT ANALYSIS
# ==============================
features = ["food_quality", "cleanliness", "quantity", "taste"]

for feature in features:
    plt.figure(figsize=(6, 4))
    sns.scatterplot(x=df[feature], y=df["rating"])
    plt.title(f"{feature} vs Rating")
    plt.xlabel(feature)
    plt.ylabel("Rating")
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/{feature}_vs_rating.png")
    plt.close()

# ==============================
# FEATURE IMPORTANCE (Simple Proxy)
# ==============================
impact = df[features + ["rating"]].corr()["rating"].drop("rating")

plt.figure(figsize=(6, 4))
impact.sort_values().plot(kind="barh")
plt.title("Feature Impact on Rating (Correlation)")
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/feature_importance.png")
plt.close()

# ==============================
# INSIGHTS GENERATION
# ==============================
print("\n===== KEY INSIGHTS =====")

strongest = impact.abs().sort_values(ascending=False)

print("Most influential feature:", strongest.index[0])
print("\nFeature correlations with rating:\n", impact.sort_values(ascending=False))

print("\nEDA completed. Outputs saved in:", OUTPUT_DIR)