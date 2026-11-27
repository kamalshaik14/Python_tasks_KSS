#4. Temperature Monitoring System
'''Scenario:
temps = np.array([28, 30, 32, 35, 33, 31, 29])
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
Task:
● Create DataFrame
● Plot:
○ Line graph → daily temperature trend
○ Bar chart → day-wise temperature
○ Pie chart → proportion of high (>30) vs low temps
○ Histogram → temperature frequency
○ Scatter plot → day index vs temperature'''


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

temps = np.array([28, 30, 32, 35, 33, 31, 29])
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

df = pd.DataFrame({"Day": days, "Temperature": temps})
print(df)

high = np.sum(df["Temperature"] > 30)
low = np.sum(df["Temperature"] <= 30)

fig, ax = plt.subplots(2, 3, figsize=(10, 6))

ax[0, 0].plot(df["Day"], df["Temperature"], marker="o")
ax[0, 0].set_title("Daily Temperature Trend")

ax[0, 1].bar(df["Day"], df["Temperature"])
ax[0, 1].set_title("Temperature by Day")

ax[0, 2].pie([high, low], labels=["High (>30)", "Low (<=30)"], autopct="%1.0f%%")
ax[0, 2].set_title("High vs Low Temperatures")

ax[1, 0].hist(df["Temperature"], bins=5, edgecolor="black")
ax[1, 0].set_title("Temperature Frequency")
ax[1, 0].set_xlabel("Temperature")
ax[1, 0].set_ylabel("Frequency")

ax[1, 1].scatter(df.index, df["Temperature"])
ax[1, 1].set_title("Day Index vs Temperature")
ax[1, 1].set_xlabel("Day Index")
ax[1, 1].set_ylabel("Temperature")

ax[1, 2].axis("off")

plt.tight_layout()
plt.show()
