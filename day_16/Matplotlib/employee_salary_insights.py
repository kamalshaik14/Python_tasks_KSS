#3. Employee Salary Insights
'''Scenario:
salaries = np.array([25000, 30000, 28000, 40000, 50000, 35000])
departments = ["HR", "IT", "HR", "IT", "Sales", "Sales"]
Task:
● Convert into DataFrame
● Plot:
○ Line graph → salary trend
○ Bar chart → department-wise salary comparison
○ Pie chart → department distribution
○ Histogram → salary distribution
○ Scatter plot → index vs salary'''


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

salaries = np.array([25000, 30000, 28000, 40000, 50000, 35000])
departments = ["HR", "IT", "HR", "IT", "Sales", "Sales"]

df = pd.DataFrame({"Department": departments, "Salary": salaries})
print(df)

# Average salary and employee count for each department
avg_salary = df.groupby("Department")["Salary"].mean()
employee_count = df["Department"].value_counts()

fig, ax = plt.subplots(2, 3, figsize=(10, 6))

ax[0, 0].plot(df.index, df["Salary"], marker="o")
ax[0, 0].set_title("Salary Trend")

ax[0, 1].bar(avg_salary.index, avg_salary.values)
ax[0, 1].set_title("Average Salary by Department")

ax[0, 2].pie(employee_count.values, labels=employee_count.index, autopct="%1.0f%%")
ax[0, 2].set_title("Employee Distribution")

ax[1, 0].hist(df["Salary"], bins=5, edgecolor="black")
ax[1, 0].set_title("Salary Distribution")
ax[1, 0].set_xlabel("Salary")
ax[1, 0].set_ylabel("Frequency")

ax[1, 1].scatter(df.index, df["Salary"])
ax[1, 1].set_title("Index vs Salary")
ax[1, 1].set_xlabel("Index")
ax[1, 1].set_ylabel("Salary")

ax[1, 2].axis("off")

plt.tight_layout()
plt.show()
