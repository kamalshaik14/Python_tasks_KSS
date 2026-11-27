#7. Filtered Bar Chart
#Scenario:
#marks = np.array([45, 80, 60, 30, 90])
#names = ["A", "B", "C", "D", "E"]
#Task:
#● Convert to DataFrame
#● Filter students with marks > 50
#● Plot bar chart only for filtered students


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

marks = np.array([45, 80, 60, 30, 90])
names = ["A", "B", "C", "D", "E"]

# Convert names and marks into a DataFrame
df = pd.DataFrame({"Name": names, "Marks": marks})
print("All students:")
print(df)

# Keep only students who scored more than 50
filtered_df = df[df["Marks"] > 50]
print("\nStudents with marks greater than 50:")
print(filtered_df)

# Plot only the filtered students
plt.bar(filtered_df["Name"], filtered_df["Marks"])
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.title("Students Scoring More Than 50")
plt.figure(figsize=(8,5))
plt.show()
