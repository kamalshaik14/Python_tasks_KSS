#6. Multi-Level List Transformation (Advanced List Comprehension)
#A dataset contains:data = [[1, 2, 3], [4, 5], [6]]
#Task:
#● Flatten the list using list comprehension.
#● Then create a new list containing squares of only even numbers.


data = [[1, 2, 3], [4, 5], [6]]

flat = [number for sublist in data for number in sublist]
even_squares = [number ** 2 for number in flat if number % 2 == 0]

print(flat)         
print(even_squares) 
