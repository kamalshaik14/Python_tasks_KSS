#10. Find Indexes of Specific Value
#A quality check system stores product defect codes:[2, 4, 1, 4, 3, 4, 5]
#Task:
#● Find the indexes where value = 4 using NumPy searchin



import numpy as np

codes = [2,4,1,4,3,4,5]

arr = np.array((codes))

indexes = np.where(arr == 4)[0]

print("indexes of 4 :",indexes)
