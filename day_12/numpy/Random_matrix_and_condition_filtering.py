#10. Random Matrix and Condition Filtering
#Scenario:
#● Generate a 3×3 matrix of random numbers (0–50).
#Task:
#● Filter elements greater than 25.
#● Print filtered values.

import numpy as np

matrix = np.random.randint(1,51,size=(3,3))

filtered = matrix[matrix > 25]


print("matrix:")
print(matrix)
print("values greater than 25:")
print(filtered)


          
