#4.Write a program to check whether a number is Prime. 

number = int(input("enter the number"))

count = 0

for i in range(1,number + 1):

    if number % i == 0:

        count += 1

if count == 2:
    print("prime number")

else:
    print("is not a prime number")
