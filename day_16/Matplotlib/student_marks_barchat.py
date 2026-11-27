#2. Student Marks Bar Chart
#Scenario:
#Marks of students:
#names = ["A", "B", "C", "D"]
#marks = np.array([70, 85, 60, 90])
#Task:
#● Create a DataFrame
#● Plot a bar graph
#● Show student names on X-axis

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


names = ["A", "B", "C", "D"]
marks = np.array([70, 85, 60, 90])

df = pd.DataFrame({"names":names,"marks":marks})
print(df)

plt.bar(df["names"],df["marks"])
plt.title("STUDENT MARKS")
plt.xlabel("student names")
plt.ylabel("marks")
plt.tight_layout()

plt.show()
