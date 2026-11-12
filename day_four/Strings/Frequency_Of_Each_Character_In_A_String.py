#9. Write a program to count the frequency of each character in a string. 


name = "i am kamal form gudipadu"
seen =" "

for char in name:
    if char not in seen and char != " ":
        print(char,":",name.count(char))
        seen += char 

        

