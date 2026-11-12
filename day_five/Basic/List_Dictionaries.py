#9.- List of Dictionaries: Given the following data:

'''   employees = [

        {"name": "John", "age": 25, "salary": 30000},

        {"name": "Alice", "age": 30, "salary": 50000},

        {"name": "Bob", "age": 28, "salary": 40000},

        {"name": "David", "age": 35, "salary": 60000}

    ]


    Perform the following:

    * Find the employee with the highest salary.

    * Filter employees whose salary is greater than 35,000.

    * Calculate the average salary.

    * Create a list containing only employee names.'''



employees = [
    {"name": "John", "age": 25, "salary": 30000},
    {"name": "Alice", "age": 30, "salary": 50000},
    {"name": "Bob", "age": 28, "salary": 40000},
    {"name": "David", "age": 35, "salary": 60000}
]

# Highest salary
highest = employees[0]
for person in employees:
    if person["salary"] > highest["salary"]:
        highest = person
print("Highest salary:", highest["name"])

# Salary greater than 35,000
for person in employees:
    if person["salary"] > 35000:
        print("salary > 35000:",person["name"])

# Average salary
total = 0
for person in employees:
    total += person["salary"]
print("Average salary:", total / len(employees))

# Employee names
names = []
for person in employees:
    names.append(person["name"])
print("Names:", names)
