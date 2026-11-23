#12. Sorting Customer Names
#A system stores customer names:["Ravi", "Anil", "Sita", "John"]
#Task:
#● Convert it to a NumPy array.
#● Sort the names alphabetically.


import numpy as np

name = ["Ravi","Anil","Sita","John"]

arr = np.array((name))

sorting = np.sort(arr)

print("original:",arr)
print("sort the name alphabetically:",sorting)
