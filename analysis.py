import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data/mess_data.csv')

# Average ratings
print("Average Ratings:")
print(data.mean())

# Plot
data.mean().plot(kind='bar')
plt.title("Average Mess Feedback")
plt.show()