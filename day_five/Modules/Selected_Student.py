#2. Write a program that uses random.choice() to randomly select a student from a list and display:''' The selected student for presentation is: <name> '''


import random

students = ["kamal","ayesha","nasreen","yasin","khaja"]


selected = random.choice(students)

print(f"The selected student for presentation is: {selected}")
