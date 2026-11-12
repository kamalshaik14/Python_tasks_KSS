#16. Write a function that returns the factorial of a number. 


def factorial(number):
    result=1
    for value in range(1, number + 1):
        result*=value
    return  result

number=int(input("enter a number"))

print("factorial:",factorial(number))
