#6. Write a program to count the number of vowels in a string. 


text= " i am shaik kamal"

vowels="aeiouAEIOU"

count = 0

for char in text:
    if char in vowels:
        count += 1


print("number of vowels:",count)


        
