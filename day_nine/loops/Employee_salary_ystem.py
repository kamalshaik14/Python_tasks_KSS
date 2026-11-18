#3. Employee Salary System (Simple Inheritance)
#A company has two types of employees: Employee and Manager. Create a base class Employee containing name and salary. Create a derived class Manager that inherits from Employee and displays the employee details.


class Employee:
    def show_details(self):
        print(self.name, self.salary)


class Manager(Employee):
    pass


m = Manager()
m.name = "Ravi"
m.salary = 50000
m.show_details()
