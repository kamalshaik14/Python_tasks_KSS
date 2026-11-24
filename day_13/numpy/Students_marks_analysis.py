#2. Student Marks Analysis
#Given marks of 5 students in 3 subjects:marks = np.array([[70, 80, 90],[60, 75, 85],[50, 65, 70],[90, 95, 85],[40, 55, 60]])
#Task:
#● Calculate total marks of each student.
#● Identify students whose total marks are above the class average.

import numpy as np


marks = np.array([[70, 80, 90],[60, 75, 85],[50, 65, 70],[90, 95, 85],[40, 55, 60]])

total = marks.sum(axis=1)
average = total.mean()
above_average = total[total > average]

print("total marks:",total)
print("average marks:",average)
print("above average marks:",above_average)
