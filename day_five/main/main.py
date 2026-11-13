#4.A company wants to organize its Python code using packages.
#   Create a package named utilities that contains two modules:
#   ● math_operations.py (functions for addition and multiplication)
#   ● string_operations.py (functions to convert string to uppercase and count characters)
#   Write a Python program that imports the package and uses functions from both modules.


from utilities.math_operations import add, multiply
from utilities.string_operations import to_uppercase, count_characters

print(add(8, 4))
print(multiply(8, 4))
print(to_uppercase("hello, Python!"))
print(count_characters("hello, Python!"))
