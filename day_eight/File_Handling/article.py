#5. Word Counter Program 
'''A writer saves an article in a file called article.txt. Write a Python program that: 
● Opens and reads the file 
● Counts the number of words, lines, and characters in the file 
● Displays the results.'''


file = open("article.txt","r")

text = file.read()
file.close()

words = text.split()
words_count = len(words)
line = text.splitlines()
line_count = len(line)
characters = len(text)

print("words:",words_count)
print("lines:",line_count)
print("characters:",characters)
