#15. Infinite Even Number Generator (Generators)
#Create a generator function that continuously generates even numbers starting from
#2. The program should print the first N even numbers using this generator.


def even_numbers():
    number = 2
    while True:
        yield number
        number += 2


n = int(input("How many even numbers? "))

generator = even_numbers()

for _ in range(n):
    print(next(generator))
