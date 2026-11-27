#2. Monthly Sales Analysis
'''Scenario:
sales = np.array([100, 150, 200, 180, 220, 300])
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
Task:
● Create DataFrame
● Plot:
○ Line graph → sales trend
○ Bar chart → month-wise comparison
○ Pie chart → contribution of each month
○ Histogram → frequency of sales values
○ Scatter plot → month index vs sales'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sales = np.array([100, 150, 200, 180, 220, 300])
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

df = pd.DataFrame({"Month": months, "Sales": sales})
print(df)

fig, ax = plt.subplots(2, 3, figsize=(10, 6))

ax[0, 0].plot(df["Month"], df["Sales"], marker="o")
ax[0, 0].set_title("Sales Trend")

ax[0, 1].bar(df["Month"], df["Sales"])
ax[0, 1].set_title("Monthly Comparison")

ax[0, 2].pie(df["Sales"], labels=df["Month"], autopct="%1.0f%%")
ax[0, 2].set_title("Monthly Contribution")

ax[1, 0].hist(df["Sales"], bins=5, edgecolor="black")
ax[1, 0].set_title("Sales Frequency")
ax[1, 0].set_xlabel("Sales")
ax[1, 0].set_ylabel("Frequency")

ax[1, 1].scatter(df.index, df["Sales"])
ax[1, 1].set_title("Month Index vs Sales")
ax[1, 1].set_xlabel("Month Index")
ax[1, 1].set_ylabel("Sales")

ax[1, 2].axis("off")

plt.tight_layout()
plt.show()

