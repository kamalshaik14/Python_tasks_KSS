#5. Employee Management System (OOP + File + Dict)
#Scenario:
#Manage employee data.
#Task:
#● Create a class Employee
#● Store employees in a dictionary
#● Save data to a file
#● Use exception handling for invalid salary input
#● Use loop to display all employees


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


employees = {}

while True:
    name = input("Enter employee name (or stop): ")

    if name.lower() == "stop":
        break

    try:
        salary = float(input("Enter salary: "))
        employees[name] = Employee(name, salary)
    except ValueError:
        print("Enter a valid salary.")
        continue

# Save employees to a file
try:
    with open("employees.txt", "w") as file:
        for employee in employees.values():
            file.write(f"{employee.name}, {employee.salary}\n")
except OSError:
    print("Could not save the file.")

# Display all employees
for employee in employees.values():
    print(employee.name, employee.salary)
