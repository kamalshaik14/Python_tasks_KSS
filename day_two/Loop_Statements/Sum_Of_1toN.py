#3. Write a program to find the sum of numbers from 1 to N using a loop. 

n =int(input("enter a positive number N:"))

total=0

for i in range (1,n+1):
    total += i

print(f"sum of number from 1 to {n}={total}")
