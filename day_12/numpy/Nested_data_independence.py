#5. Nested Data Independence (Deep Copy)
#A school stores classroom data:classes = [["Math", [30, 35]], ["Science", [25, 28]]]
#Scenario:
#● Create a deep copy of this structure.
#● Modify student count in original.
#Task:
#● Prove that copied data remains unchanged.
#● Explain why deep copy is required here

import copy

classes = [["Math", [30, 35]], ["Science", [25, 28]]]


deep = copy.deepcopy(classes)

classes[0][1][0] = 60

print("classes:",classes)
print("deep copy:",deep)


#We use deep copy so changes to nested data in the original don’t change the copied data.
