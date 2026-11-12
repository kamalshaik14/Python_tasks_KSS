#4. Write a program that searches for a number in a list and breaks the loop when found. 


numbers=[10,20,30,40,50,60]
target=20

for i in range(len(numbers)):
    
    if numbers [i] == target:
        
        print(f"{target} found at index {i}")

        break
            

        
else:
    print(f"{target} is not found on the list")
    
