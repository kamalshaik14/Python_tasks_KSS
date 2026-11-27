#1. Monthly Sales Line Graph
#Scenario:
#A shop records monthly sales:
#sales = np.array([100, 150, 200, 250, 300])
#months = ["Jan", "Feb", "Mar", "Apr", "May"]
#Task:
#● Convert data into a Pandas DataFrame
#● Plot a line graph
#● Label X-axis as months and Y-axis as sales


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sales = np.array([100,150,200,250,300])
months = ["Jan", "Feb", "Mar", "Apr", "May"]


df = pd.DataFrame({"sale":sales,"month":months})

print(df)

plt.plot(df["month"],df["sale"],marker = "o")
plt.xlabel("months")
plt.ylabel("sales")
plt.title("MONTHLY SALES")
plt.grid(True)


plt.show()
