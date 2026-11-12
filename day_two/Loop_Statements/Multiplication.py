#2. Write a program to print the multiplication table of a number using a loop. 


num=int(input("ENTEER A NUMBER"))

print(f"multiplication tabule of{num}:")

for i in range (1,11):
    print(f"{num}*{i}={num*i}")
