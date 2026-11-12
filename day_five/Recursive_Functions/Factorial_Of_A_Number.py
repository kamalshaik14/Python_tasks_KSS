#1. Write a recursive function to calculate the factorial of a number. 


def factorial(n):
    if n == 0 or n == 1:  
        return 1
    return n * factorial(n - 1)  


number = 5
print(factorial(number))
