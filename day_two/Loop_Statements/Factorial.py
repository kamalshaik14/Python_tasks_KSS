#5. Write a program to calculate the factorial of a number using a loop. 


n = 9

factorial = 1
for i in range(1, n + 1):
    factorial *= i

print(f"Factorial of {n} = {factorial}")
