#10. Data Cleaning + Visualization
#Scenario:
#data = np.array([100, np.nan, 200, 150, np.nan, 300])
#Task:
#1. Convert to Pandas Series
#2. Replace NaN with mean
#3. Plot:
#○ Line graph of cleaned data
#○ Bar chart of values > average


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = np.array([100, np.nan, 200, 150, np.nan, 300])

s = pd.Series(data)
s = s.fillna(s.mean())

above_average = s[s > s.mean()]

fig, ax = plt.subplots(1, 2)

ax[0].plot(s, marker="o")
ax[0].set_title("Cleaned Data")

ax[1].bar(above_average.index, above_average)
ax[1].set_title("Values Above Average")

plt.show()
