#14. Performance Tracker (Decorators)
#A software team wants to track how long functions take to execute. Create a decorator
#that measures and prints the execution time of a function.


import time


def track_time(function):
    def wrapper():
        start = time.time()
        function()
        end = time.time()
        print("Execution time:", end - start, "seconds")
    return wrapper


@track_time
def task():
    time.sleep(1)
    print("Task completed")


task()
