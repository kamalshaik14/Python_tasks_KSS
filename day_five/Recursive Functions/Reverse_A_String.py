#4. Write a recursive function to reverse a string. 


def reverse_string (s):
    if s == "":
        return s
    return reverse_string(s[1:])+s[0]

text="kamal"
print(reverse_string(text))
