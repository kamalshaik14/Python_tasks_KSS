#8. Complex DataFrame Transformation
#A DataFrame:
#df = pd.DataFrame({"Name": ["A", "B", "C", "D"],"Marks": [50, 80, 30, 90]})
#Scenario:
#● Students scoring below 50 failed
#Task:
#1. Create a column Status ("Pass"/"Fail")
#2. Filter only passed students
#3. Calculate average marks of passed student

import pandas as pd

df = pd.DataFrame({
    "Name": ["A", "B", "C", "D"],
    "Marks": [50, 80, 30, 90]
})

df["Status"] = df["Marks"].apply(lambda mark: "Fail" if mark < 50 else "Pass")
passed = df[df["Status"] == "Pass"]
average_marks = passed["Marks"].mean()

print(passed)
print("Average marks of passed students:", average_marks)
