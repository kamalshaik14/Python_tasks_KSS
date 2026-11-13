#5.Write a program to check whether a number is a Perfect number. 

number = int(input("enter a number"))

count = 0

for i in range(1,number):
    if number % i == 0:
        count += i

if count == number :
    
    print("perfect number")

else:
    print("is not a perfect number")
    
