#2. Random Number Analyzer
#Scenario:
#A system generates random numbers for testing.
#Task:
#● Use random to generate 10 numbers
#● Store in a list
#● Use loop + condition to count even/odd numbers
#● Use set to remove duplicates






import random

# Generate and store 10 numbers
numbers = [random.randint(1, 100) for  _ in range(10)]
print("Numbers:", numbers)

even = 0
odd = 0

# Count even and odd numbers
for number in numbers:
    if number % 2 == 0:
        even += 1
    else:
        odd += 1

# Remove duplicates using a set
unique_numbers = set(numbers)

print("Even count:", even)
print("Odd count:", odd)
print("Unique numbers:", unique_numbers)
