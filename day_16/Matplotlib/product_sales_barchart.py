#5. Product Sales Bar Chart
#Scenario:
#products = ["Pen", "Book", "Pencil"]
#sales = np.array([50, 80, 40])
#Task:
#● Create DataFrame
#● Plot bar chart
#● Add labels and title

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

products = ["Pen", "Book", "Pencil"]
sales = np.array([50, 80, 40])



df = pd.DataFrame({"product":products,"sales":sales})

print(df)

plt.figure(figsize=(8,6))
plt.bar(df["product"],df["sales"])
plt.title("PRODUCT SALES BAR CHART")
plt.xlabel("producs")
plt.ylabel("sales")
plt.show()
