from textblob import TextBlob
import pandas as pd

# Load dataset
data = pd.read_csv('data/mess_data.csv')

# Handle missing values
data['review'] = data['review'].fillna('')

# Sentiment function
def get_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity

    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Apply sentiment analysis
data['sentiment'] = data['review'].apply(get_sentiment)

# Print results
print(data[['review', 'sentiment']])

print("\nSentiment Summary:")
print(data['sentiment'].value_counts())

import matplotlib.pyplot as plt

# Sentiment counts
sentiment_counts = data['sentiment'].value_counts()

labels = sentiment_counts.index
sizes = sentiment_counts.values

colors = ['#22c55e', '#ef4444']

fig, ax = plt.subplots(figsize=(10, 7))

# Donut chart
wedges, texts, autotexts = ax.pie(
    sizes,
    labels=labels,
    colors=colors,
    autopct=lambda pct: f"{pct:.1f}%\n({int(round(pct/100.*sum(sizes)))})",
    startangle=90,
    wedgeprops=dict(width=0.38, edgecolor='white'),
    pctdistance=0.78,
    shadow=True
)

# Style labels
plt.setp(texts, fontsize=13, fontweight='bold')
plt.setp(autotexts, fontsize=11, color='white', fontweight='bold')

# Center circle
centre_circle = plt.Circle((0, 0), 0.58, fc='white')
fig.gca().add_artist(centre_circle)

# Title
ax.set_title(
    "Mess Food Feedback Sentiment Dashboard",
    fontsize=20,
    fontweight='bold',
    pad=20
)

# Add analytics text in center
positive_count = sentiment_counts.get('Positive', 0)
negative_count = sentiment_counts.get('Negative', 0)

summary_text = (
    f"Total Reviews\n{sum(sizes)}\n\n"
    f"Positive: {positive_count}\n"
    f"Negative: {negative_count}"
)

ax.text(
    0, 0,
    summary_text,
    ha='center',
    va='center',
    fontsize=12,
    fontweight='bold'
)

# Background styling
fig.patch.set_facecolor('#f8fafc')

plt.tight_layout()
plt.show()