#5. Write a program to assign grades based on marks (for example: A, B, C, Fail).


marks = 85

if marks >= 80:
    grade = "A"
elif marks >= 60:
    grade = "B"
elif marks >= 40:
    grade = "C"
else:
    grade = "Fail"

print("Grade:", grade)
