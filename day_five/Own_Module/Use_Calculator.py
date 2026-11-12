#1 Create a Python module named calculator.py that contains functions to perform:
  # ● Addition
  # ● Subtraction
  # ● Multiplication
  # ● Division
  # Then write another Python program that imports this module and performs calculations based on user input.


import Calculator

first = float(input("enter frist number:"))
operation = input("enter an operation(+,-,*,/)")
second = float(input("enter second number:"))

if operation == "+":
    result = Calculator.add(first, second)
elif operation == "-":
    result = Calculator.subtract(first, second)
elif operation == "*":
    result = Calculator.multiply(first, second)
elif operation == "/":
    result = Calculator.divide(first, second)
else:
    print("Invalid operation")
    exit()

print("Result:", result)
