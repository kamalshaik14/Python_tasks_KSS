

# Store the three subject names in a tuple
subjects = ("Math", "Science", "English")

# Use a set for unique student names and a dictionary for marks
students = set()
marks_data = {}


def add_student():
    name = input("Enter student name: ").strip()

    if name in students:
        print("Student already exists.")
        return

    marks = []

    try:
        for subject in subjects:
            mark = float(input(f"Enter marks for {subject}: "))
            marks.append(mark)
    except ValueError:
        print("Invalid input! Please enter numeric marks.")
        return

    students.add(name)
    marks_data[name] = marks
    print("Student added.")


def display_students():
    if not marks_data:
        print("No student records found.")
        return

    for name, marks in marks_data.items():
        print(f"{name} : {marks}")


def total_marks(marks):
    if not isinstance(marks, list):
        raise TypeError

    if not marks:
        return 0

    if not isinstance(marks[0], (int, float)):
        raise TypeError

    return marks[0] + total_marks(marks[1:])


def calculate_average():
    name = input("Enter student name to calculate average: ").strip()

    try:
        if name not in marks_data:
            raise NameError

        marks = marks_data[name]
        total = total_marks(marks)
        average = total / len(marks)

        print("Total Marks:", total)
        print("Average Marks:", average)

    except NameError:
        print("Student name not found.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    except TypeError:
        print("Marks data type error.")


while True:
    print("\n1. Add Student")
    print("2. Display Students")
    print("3. Calculate Average")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        calculate_average()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1-4.")
