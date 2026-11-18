#10. University Staff Management (Hierarchical Inheritance)
#A university has different staff types such as Professor, LabAssistant, and
#Administrator. All inherit from a base class Staff. Implement hierarchical inheritance to manage and display their information




class Staff:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)


class Professor(Staff):
    pass


class LabAssistant(Staff):
    pass


class Administrator(Staff):
    pass


professor = Professor("kamal")
assistant = LabAssistant("Anuhya")
administrator = Administrator("Karimulla")

professor.display()
assistant.display()
administrator.display()
