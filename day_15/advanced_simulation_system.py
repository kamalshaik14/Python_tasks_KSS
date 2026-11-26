#10. Advanced Simulation System
#Scenario:
#Simulate exam results and generate reports.
#Task:
#● Generate random marks using random
#● Store in NumPy array
#● Convert to Pandas DataFrame
#● Use OOP to represent Student
#● Use conditions + loops to assign grades
#● Save report to file
#● Handle errors using try-except
#● Use math module for statistics



import random
import math
import numpy as np
import pandas as pd

class Student:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

try:
    names = ["Asha", "Ravi", "Sita", "Arun"]
    marks = np.array([random.randint(0, 100) for _ in names],dtype=float)

    students = []
    for name, mark in zip(names, marks):
        students.append(Student(name, mark))

    grades = []
    for student in students:
        if student.mark >= 90:
            grades.append("A")
        elif student.mark >= 75:
            grades.append("B")
        elif student.mark >= 50:
            grades.append("C")
        else:
            grades.append("Fail")

    report = pd.DataFrame({
        "Name": names,
        "Mark": marks,
        "Grade": grades
    })

    average = math.fsum(marks) / len(marks)
    report.loc[len(report)] = ["Average", average, ""]

    report.to_csv("exam_report.csv", index=False)
    print(report)
    print("Report saved to exam_report.csv")

except Exception as error:
    print("Error:", error)
