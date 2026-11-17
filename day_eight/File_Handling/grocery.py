#3. Grocery List Manager

file=open("grocery.txt","w")

while True:
    
    
    
    items = input("enter the grocery (enter the 'done' to finish):")

    if items == "done":
        break

    file.write(items + "\n")


file.close()






