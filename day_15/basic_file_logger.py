#4. Basic File Logger
#Scenario:
#A system logs user actions.
#Task:
#● Take user input
#● Store logs in a file
#● Use loop to allow multiple entries
#● Handle file errors using exception handling


while True:
    action = input("Enter action (or stop): ")

    if action == "stop":
        break

    try:
        file = open("logs.txt", "a")
        file.write(action + "\n")
        file.close()
    except:
        print("File error")
