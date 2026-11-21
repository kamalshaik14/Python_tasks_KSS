#10. Data Processing Pipeline
#A data pipeline receives the following array:[12, 7, 25, 3, 18, 10]
#Scenario:
#1. Convert the list into a NumPy array.
#2. Sort the array.
#3. Split the sorted array into two equal parts.
#4. Calculate the sum of each part.
#Output:
#● Sorted array
#● Two split arrays
#● Sum of each part

import numpy as np

arr = np.array([12,7,25,3,18,10])


sort = np.sort(arr)

print("sorted:",sort)

parts = np.split(sort,2)

print("frist part:",parts[0])
print("second part:",parts[1])


print("sum of frist part:",np.sum(parts[0]))
print("som of second part:",np.sum(parts[1]))
