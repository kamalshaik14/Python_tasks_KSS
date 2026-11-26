#6. Data Analysis Tool (NumPy + Pandas)
#Scenario:
#Analyze student marks.
#Task:
#● Generate marks using NumPy
#● Convert into Pandas DataFrame
#● Use conditions to filter passing students
#● Calculate mean using math/NumPy
#● Use loop to print results


import numpy as np
import pandas as pd

# Generate marks for 5 students
marks = np.random.randint(0, 101, 5)

# Create a DataFrame
df = pd.DataFrame({
    "Student": ["A", "B", "C", "D", "E"],
    "Marks": marks
})

# Filter students who passed (50 or more)
passed = df[df["Marks"] >= 50]

# Calculate the mean
average = np.mean(marks)

# Print each passing student
for index, row in passed.iterrows():
    print(row["Student"], row["Marks"])

print("Average marks:", average)
