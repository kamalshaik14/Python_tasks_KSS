#1. Student Score Processor
#Scenario:
#A teacher stores student names and marks in a list of tuples.
#Task:
#● Convert data into a dictionary
#● Use a loop + condition to find students scoring above 50
#● Use math module to calculate average
#● Store results in a text file

import math

students = [("kamal",80),("yasin",75),("nagul",80),("khaja",45)]


dic = dict(students)

with open("student_result.txt","w")as file :
    for name,marks in dic.items():
        if marks > 50:
            file.write(f"{name}:{marks}\n")


    average = math.fsum(dic.values()) / len(dic)
    file.write(f"average: {average:.2f}\n")

