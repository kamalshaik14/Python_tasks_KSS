# Write a program to check whether a given number is a Strong number.

number = int(input("Enter a number: "))
original = number
total = 0

while number > 0:
    digit = number % 10

    # Digit factorial calculate cheyyadam
    factorial = 1
    for i in range(1, digit + 1):
        factorial *= i

    total += factorial
    number //= 10

if total == original:
    print(original, "is a Strong number")
else:
    print(original, "is not a Strong number")
