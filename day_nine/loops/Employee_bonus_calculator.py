#17. Employee Bonus Calculator (Decorators & OOP)
#A company wants to apply a bonus calculation automatically before displaying the
#salary. Create an Employee class and use a decorator that modifies the salary by adding a bonus before displaying it


def add_bonus(function):
    def wrapper(self):
        function(self, self.salary + 5000)
    return wrapper


class Employee:
    def __init__(self, salary):
        self.salary = salary

    @add_bonus
    def display_salary(self, salary):
        print("Salary with bonus:", salary)


employee = Employee(30000)
employee.display_salary()
