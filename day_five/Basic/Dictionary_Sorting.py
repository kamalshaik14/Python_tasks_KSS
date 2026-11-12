#* Dictionary Sorting: Given a dictionary:
 
'''    python
    students = {
        "Rahul": 85,
        "Amit": 92,
        "Priya": 78,
        "Sneha": 95
    }
    
 
    Sort the dictionary based on marks in descending order and print the top two students.'''


students = {"Rahul": 85, "Amit": 92, "Priya": 78, "Sneha": 95}

# Sort by marks, highest first
sorted_students = sorted(students, key=students.get, reverse=True)

# Print the top two
for name in sorted_students[:2]:
    print(name, students[name])
