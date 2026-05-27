import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os 
os.makedirs("plots", exist_ok=True)


# Load dataset
df = pd.read_csv("data/mess_data.csv")

# Select numerical columns
numerical_columns = df.select_dtypes(include=['int64', 'float64']).columns

print("Numerical Columns:")
print(numerical_columns)

for col in numerical_columns:

    print(f"\nAnalyzing column: {col}")

    # Calculate IQR
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # Detect outliers
    outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]

    print(f"Number of outliers in {col}: {len(outliers)}")
    if len(outliers) > 0:
        print(f"{col} contains unusual values that may affect analysis.")
    else:
        print(f"No significant outliers detected in {col}.")

    # Box Plot
    plt.figure(figsize=(8, 4))
    sns.boxplot(x=df[col])
    plt.title(f"Box Plot for {col}")
    plt.savefig(f"plots/{col}_boxplot.png")
    plt.close()

    # Distribution Plot
    plt.figure(figsize=(8, 4))
    sns.histplot(df[col], kde=True)
    plt.title(f"Distribution Plot for {col}")
    plt.savefig(f"plots/{col}_distribution.png")
    plt.close()