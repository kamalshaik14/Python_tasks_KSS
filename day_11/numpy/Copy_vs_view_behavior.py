#13. Copy vs View Behavior in Data Processing
#Scenario:
#A dataset:[10, 20, 30, 40]
#Task:
#● Create a copy of the array.
#● Modify the original array.
#● Show that the copy does not change.
#● Repeat using view() and observe the difference.


import numpy as np

dataset = [10,20,30,40]

original = np.array((dataset))

copy = original.copy()

original[0] = 80

print("original:",original)
print("copy:",copy)


viewed = original.view()

original[0] = 75

print("original:",original)
print("view:",viewed)
