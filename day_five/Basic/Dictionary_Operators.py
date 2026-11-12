# Create a dictionary containing student names and marks. Add a new student, update an existing student's marks, and print all student details.

students = {
    "kamal":85,
    "yasin":65,
    "ayesha":90
    }

students["nagul"]=78

students["yasin"]=95

for name,marks in students.items():
    print(name,":",marks)

