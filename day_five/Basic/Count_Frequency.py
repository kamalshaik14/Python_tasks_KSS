#The program counts each character in "programming" and stores the counts in a dictionary.


text = "programming"
count = {}

for i in text:
    if i in count:
        count[i]+= 1
    else:
        count[i] = 1

print(count)
