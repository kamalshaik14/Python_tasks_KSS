#9. Smart Data Processing Pipeline
#Scenario:
#A system processes numeric data from file.
#Task:
#● Read numbers from a file
#● Use NumPy for calculations (mean, std)
#● Convert results to Pandas DataFrame
#● Use exception handling for bad data
#● Use a generator to stream data
#● Apply decorator to measure execution time



import numpy as np
import pandas as pd
import time

def timer(function):
    def wrapper():
        start = time.time()
        function()
        print("Time:", time.time() - start)
    return wrapper

def read_numbers():
    with open("numbers.txt") as file:
        for line in file:
            try:
                yield float(line)
            except ValueError:
                print("Bad data:", line.strip())

@timer
def process():
    numbers = list(read_numbers())
    data = pd.DataFrame({
        "Mean": [np.mean(numbers)],
        "Standard Deviation": [np.std(numbers)]
    })
    print(data)

try:
    process()
except FileNotFoundError:
    print("numbers.txt not found")
