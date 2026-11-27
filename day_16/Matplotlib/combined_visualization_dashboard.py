#9. Combined Visualization Dashboard
#Scenario:
#sales = np.array([100, 200, 150, 300])
#products = ["A", "B", "C", "D"]
#Task:
#● Create DataFrame
#● Plot:
#○ Line graph (trend)
#○ Bar chart (comparison)
#○ Pie chart (distribution)
#● Show all in single figure (subplots)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sales = np.array([100,200,150,300])
products = ["A","B","C","D"]

df = pd.DataFrame({"Sales":sales,"Product":products})
print(df)

fig,axes = plt.subplots(1,3, figsize = (12,4))

# Line graph: sales trend across products
axes[0].plot(df["Product"], df["Sales"], marker="o")
axes[0].set_title("Sales Trend")
axes[0].set_xlabel("Product")
axes[0].set_ylabel("Sales")

# Bar chart: compare sales by product
axes[1].bar(df["Product"], df["Sales"])
axes[1].set_title("Sales Comparison")
axes[1].set_xlabel("Product")
axes[1].set_ylabel("Sales")

# Pie chart: each product's share of total sales
axes[2].pie(df["Sales"], labels=df["Product"], autopct="%1.1f%%")
axes[2].set_title("Sales Distribution")

fig.tight_layout()
plt.show()
