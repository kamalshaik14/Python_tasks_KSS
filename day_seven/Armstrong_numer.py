#Write a program to check whether a given number is an Armstrong number or not.

number = int(input("enter the number"))

num = number

lenth = len(str(number))

total = 0

while number > 0:
    digit = number % 10
    total += digit**3
    number //= 10


if total == num:
    print("armstrong number")

else:
    print("is not a armstrong number")



