#11. Boolean Masking for Salary Analysis
#Scenario:
#Employee salaries:[25000, 40000, 15000, 50000, 30000]
#Task:
#● Filter salaries above 30000.
#● Count how many employees satisfy this condition.

import numpy as np

salaries = [25000, 40000, 15000, 50000, 30000]


arr = np.array((salaries))

filtered = arr[arr > 30000]

print("above 30000 :",filtered)

print("number of employees:",len(filtered))
