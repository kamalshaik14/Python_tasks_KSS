#7. Generator-based Log Reader
#Scenario:
#A large log file needs to be processed.
#Task:
#● Create a generator to read file line by line
#● Use loop to process logs
#● Use condition to filter errors
#● Count occurrences using a dictionary


def read_logs(filename):
    with open(filename, "r") as file:
        for line in file:
            yield line.strip()


error_counts = {}

for log in read_logs("logs.txt"):
    if "ERROR" in log:
        error_type = log.split("ERROR")[-1].strip()
        error_counts[error_type] = error_counts.get(error_type, 0) + 1

print(error_counts)
