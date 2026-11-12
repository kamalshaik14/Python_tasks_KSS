#19. Write a function that takes a string as input and returns the number of vowels. 


def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0

    for character in text:
        if character in vowels:
            count += 1

    return count

message = input("Enter a string: ")
print("Number of vowels:", count_vowels(message))
