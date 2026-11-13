#18. Write a function to find the sum of elements in a list using a user-defined function. 


def list_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

values = [10,20,30,40,50]

print("sum of list:",list_sum(values))
