#6. Employee Salary Management System 
'''A company stores employee data in a file employees.txt in the format: 
EmployeeName Salary 
Example: 
Ramesh 25000 
Sita 30000 
Arun 28000 
Write a Python program that: 
● Reads employee data from the file 
● Displays all employee details 
● Finds the employee with the highest salary 
● Appends a new employee record to the file.'''


# Read and display employee details
file = open("employees.txt", "r")

highest_name = ""
highest_salary = 0

for line in file:
    name, salary = line.split()
    salary = int(salary)

    print(name, salary)

    if salary > highest_salary:
        highest_salary = salary
        highest_name = name

file.close()

print("Highest salary:", highest_name, highest_salary)

# Add a new employee
name = input("Enter employee name: ")
salary = input("Enter salary: ")

file = open("employees.txt", "a")
file.write(name + " " + salary + "\n")
file.close()

print("New employee added.")
