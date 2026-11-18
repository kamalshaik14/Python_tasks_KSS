#8. Random Number Generator (Generators)
#A program is needed to generate numbers for testing purposes. Create a generator
#function that produces numbers from 1 to N and prints them one by one when iterated.







class NumberGenerator:
    def __init__(self, n):
        self.n = n

    def generate(self):
        return list(range(1, self.n + 1))


numbers = NumberGenerator(5)

for number in numbers.generate():
    print(number)
