#1. Student List Backup (Shallow Copy)
#A teacher has a list of student marks:marks = [50, 60, 70, 80]
#Scenario:
#She creates a backup using assignment:
#backup = marks
#Task:
#● Modify the first element in marks.
#● Observe the change in backup.
#● Explain why both lists are affected.


import numpy as np

marks = np.array([50,60,70,80])

backup = marks

marks[0]=25

print("marks:",marks)    
print("backup:",backup)


#Both are affected because marks and backup point to the same list
