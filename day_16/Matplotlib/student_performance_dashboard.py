#11. Student Performance Dashboard
#Scenario:
#A school records marks of students in one subject:
#marks = np.array([45, 67, 89, 56, 72, 91, 38])
#students = ["A", "B", "C", "D", "E", "F", "G"]
#Task:
#● Convert to Pandas DataFrame
#● Plot:
#○ Line graph → trend of marks
#○ Bar chart → student vs marks
#○ Pie chart → Pass (>50) vs Fail
#○ Histogram → distribution of marks
#○ Scatter plot → index vs marks


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

marks = np.array([45, 67, 89, 56, 72, 91, 38])
students = ["A", "B", "C", "D", "E", "F", "G"]

df = pd.DataFrame({"Student": students, "Marks": marks})

passed = sum(marks > 50)
failed = sum(marks <= 50)

fig, ax = plt.subplots(2, 3, figsize=(10, 6))

ax[0, 0].plot(df["Student"], df["Marks"], marker="o")
ax[0, 0].set_title("Line Graph")

ax[0, 1].bar(df["Student"], df["Marks"])
ax[0, 1].set_title("Bar Chart")

ax[0, 2].pie([passed, failed], labels=["Pass", "Fail"], autopct="%1.0f%%")
ax[0, 2].set_title("Pass vs Fail")

ax[1, 0].hist(df["Marks"])
ax[1, 0].set_title("Histogram")

ax[1, 1].scatter(df.index, df["Marks"])
ax[1, 1].set_title("Index vs Marks")

ax[1, 2].axis("off")  # Empty space

plt.show()
