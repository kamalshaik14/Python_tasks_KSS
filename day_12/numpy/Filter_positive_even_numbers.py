#7. Filter Positive Even Numbers from Dataset
#Scenario:
#A dataset contains mixed values:arr = [-5, 10, 15, -2, 20, 25, 30]
#Task:
#● Convert to NumPy array.
#● Filter values that are:
#○ Positive
#○ Even

import numpy as np

values = [-5,10,15,-2,20,25,30]

arr = np.array((values))

filtered = arr[(arr>0)&(arr%2==0)]

print("positive even number :",filtered)
