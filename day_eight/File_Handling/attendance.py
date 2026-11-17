#1. Student Attendance Record

# Get the student's name
name = input("Enter the student's name: ")

# Add the name to the file
file = open("attendance.txt", "a")
file.write(name + "\n")
file.close()

# Read and display all names in the file
file = open("attendance.txt", "r")
print(file.read())
file.close()
