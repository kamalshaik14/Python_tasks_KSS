#1 Student Information System (Class & Object)
# A school wants a program to store student details. Create a Student class with attributes such as name, roll number, and marks. Create objects for at least three students and display their details.


class student :
    def display_detailes (self):
        print(f"name:{self.name}")
        print(f"roll number:{self.roll_number}")
        print(f"marks : {self.marks}")


student1 = student()
student1.name = "kamal"
student1.roll_number = 140
student1.marks = 352

student2 = student()
student2.name = "yasin"
student2.roll_number = 150
student2.marks = 355

student3 = student()
student3.name = "nagul"
student3.roll_number = 160
student3.marks  = 150


for student in [student1,student2,student3]:
    student.display_detailes()
    print()


    
